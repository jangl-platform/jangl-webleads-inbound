import re
from rest_framework import serializers

ssn_re = re.compile(r'^(?P<area>\d{3})[- ]?(?P<group>\d{2})[- ]?(?P<serial>\d{4})$')

allow_blank = {'default': '', 'initial': '', 'allow_blank': True}
allow_null = {'default': None, 'initial': None, 'allow_null': True}


class PingDataSerializer(serializers.Serializer):
    ssn = serializers.RegexField(ssn_re)
    income = serializers.IntegerField(**allow_null)


class PostDataSerializer(serializers.Serializer):
    ssn = serializers.RegexField(ssn_re)
    income = serializers.IntegerField(**allow_null)
    birthdate = serializers.DateField(**allow_null)
    months_at_residence = serializers.IntegerField(min_value=0, **allow_null)
    residence_payment = serializers.IntegerField(**allow_null)
    residence_type = serializers.CharField(max_length=50, **allow_blank)
    employer = serializers.CharField(max_length=75, **allow_blank)
    months_at_employer = serializers.IntegerField(min_value=0, **allow_null)
    job_title = serializers.CharField(max_length=75, **allow_blank)
    bankruptcy = serializers.NullBooleanField(required=False)
    has_cosigner = serializers.NullBooleanField(required=False)
    credit_rating = serializers.CharField(max_length=50, **allow_blank)
    credit_check = serializers.BooleanField(initial=False, default=False)
