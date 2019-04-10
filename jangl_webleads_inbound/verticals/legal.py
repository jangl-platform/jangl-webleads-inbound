from rest_framework import serializers

allow_blank = {'default': '', 'initial': '', 'allow_blank': True}
allow_null = {'default': None, 'initial': None, 'allow_null': True}


class PingDataSerializer(serializers.Serializer):
    type_of_legal_problem = serializers.CharField()
    description = serializers.CharField(**allow_blank)
    best_time_to_contact = serializers.CharField(**allow_blank)

    total_debt = serializers.IntegerField(min_value=0, **allow_null)
    monthly_income = serializers.IntegerField(min_value=0, **allow_null)
    total_assets_value = serializers.IntegerField(min_value=0, **allow_null)
    owns_real_estate = serializers.NullBooleanField(required=False)
    business_owner = serializers.NullBooleanField(required=False)
    currently_has_attorney = serializers.NullBooleanField(required=False)

    incident_date = serializers.DateField(**allow_null)
    applicant_age = serializers.IntegerField(min_value=0, **allow_null)
    condition_num_years = serializers.IntegerField(min_value=0, **allow_null)
    work_reduction = serializers.NullBooleanField(required=False)
    previously_applied = serializers.NullBooleanField(required=False)
    claim_pending = serializers.NullBooleanField(required=False)
    doctor_treatment = serializers.NullBooleanField(required=False)
    current_benefits = serializers.NullBooleanField(required=False)
    criminal_charges_against_me = serializers.NullBooleanField(required=False)
    criminal_charges_against_other = serializers.NullBooleanField(required=False)


class PostDataSerializer(serializers.Serializer):
    type_of_legal_problem = serializers.CharField()
    description = serializers.CharField()
    best_time_to_contact = serializers.CharField()

    total_debt = serializers.IntegerField(min_value=0, **allow_null)
    monthly_income = serializers.IntegerField(min_value=0, **allow_null)
    total_assets_value = serializers.IntegerField(min_value=0, **allow_null)
    owns_real_estate = serializers.NullBooleanField(required=False)
    business_owner = serializers.NullBooleanField(required=False)
    currently_has_attorney = serializers.NullBooleanField(required=False)

    incident_date = serializers.DateField(**allow_null)
    applicant_age = serializers.IntegerField(min_value=0, **allow_null)
    condition_num_years = serializers.IntegerField(min_value=0, **allow_null)
    work_reduction = serializers.NullBooleanField(required=False)
    previously_applied = serializers.NullBooleanField(required=False)
    claim_pending = serializers.NullBooleanField(required=False)
    doctor_treatment = serializers.NullBooleanField(required=False)
    current_benefits = serializers.NullBooleanField(required=False)
    criminal_charges_against_me = serializers.NullBooleanField(required=False)
    criminal_charges_against_other = serializers.NullBooleanField(required=False)
