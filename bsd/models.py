from __future__ import unicode_literals
from dateutil import tz
from django.conf import settings
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from localflavor.us.models import USStateField
from .api import BSD
import datetime
import logging
import json


logger = logging.getLogger(__name__)

"""Get BSD api"""
bsdApi = BSD().api


class BSDProfile(models.Model):
    # 0 should only be used for legacy records that predate this field
    cons_id_default = '0'
    cons_id = models.CharField(default=cons_id_default, max_length=128)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class BSDEventManager(models.Manager):

    def from_json(self, data):

        """Assume duration type = minutes for BSD data"""
        duration_type = 1

        try:
            """Expected format for get_event_details"""
            capacity = data["days"][0]["capacity"]
            duration_count = data["days"][0]["duration"]
            start_datetime_utc = datetime.datetime.strptime(
                data["days"][0]["start_dt"],
                '%Y-%m-%d %H:%M:%S'
            )
            venue_state_or_territory = data["venue_state_code"]
        except KeyError:
            """Expected format for get_events_for_cons"""
            capacity = data["venue_capacity"]
            duration_count = data["duration"]
            start_datetime_utc = datetime.datetime.strptime(
                data["start_datetime_system"],
                '%Y-%m-%d %H:%M:%S'
            )
            venue_state_or_territory = data["venue_state_cd"]

        """Get Local Datetime"""
        utc_zone = tz.gettz('UTC')
        local_zone = tz.gettz(data["local_timezone"])
        utc_datetime = start_datetime_utc.replace(tzinfo=utc_zone)
        local_datetime = utc_datetime.astimezone(local_zone)

        bsd_event = self.model(
            capacity=capacity,
            contact_phone=data["contact_phone"],
            creator_cons_id=data["creator_cons_id"],
            event_id_obfuscated=data["event_id_obfuscated"],
            event_type=data["event_type_id"],
            flag_approval=int(data["flag_approval"]),
            host_name=data["creator_name"],
            name=data["name"],
            description=data["description"],
            duration_count=duration_count,
            duration_type=duration_type,
            host_receive_rsvp_emails=data["host_receive_rsvp_emails"],
            public_phone=data["public_phone"],
            start_day=local_datetime.date(),
            start_time=local_datetime.time(),
            start_time_zone=data["local_timezone"],
            venue_name=data["venue_name"],
            venue_addr1=data["venue_addr1"],
            venue_addr2=data["venue_addr2"],
            venue_city=data["venue_city"],
            venue_country=data["venue_country"],
            venue_directions=data["venue_directions"],
            venue_state_or_territory=venue_state_or_territory,
            venue_zip=data["venue_zip"],
        )
        return bsd_event


class BSDEvent(models.Model):
    """BSD Event"""
    objects = BSDEventManager()

    duration_type_choices = (
        (1, 'Minutes'),
        (2, 'Hours'),
    )
    event_type_choices = (
        (1, 'Volunteer Activity or Meeting'),
        (2, 'Phone Bank'),
        (3, 'Rally'),
        (4, 'Party Meetings'),
    )
    time_zone_choices = (('US/%s' % tz, tz) for tz in (
        'Eastern',
        'Central',
        'Mountain',
        'Pacific',
        'Alaska',
        'Hawaii',
    ))
    time_zone_default = 'US/Eastern'

    capacity = models.IntegerField(
        default=0,
        help_text="Including guests. Leave 0 for unlimited.",
        verbose_name='Capacity Limit',
    )
    contact_phone = models.CharField(max_length=25)
    creator_cons_id = models.CharField(max_length=128)
    event_id_obfuscated = models.CharField(max_length=128)
    event_type = models.IntegerField(
        choices=event_type_choices,
        verbose_name='Choose an Event Type',
    )
    flag_approval = models.IntegerField(
        default=1,  # default to needs approval
    )
    host_name = models.CharField(max_length=255)
    name = models.CharField(max_length=128)
    description = models.TextField()
    duration_count = models.IntegerField()
    duration_type = models.IntegerField(
        choices=duration_type_choices,
        default=1,  # default to minutes
    )
    host_receive_rsvp_emails = models.IntegerField(
        default=1,  # default to yes
        verbose_name='Notify me when new people RSVP'
    )
    public_phone = models.IntegerField(
        default=1,  # default to yes
        verbose_name='Make my phone number public to attendees'
    )
    start_day = models.DateField(verbose_name='Date')
    start_time = models.TimeField(verbose_name='Start Time')
    start_time_zone = models.CharField(
        choices=time_zone_choices,
        default=time_zone_default,
        max_length=40,
        verbose_name='Time Zone',
    )
    venue_name = models.CharField(max_length=255, verbose_name='Venue Name')
    venue_addr1 = models.CharField(
        max_length=255,
        verbose_name='Venue Address'
    )
    venue_addr2 = models.CharField(
        blank=True,
        max_length=255,
        null=True,
        verbose_name='Venue Address #2'
    )
    venue_city = models.CharField(max_length=64, verbose_name='Venue City')
    venue_country = models.CharField(
        default='US',
        max_length=2,
        verbose_name='Venue Country',
    )
    venue_directions = models.TextField(
        blank=True,
        null=True,
        verbose_name='Directions to Venue',
    )
    venue_state_or_territory = USStateField(verbose_name='Venue State')
    venue_zip = models.CharField(max_length=16, verbose_name='Venue Zip Code')

    def _get_status(self):
        if self.flag_approval == 1:
            return 'Pending Approval'
        else:
            return 'Approved'
    status = property(_get_status)

    # Duration in minutes
    def duration_minutes(self):
        # Multiply count by 60 if unit is hours
        if self.duration_type == 2:
            return self.duration_count * 60
        else:
            return self.duration_count

    # Custom logic to create event via BSD api
    def create_event(self, *args, **kwargs):
        """Create Event in BSD"""

        """Show Attendee First Names + Last Initial"""
        attendee_visibility = 'FIRST'

        """Set flag_approval to '0' for auto approval, otherwise '1'"""
        flag_approval = '0' if settings.EVENT_AUTO_APPROVAL else '1'

        '''
        Save event to BSD
        https://github.com/bluestatedigital/bsd-api-python#raw-api-method
        '''
        api_call = '/event/create_event'
        api_params = {}
        request_type = bsdApi.POST
        query = {
            'attendee_visibility': attendee_visibility,
            'capacity': self.capacity,
            'contact_phone': self.contact_phone,
            'creator_cons_id': self.creator_cons_id,
            'creator_name': self.host_name,
            'event_type_id': self.event_type,
            'days': [{
                'start_datetime_system': str(datetime.datetime.combine(
                    self.start_day,
                    self.start_time
                )),
                'duration': self.duration_minutes()
            }],
            'description': self.description,
            'flag_approval': flag_approval,
            'host_receive_rsvp_emails': self.host_receive_rsvp_emails,
            'local_timezone': self.start_time_zone,
            'name': self.name,
            'public_phone': self.public_phone,
            'venue_addr1': self.venue_addr1,
            'venue_addr2': self.venue_addr2,
            'venue_city': self.venue_city,
            'venue_directions': self.venue_directions,
            'venue_name': self.venue_name,
            'venue_state_cd': self.venue_state_or_territory,
            'venue_zip': self.venue_zip,
        }
        body = {
            'event_api_version': '2',
            'values': json.dumps(query)
        }

        apiResult = bsdApi.doRequest(api_call, api_params, request_type, body)

        try:
            # Parse and validate response
            assert apiResult.http_status is 200
            assert 'event_id_obfuscated' in json.loads(apiResult.body)
        except AssertionError:
            raise ValidationError('''
                Event creation failed, please check data and try again.
            ''')

        return

    def save(self, *args, **kwargs):

        """Create or Update event"""
        if self.event_id_obfuscated != "":
            self.update_event(*args, **kwargs)
        else:
            self.create_event(*args, **kwargs)

    def update_event(self, *args, **kwargs):
        '''
        Update Event in BSD
        https://github.com/bluestatedigital/bsd-api-python#raw-api-method
        '''
        api_call = '/event/update_event'
        api_params = {}
        request_type = bsdApi.POST
        query = {
            'capacity': self.capacity,
            'contact_phone': self.contact_phone,
            'creator_cons_id': self.creator_cons_id,
            'creator_name': self.host_name,
            'event_id_obfuscated': self.event_id_obfuscated,
            'event_type_id': self.event_type,
            'days': [{
                'start_datetime_system': str(datetime.datetime.combine(
                    self.start_day,
                    self.start_time
                )),
                'duration': self.duration_minutes()
            }],
            'description': self.description,
            'host_receive_rsvp_emails': self.host_receive_rsvp_emails,
            'local_timezone': self.start_time_zone,
            'name': self.name,
            'public_phone': self.public_phone,
            'venue_addr1': self.venue_addr1,
            'venue_addr2': self.venue_addr2,
            'venue_city': self.venue_city,
            'venue_directions': self.venue_directions,
            'venue_name': self.venue_name,
            'venue_state_cd': self.venue_state_or_territory,
            'venue_zip': self.venue_zip,
        }
        body = {
            'event_api_version': '2',
            'values': json.dumps(query)
        }

        apiResult = bsdApi.doRequest(api_call, api_params, request_type, body)

        try:
            # Parse and validate response
            assert apiResult.http_status is 200
            assert 'event_id_obfuscated' in json.loads(apiResult.body)
        except AssertionError:
            raise ValidationError('''
                Event update failed, please check data and try again.
            ''')

        return

    class Meta:
        managed = False
