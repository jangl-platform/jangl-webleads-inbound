from rest_framework import serializers

allow_blank = {'default': '', 'initial': '', 'allow_blank': True}
allow_null = {'default': None, 'initial': None, 'allow_null': True}
empty_list = {'default': [], 'initial': [], 'many': True}


class TicketSerializer(serializers.Serializer):
    ticket_date = serializers.DateField(**allow_null)
    description = serializers.CharField(max_length=50, **allow_blank)


class MajorViolationSerializer(serializers.Serializer):
    violation_date = serializers.DateField(**allow_null)
    description = serializers.CharField(max_length=50, **allow_blank)
    state = serializers.CharField(max_length=2, **allow_blank)


class AccidentSerializer(serializers.Serializer):
    accident_date = serializers.DateField(**allow_null)
    description = serializers.CharField(max_length=50, **allow_blank)
    at_fault = serializers.NullBooleanField(required=False)
    damage = serializers.CharField(max_length=30, **allow_blank)


class ClaimSerializer(serializers.Serializer):
    claim_date = serializers.DateField(**allow_null)
    description = serializers.CharField(max_length=50, **allow_blank)
    paid_amount = serializers.DecimalField(max_digits=8, decimal_places=2, **allow_null)


class PingDriverSerializer(serializers.Serializer):
    birth_date = serializers.DateField(**allow_null)
    marital_status = serializers.CharField(max_length=30, **allow_blank)
    relationship = serializers.CharField(max_length=30, **allow_blank)
    gender = serializers.CharField(max_length=1, **allow_blank)
    license_status = serializers.CharField(max_length=30, **allow_blank)
    license_state = serializers.CharField(max_length=2, **allow_blank)
    license_ever_suspended = serializers.NullBooleanField(required=False)
    age_licensed = serializers.IntegerField(**allow_null)
    residence_type = serializers.CharField(max_length=30, **allow_blank)
    months_at_residence = serializers.IntegerField(**allow_null)
    occupation = serializers.CharField(max_length=50, **allow_blank)
    months_at_employer = serializers.IntegerField(**allow_null)
    education = serializers.CharField(max_length=30, **allow_blank)
    requires_sr22 = serializers.NullBooleanField(required=False)
    bankruptcy = serializers.NullBooleanField(required=False)

    tickets = TicketSerializer(**empty_list)
    major_violations = MajorViolationSerializer(**empty_list)
    accidents = AccidentSerializer(**empty_list)
    claims = ClaimSerializer(**empty_list)


class DriverSerializer(PingDriverSerializer):
    first_name = serializers.CharField(max_length=50, **allow_blank)
    last_name = serializers.CharField(max_length=50, **allow_blank)


class VehicleSerializer(serializers.Serializer):
    year = serializers.IntegerField()
    make = serializers.CharField(max_length=40, **allow_blank)
    model = serializers.CharField(max_length=40, **allow_blank)
    submodel = serializers.CharField(max_length=100, **allow_blank)
    vin = serializers.CharField(max_length=20, **allow_blank)
    salvaged = serializers.NullBooleanField(required=False)
    rental = serializers.NullBooleanField(required=False)
    towing = serializers.NullBooleanField(required=False)
    alarm = serializers.CharField(max_length=30, **allow_blank)
    four_wheel_drive = serializers.NullBooleanField(required=False)
    abs = serializers.NullBooleanField(required=False)
    airbags = serializers.NullBooleanField(required=False)
    automatic_seat_belts = serializers.NullBooleanField(required=False)
    garage = serializers.CharField(max_length=30, **allow_blank)
    ownership = serializers.CharField(max_length=10, **allow_blank)
    primary_use = serializers.CharField(max_length=30, **allow_blank)
    annual_miles = serializers.IntegerField(**allow_null)
    weekly_commute_days = serializers.IntegerField(**allow_null)
    one_way_distance = serializers.IntegerField(**allow_null)
    comprehensive_deductible = serializers.CharField(max_length=30, **allow_blank)
    collision_deductible = serializers.CharField(max_length=30, **allow_blank)


class RequestedPolicySerializer(serializers.Serializer):
    coverage_type = serializers.CharField(max_length=30, **allow_blank)
    bodily_injury = serializers.CharField(max_length=10, **allow_blank)
    property_damage = serializers.IntegerField(**allow_null)


class CurrentPolicySerializer(serializers.Serializer):
    insurance_company = serializers.CharField(max_length=50, **allow_blank)
    expiration_date = serializers.DateField(**allow_null)
    insured_since = serializers.DateField(**allow_null)
    coverage_type = serializers.CharField(max_length=30, **allow_blank)


class PingDataSerializer(serializers.Serializer):
    drivers = PingDriverSerializer(many=True, allow_empty=False)
    vehicles = VehicleSerializer(many=True, allow_empty=False)
    requested_policy = RequestedPolicySerializer()
    current_policy = CurrentPolicySerializer(**allow_null)


class PostDataSerializer(serializers.Serializer):
    drivers = DriverSerializer(many=True, allow_empty=False)
    vehicles = VehicleSerializer(many=True, allow_empty=False)
    requested_policy = RequestedPolicySerializer()
    current_policy = CurrentPolicySerializer(**allow_null)
