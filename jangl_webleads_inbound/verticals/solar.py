from rest_framework import serializers

allow_blank = {'default': '', 'initial': '', 'allow_blank': True}


class PingDataSerializer(serializers.Serializer):
    best_call_time = serializers.CharField(**allow_blank)
    purchase_time_frame = serializers.CharField(**allow_blank)
    own_property = serializers.BooleanField(default=False)
    monthly_electric_bill = serializers.IntegerField()
    utility_provider = serializers.CharField(**allow_blank)
    roof_shade = serializers.CharField(**allow_blank)
    property_type = serializers.CharField(max_length=30, **allow_blank)
    credit_rating = serializers.CharField(max_length=50, **allow_blank)


class PostDataSerializer(serializers.Serializer):
    best_call_time = serializers.CharField(**allow_blank)
    purchase_time_frame = serializers.CharField(**allow_blank)
    own_property = serializers.BooleanField(default=False)
    monthly_electric_bill = serializers.IntegerField()
    utility_provider = serializers.CharField(**allow_blank)
    roof_shade = serializers.CharField(**allow_blank)
    property_type = serializers.CharField(max_length=30, **allow_blank)
    credit_rating = serializers.CharField(max_length=50, **allow_blank)
