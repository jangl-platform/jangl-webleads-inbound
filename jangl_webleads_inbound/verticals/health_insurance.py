from rest_framework import serializers

allow_blank = {'default': '', 'initial': '', 'allow_blank': True}
allow_null = {'default': None, 'initial': None, 'allow_null': True}
empty_list = {'default': [], 'initial': [], 'many': True}


class RelativeSerializer(serializers.Serializer):
    height = serializers.IntegerField(**allow_null)
    weight = serializers.IntegerField(**allow_null)
    birth_date = serializers.DateField(**allow_null)
    gender = serializers.CharField(max_length=1, **allow_blank)
    student = serializers.NullBooleanField(required=False)
    tobacco = serializers.NullBooleanField(required=False)
    medical_condition = serializers.CharField(max_length=200, **allow_blank)


class CurrentPolicySerializer(serializers.Serializer):
    insurance_company = serializers.CharField(max_length=50, **allow_blank)
    expiration_date = serializers.DateField(**allow_null)
    insured_since = serializers.DateField(**allow_null)


class PingDataSerializer(serializers.Serializer):
    height = serializers.IntegerField(max_value=100, **allow_null)
    weight = serializers.IntegerField(**allow_null)
    birth_date = serializers.DateField(**allow_null)
    gender = serializers.CharField(max_length=1, **allow_blank)
    student = serializers.NullBooleanField(required=False)
    tobacco = serializers.NullBooleanField(required=False)
    bmi = serializers.IntegerField(**allow_null)
    medical_condition = serializers.CharField(max_length=200, **allow_blank)
    currently_employed = serializers.NullBooleanField(required=False)
    number_in_household = serializers.IntegerField(**allow_null)
    household_income = serializers.IntegerField(**allow_null)
    hospitalized = serializers.NullBooleanField(required=False)
    ongoing_medical_treatment = serializers.NullBooleanField(required=False)
    previously_denied = serializers.NullBooleanField(required=False)
    prescriptions = serializers.NullBooleanField(required=False)
    prescription_description = serializers.CharField(max_length=255, **allow_blank)
    qualifying_life_condition = serializers.CharField(max_length=255, **allow_blank)

    spouse = RelativeSerializer(**allow_null)
    children = RelativeSerializer(**empty_list)
    current_policy = CurrentPolicySerializer(**allow_null)


class PostDataSerializer(serializers.Serializer):
    height = serializers.IntegerField(max_value=100, **allow_null)
    weight = serializers.IntegerField(**allow_null)
    birth_date = serializers.DateField(**allow_null)
    gender = serializers.CharField(max_length=1, **allow_blank)
    student = serializers.NullBooleanField(required=False)
    tobacco = serializers.NullBooleanField(required=False)
    bmi = serializers.IntegerField(**allow_null)
    medical_condition = serializers.CharField(max_length=200, **allow_blank)
    currently_employed = serializers.NullBooleanField(required=False)
    number_in_household = serializers.IntegerField(**allow_null)
    household_income = serializers.IntegerField(**allow_null)
    hospitalized = serializers.NullBooleanField(required=False)
    ongoing_medical_treatment = serializers.NullBooleanField(required=False)
    previously_denied = serializers.NullBooleanField(required=False)
    prescriptions = serializers.NullBooleanField(required=False)
    prescription_description = serializers.CharField(max_length=255, **allow_blank)
    qualifying_life_condition = serializers.CharField(max_length=255, **allow_blank)

    spouse = RelativeSerializer(**allow_null)
    children = RelativeSerializer(**empty_list)
    current_policy = CurrentPolicySerializer(**allow_null)
