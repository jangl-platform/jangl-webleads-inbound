from rest_framework import serializers

allow_blank = {'default': '', 'initial': '', 'allow_blank': True}
allow_null = {'default': None, 'initial': None, 'allow_null': True}
empty_list = {'default': [], 'initial': [], 'many': True}


class ClaimSerializer(serializers.Serializer):
    claim_date = serializers.DateField(**allow_null)
    type = serializers.CharField(max_length=30, **allow_blank)
    paid_amount = serializers.IntegerField(min_value=1, max_value=1e7, **allow_null)


class PropertySerializer(serializers.Serializer):
    zip_code = serializers.RegexField(r'^\d{5}$')
    property_type = serializers.CharField(max_length=30, **allow_blank)
    ownership = serializers.CharField(max_length=30, **allow_blank)
    occupancy = serializers.CharField(max_length=30, **allow_blank)
    months_at_residence = serializers.IntegerField(min_value=0, **allow_null)
    garage = serializers.CharField(max_length=30, **allow_blank)
    foundation = serializers.CharField(max_length=35, **allow_blank)
    home_security = serializers.CharField(max_length=30, **allow_blank)
    year_built = serializers.IntegerField(**allow_null)
    year_upgraded = serializers.IntegerField(**allow_null)
    stories = serializers.IntegerField(min_value=1, max_value=15, **allow_null)
    bedrooms = serializers.IntegerField(min_value=1, max_value=15, **allow_null)
    bathrooms = serializers.IntegerField(min_value=1, max_value=15, **allow_null)
    square_footage = serializers.IntegerField(min_value=100, max_value=1e5, **allow_null)
    dwelling_value = serializers.IntegerField(min_value=1000, max_value=1e9, **allow_null)
    construction_class = serializers.CharField(max_length=30, **allow_blank)
    construction_type = serializers.CharField(max_length=30, **allow_blank)
    roof_type = serializers.CharField(max_length=30, **allow_blank)
    panel_type = serializers.CharField(max_length=30, **allow_blank)
    proximity_water = serializers.CharField(max_length=30, **allow_blank)
    exterior_walls = serializers.CharField(max_length=30, **allow_blank)
    heating_type = serializers.CharField(max_length=30, **allow_blank)
    wiring_type = serializers.CharField(max_length=30, **allow_blank)
    dog = serializers.CharField(max_length=30, **allow_blank)
    newly_purchased = serializers.NullBooleanField(required=False)
    fireplace = serializers.NullBooleanField(required=False)
    deadbolt_locks = serializers.NullBooleanField(required=False)
    smoke_alarm = serializers.NullBooleanField(required=False)
    fire_alarm = serializers.NullBooleanField(required=False)
    fire_extinguisher = serializers.NullBooleanField(required=False)
    manned_fire_station_within_5_miles = serializers.NullBooleanField(required=False)
    fire_hydrant_within_1000_feet = serializers.NullBooleanField(required=False)
    indoor_sprinklers = serializers.NullBooleanField(required=False)
    copper_water_pipes = serializers.NullBooleanField(required=False)
    brush_hazard_within_500_feet = serializers.NullBooleanField(required=False)
    flood_area = serializers.NullBooleanField(required=False)
    central_air_conditioning = serializers.NullBooleanField(required=False)
    sauna = serializers.NullBooleanField(required=False)
    hot_tub = serializers.NullBooleanField(required=False)
    woodburning_stove = serializers.NullBooleanField(required=False)
    sump_pump = serializers.NullBooleanField(required=False)
    in_ground_swimming_pool = serializers.NullBooleanField(required=False)
    swimming_pool_is_fenced = serializers.NullBooleanField(required=False)
    smoker_in_household = serializers.NullBooleanField(required=False)
    trampoline = serializers.NullBooleanField(required=False)
    covered_deck_patio = serializers.NullBooleanField(required=False)
    claims = ClaimSerializer(**empty_list)


class RequestedPolicySerializer(serializers.Serializer):
    coverage_type = serializers.CharField(max_length=30, **allow_blank)
    replacement_cost = serializers.IntegerField(min_value=1e4, max_value=1e8, **allow_null)
    liability = serializers.CharField(max_length=20, **allow_blank)
    deductible = serializers.CharField(max_length=20, **allow_blank)


class CurrentPolicySerializer(serializers.Serializer):
    insurance_company = serializers.CharField(max_length=50, **allow_blank)
    expiration_date = serializers.DateField(**allow_null)
    insured_since = serializers.DateField(**allow_null)
    coverage_type = serializers.CharField(max_length=30, **allow_blank)


class PingDataSerializer(serializers.Serializer):
    birth_date = serializers.DateField(**allow_null)
    gender = serializers.CharField(max_length=1, **allow_blank)
    occupation = serializers.CharField(max_length=30, **allow_blank)
    marital_status = serializers.CharField(max_length=30, **allow_blank)
    properties = PropertySerializer(many=True)

    requested_policy = RequestedPolicySerializer()
    current_policy = CurrentPolicySerializer(**allow_null)


class PostDataSerializer(serializers.Serializer):
    birth_date = serializers.DateField(**allow_null)
    gender = serializers.CharField(max_length=1, **allow_blank)
    occupation = serializers.CharField(max_length=30, **allow_blank)
    marital_status = serializers.CharField(max_length=30, **allow_blank)
    properties = PropertySerializer(many=True, allow_empty=False)

    requested_policy = RequestedPolicySerializer()
    current_policy = CurrentPolicySerializer(**allow_null)
