from rest_framework import serializers

allow_blank = {'default': '', 'initial': '', 'allow_blank': True}
allow_null = {'default': None, 'initial': None, 'allow_null': True}


class PingDataSerializer(serializers.Serializer):
    birth_date = serializers.DateField(**allow_null)
    year = serializers.IntegerField(**allow_null)
    make = serializers.CharField(**allow_blank)
    model = serializers.CharField(**allow_blank)
    mileage = serializers.CharField(**allow_blank)


class PostDataSerializer(serializers.Serializer):
    birth_date = serializers.DateField(**allow_null)
    year = serializers.IntegerField(**allow_null)
    make = serializers.CharField(**allow_blank)
    model = serializers.CharField(**allow_blank)
    mileage = serializers.CharField(**allow_blank)
