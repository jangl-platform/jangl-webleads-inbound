from rest_framework import serializers

allow_blank = {'default': '', 'initial': '', 'allow_blank': True}
allow_null = {'default': None, 'initial': None, 'allow_null': True}
empty_list = {'default': [], 'initial': [], 'many': True}


class PersonSerializer(serializers.Serializer):
    birth_date = serializers.DateField(**allow_null)
    gender = serializers.CharField(max_length=1, **allow_blank)
    height = serializers.IntegerField(**allow_null)
    weight = serializers.IntegerField(**allow_null)
    residence_type = serializers.CharField(max_length=20, **allow_blank)
    months_at_current_residence = serializers.IntegerField(**allow_null)
    marital_status = serializers.CharField(max_length=50, **allow_blank)
    education = serializers.CharField(max_length=50, **allow_blank)
    occupation = serializers.CharField(max_length=50, **allow_blank)
    relationship_to_applicant = serializers.CharField(max_length=50, **allow_blank)
    student = serializers.NullBooleanField(required=False)
    tobacco = serializers.NullBooleanField(required=False)
    expectant_parent = serializers.NullBooleanField(required=False)
    relative_heart = serializers.NullBooleanField(required=False)
    relative_cancer = serializers.NullBooleanField(required=False)
    hospitalized = serializers.NullBooleanField(required=False)
    ongoing_medical_treatment = serializers.NullBooleanField(required=False)
    dui = serializers.NullBooleanField(required=False)
    previously_denied = serializers.NullBooleanField(required=False)
    hazard_pilot = serializers.NullBooleanField(required=False)
    hazard_felony = serializers.NullBooleanField(required=False)
    hazard_other = serializers.NullBooleanField(required=False)
    hazardous_activity = serializers.NullBooleanField(required=False)
    medical_condition = serializers.CharField(max_length=200, **allow_blank)

    def to_internal_value(self, data):
        if 'DUI' in data:
            data['dui'] = data.pop('DUI')
        return super(PersonSerializer, self).to_internal_value(data)


class MedicationSerializer(serializers.Serializer):
    medication_name = serializers.CharField(max_length=50, **allow_blank)
    dosage = serializers.CharField(max_length=30, **allow_blank)
    frequency = serializers.CharField(max_length=30, **allow_blank)
    comment = serializers.CharField(max_length=30, **allow_blank)


class RequestedPolicySerializer(serializers.Serializer):
    coverage_type = serializers.CharField(max_length=30, **allow_blank)
    coverage_amount = serializers.CharField(max_length=20, **allow_blank)
    coverage_term = serializers.CharField(max_length=20, **allow_blank)


class CurrentPolicySerializer(serializers.Serializer):
    insurance_company = serializers.CharField(max_length=50, **allow_blank)
    expiration_date = serializers.DateField(**allow_null)
    insured_since = serializers.DateField(**allow_null)
    coverage_type = serializers.CharField(max_length=30, **allow_blank)


class PingDataSerializer(serializers.Serializer):
    persons = PersonSerializer(many=True, allow_empty=False)
    medications = MedicationSerializer(**empty_list)
    requested_policy = RequestedPolicySerializer(**allow_null)
    current_policy = CurrentPolicySerializer(**allow_null)


class PostDataSerializer(serializers.Serializer):
    persons = PersonSerializer(many=True, allow_empty=False)
    medications = MedicationSerializer(**empty_list)
    requested_policy = RequestedPolicySerializer(**allow_null)
    current_policy = CurrentPolicySerializer(**allow_null)
