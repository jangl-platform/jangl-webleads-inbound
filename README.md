# Jangl Webleads Inbound

We have included the data serializers for our inbound ping post API. You
should be able to use this to parse inbound ping post API traffic.

## Installation

To install Jangl Webleads Inbound, run this command in your terminal:
```
pip install -i https://pypi.jangl.com/pypi/ jangl-webleads-inbound
```

## Usage

You can use `get_inbound_serializer(inbound_type, vertical_slug)` to load the
appropriate serializer to process inbound ping post data. Valid attribute
values are:

##### `inbound_type`
- ping
- post
- direct_post

##### `vertical_slug`
- auto_finance
- auto_insurance
- auto_warranty
- health_insurance
- home_improvement
- home_insurance
- legal
- life_insurance
- solar

### Example

```python
>>> from jangl_webleads_inbound import get_inbound_serializer
>>> serializer_class = get_inbound_serializer('ping', 'auto_insurance')
>>> serializer_class()
InboundSerializer():
    meta = MetaSerializer(allow_null=True, default=None, initial=None):
        originally_created = DateTimeField(allow_null=True, default=None, initial=None)
        source_id = CharField(allow_blank=True, default='', initial='', max_length=50)
        offer_id = CharField(allow_blank=True, default='', initial='', max_length=100)
        lead_id_code = CharField(allow_blank=True, default='', initial='', max_length=36)
        trusted_form_cert_url = CharField(allow_blank=True, default='', initial='', max_length=255)
        user_agent = CharField(allow_blank=True, default='', initial='', max_length=255)
        landing_page_url = CharField(allow_blank=True, default='', initial='', max_length=200)
        tcpa_compliant = NullBooleanField(required=False)
        tcpa_consent_text = CharField(allow_blank=True, default='', initial='')
    contact = PingContactSerializer():
        first_name = CharField(allow_blank=True, default='', initial='', max_length=50)
        last_name = CharField(allow_blank=True, default='', initial='', max_length=50)
        email = EmailField(allow_blank=True, default='', initial='')
        phone = CharField(allow_blank=True, default='', initial='', max_length=20)
        phone2 = CharField(allow_blank=True, default='', initial='', max_length=20)
        phone_last_four = RegexField('^\\d{4}$', allow_blank=True, default='', initial='')
        address = CharField(allow_blank=True, default='', initial='', max_length=150)
        address2 = CharField(allow_blank=True, default='', initial='', max_length=150)
        city = CharField(allow_blank=True, default='', initial='', max_length=75)
        state = CharField(allow_blank=True, default='', initial='', max_length=2)
        zip_code = RegexField('^\\d{5}$')
        ip_address = IPAddressField(allow_blank=True, default='', initial='')
    data = PingDataSerializer():
        drivers = PingDriverSerializer(allow_empty=False, many=True):
            birth_date = DateField(allow_null=True, default=None, initial=None)
            marital_status = CharField(allow_blank=True, default='', initial='', max_length=30)
            relationship = CharField(allow_blank=True, default='', initial='', max_length=30)
            gender = CharField(allow_blank=True, default='', initial='', max_length=1)
            license_status = CharField(allow_blank=True, default='', initial='', max_length=30)
            license_state = CharField(allow_blank=True, default='', initial='', max_length=2)
            license_ever_suspended = NullBooleanField(required=False)
            age_licensed = IntegerField(allow_null=True, default=None, initial=None)
            residence_type = CharField(allow_blank=True, default='', initial='', max_length=30)
            months_at_residence = IntegerField(allow_null=True, default=None, initial=None)
            occupation = CharField(allow_blank=True, default='', initial='', max_length=50)
            months_at_employer = IntegerField(allow_null=True, default=None, initial=None)
            education = CharField(allow_blank=True, default='', initial='', max_length=30)
            requires_sr22 = NullBooleanField(required=False)
            bankruptcy = NullBooleanField(required=False)
            tickets = TicketSerializer(default=[], initial=[], many=True):
                ticket_date = DateField(allow_null=True, default=None, initial=None)
                description = CharField(allow_blank=True, default='', initial='', max_length=50)
            major_violations = MajorViolationSerializer(default=[], initial=[], many=True):
                violation_date = DateField(allow_null=True, default=None, initial=None)
                description = CharField(allow_blank=True, default='', initial='', max_length=50)
                state = CharField(allow_blank=True, default='', initial='', max_length=2)
            accidents = AccidentSerializer(default=[], initial=[], many=True):
                accident_date = DateField(allow_null=True, default=None, initial=None)
                description = CharField(allow_blank=True, default='', initial='', max_length=50)
                at_fault = NullBooleanField(required=False)
                damage = CharField(allow_blank=True, default='', initial='', max_length=30)
            claims = ClaimSerializer(default=[], initial=[], many=True):
                claim_date = DateField(allow_null=True, default=None, initial=None)
                description = CharField(allow_blank=True, default='', initial='', max_length=50)
                paid_amount = DecimalField(allow_null=True, decimal_places=2, default=None, initial=None, max_digits=8)
        vehicles = VehicleSerializer(allow_empty=False, many=True):
            year = IntegerField()
            make = CharField(allow_blank=True, default='', initial='', max_length=40)
            model = CharField(allow_blank=True, default='', initial='', max_length=40)
            submodel = CharField(allow_blank=True, default='', initial='', max_length=100)
            vin = CharField(allow_blank=True, default='', initial='', max_length=20)
            salvaged = NullBooleanField(required=False)
            rental = NullBooleanField(required=False)
            towing = NullBooleanField(required=False)
            alarm = CharField(allow_blank=True, default='', initial='', max_length=30)
            four_wheel_drive = NullBooleanField(required=False)
            abs = NullBooleanField(required=False)
            airbags = NullBooleanField(required=False)
            automatic_seat_belts = NullBooleanField(required=False)
            garage = CharField(allow_blank=True, default='', initial='', max_length=30)
            ownership = CharField(allow_blank=True, default='', initial='', max_length=10)
            primary_use = CharField(allow_blank=True, default='', initial='', max_length=30)
            annual_miles = IntegerField(allow_null=True, default=None, initial=None)
            weekly_commute_days = IntegerField(allow_null=True, default=None, initial=None)
            one_way_distance = IntegerField(allow_null=True, default=None, initial=None)
            comprehensive_deductible = CharField(allow_blank=True, default='', initial='', max_length=30)
            collision_deductible = CharField(allow_blank=True, default='', initial='', max_length=30)
        requested_policy = RequestedPolicySerializer():
            coverage_type = CharField(allow_blank=True, default='', initial='', max_length=30)
            bodily_injury = CharField(allow_blank=True, default='', initial='', max_length=10)
            property_damage = IntegerField(allow_null=True, default=None, initial=None)
        current_policy = CurrentPolicySerializer(allow_null=True, default=None, initial=None):
            insurance_company = CharField(allow_blank=True, default='', initial='', max_length=50)
            expiration_date = DateField(allow_null=True, default=None, initial=None)
            insured_since = DateField(allow_null=True, default=None, initial=None)
            coverage_type = CharField(allow_blank=True, default='', initial='', max_length=30)
```

## Development/Testing

#### Environment

These serializers require `Django` and `djangorestframework`. If you have
pipenv installed, you can install a sandbox environment with `pipenv install`.

#### Python shell

If you would like to launch a Python shell to interact with this code, you
can bootstrap a Django environment with `./manage.py shell`.
