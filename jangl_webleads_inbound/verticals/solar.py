from rest_framework import serializers

allow_blank = {'default': '', 'initial': '', 'allow_blank': True}


class PingDataSerializer(serializers.Serializer):
    best_call_time = serializers.CharField()
    purchase_time_frame = serializers.CharField()
    own_property = serializers.BooleanField()
    monthly_electric_bill = serializers.IntegerField()
    utility_provider = serializers.CharField()
    property_type = serializers.CharField(max_length=30, **allow_blank)
    credit_rating = serializers.CharField(max_length=50, **allow_blank)


class PostDataSerializer(serializers.Serializer):
    best_call_time = serializers.CharField()
    purchase_time_frame = serializers.CharField()
    own_property = serializers.BooleanField()
    monthly_electric_bill = serializers.IntegerField()
    utility_provider = serializers.CharField()
    property_type = serializers.CharField(max_length=30, **allow_blank)
    credit_rating = serializers.CharField(max_length=50, **allow_blank)
