from rest_framework import serializers

allow_blank = {'default': '', 'initial': '', 'allow_blank': True}
allow_null = {'default': None, 'initial': None, 'allow_null': True}


class AdditionSerializer(serializers.Serializer):
    addition_type = serializers.CharField()
    square_footage = serializers.IntegerField(min_value=1, **allow_null)


class BathroomSerializer(serializers.Serializer):
    project_type = serializers.CharField()


class CabinetSerializer(serializers.Serializer):
    project_type = serializers.CharField()
    location_in_house = serializers.CharField(**allow_blank)
    current_materials = serializers.CharField(**allow_blank)
    reface = serializers.CharField(**allow_blank)


class DeckSerializer(serializers.Serializer):
    material = serializers.CharField()
    length = serializers.IntegerField(min_value=1, **allow_null)
    width = serializers.IntegerField(min_value=1, **allow_null)


class DoorSerializer(serializers.Serializer):
    project_type = serializers.CharField()
    material = serializers.CharField()
    pre_hung = serializers.BooleanField()


class ElectricalSerializer(serializers.Serializer):
    project_type = serializers.CharField()
    service_type = serializers.CharField()


class FencingSerializer(serializers.Serializer):
    fence_type = serializers.CharField()
    length = serializers.IntegerField(min_value=1, **allow_null)
    width = serializers.IntegerField(min_value=1, **allow_null)


class FlooringSerializer(serializers.Serializer):
    flooring_type = serializers.CharField()
    inquiry_type = serializers.CharField()


class GarageDoorSerializer(serializers.Serializer):
    project_type = serializers.CharField()
    num_doors = serializers.IntegerField(min_value=1)
    openers = serializers.BooleanField()


class GutterSerializer(serializers.Serializer):
    protection = serializers.BooleanField()


class HandyManSerializer(serializers.Serializer):
    location_in_home = serializers.CharField(**allow_blank)
    service_type = serializers.CharField(**allow_blank)


class HomeSecuritySerializer(serializers.Serializer):
    building_type = serializers.CharField()
    usage = serializers.CharField()


class HVACSerializer(serializers.Serializer):
    project_type = serializers.CharField()
    air_type = serializers.CharField()
    system_type = serializers.CharField()


class InsulationSerializer(serializers.Serializer):
    service_type = serializers.CharField()


class KitchenSerializer(serializers.Serializer):
    project_type = serializers.CharField()
    cabinet_job = serializers.CharField(**allow_blank)


class PaintingSerializer(serializers.Serializer):
    project_type = serializers.CharField()


class PlumbingSerializer(serializers.Serializer):
    project_type = serializers.CharField()
    service_type = serializers.CharField()


class RoofSerializer(serializers.Serializer):
    project_type = serializers.CharField()
    roofing_type = serializers.CharField()


class SidingSerializer(serializers.Serializer):
    siding_type = serializers.CharField()
    project_type = serializers.CharField()


class SunroomSerializer(serializers.Serializer):
    num_rooms = serializers.IntegerField(min_value=1)
    length = serializers.IntegerField(min_value=1)
    width = serializers.IntegerField(min_value=1)


class WindowSerializer(serializers.Serializer):
    project_type = serializers.CharField()
    num_windows = serializers.IntegerField(min_value=1)


CATEGORIES = (
    ('additions', AdditionSerializer),
    ('bathroom', BathroomSerializer),
    ('cabinets', CabinetSerializer),
    ('deck', DeckSerializer),
    ('doors', DoorSerializer),
    ('electrical', ElectricalSerializer),
    ('fencing', FencingSerializer),
    ('flooring', FlooringSerializer),
    ('garage_doors', GarageDoorSerializer),
    ('gutters', GutterSerializer),
    ('handy_man', HandyManSerializer),
    ('home_security', HomeSecuritySerializer),
    ('hvac', HVACSerializer),
    ('insulation', InsulationSerializer),
    ('kitchen', KitchenSerializer),
    ('painting', PaintingSerializer),
    ('plumbing', PlumbingSerializer),
    ('roof', RoofSerializer),
    ('siding', SidingSerializer),
    ('sunrooms', SunroomSerializer),
    ('windows', WindowSerializer),
)


class BaseSerializer(serializers.Serializer):
    best_call_time = serializers.CharField()
    purchase_time_frame = serializers.CharField()
    own_property = serializers.BooleanField()

    def validate(self, attrs):
        categories = dict(CATEGORIES)
        num_categories = 0

        for key, value in attrs.iteritems():
            if value and key in categories:
                num_categories += 1

        if num_categories != 1:
            raise serializers.ValidationError(
                'You must send exactly one home improvement category.'
            )

        return attrs


def create_serializer(class_name):
    return type(class_name, (BaseSerializer,), {
        field: serializer(**allow_null)
        for field, serializer in CATEGORIES
    })


PingDataSerializer = create_serializer('PingDataSerializer')
PostDataSerializer = create_serializer('PostDataSerializer')
