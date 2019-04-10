from rest_framework import serializers

from . import verticals

allow_blank = {'default': '', 'initial': '', 'allow_blank': True}
allow_null = {'default': None, 'initial': None, 'allow_null': True}


class MetaSerializer(serializers.Serializer):
    originally_created = serializers.DateTimeField(**allow_null)
    source_id = serializers.CharField(max_length=50, **allow_blank)
    offer_id = serializers.CharField(max_length=100, **allow_blank)
    lead_id_code = serializers.CharField(max_length=36, **allow_blank)
    trusted_form_cert_url = serializers.CharField(max_length=255, **allow_blank)
    user_agent = serializers.CharField(max_length=255, **allow_blank)
    landing_page_url = serializers.CharField(max_length=200, **allow_blank)
    tcpa_compliant = serializers.NullBooleanField(required=False)
    tcpa_consent_text = serializers.CharField(**allow_blank)


class PingContactSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=50, **allow_blank)
    last_name = serializers.CharField(max_length=50, **allow_blank)
    email = serializers.EmailField(**allow_blank)
    phone = serializers.CharField(max_length=20, **allow_blank)
    phone2 = serializers.CharField(max_length=20, **allow_blank)
    phone_last_four = serializers.RegexField(r'^\d{4}$', **allow_blank)
    address = serializers.CharField(max_length=150, **allow_blank)
    address2 = serializers.CharField(max_length=150, **allow_blank)
    city = serializers.CharField(max_length=75, **allow_blank)
    state = serializers.CharField(max_length=2, **allow_blank)
    zip_code = serializers.RegexField(r'^\d{5}$')
    ip_address = serializers.IPAddressField(**allow_blank)


class PostContactSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    email = serializers.EmailField()
    phone = serializers.CharField(max_length=20)
    phone2 = serializers.CharField(max_length=20, **allow_blank)
    address = serializers.CharField(max_length=150)
    address2 = serializers.CharField(max_length=150, **allow_blank)
    city = serializers.CharField(max_length=75)
    state = serializers.CharField(max_length=2)
    zip_code = serializers.RegexField(r'^\d{5}$')
    ip_address = serializers.IPAddressField()


class BasePingSerializer(serializers.Serializer):
    meta = MetaSerializer(**allow_null)
    contact = PingContactSerializer()


class BasePostSerializer(serializers.Serializer):
    auth_code = serializers.CharField()
    meta = MetaSerializer(**allow_null)
    contact = PostContactSerializer()


class BaseDirectPostSerializer(serializers.Serializer):
    meta = MetaSerializer(**allow_null)
    contact = PostContactSerializer()


def get_inbound_serializer(inbound_type, vertical_slug):
    if inbound_type == 'ping':
        base = BasePingSerializer
        data_serializer = 'PingDataSerializer'
    elif inbound_type == 'post':
        base = BasePostSerializer
        data_serializer = 'PostDataSerializer'
    elif inbound_type == 'direct_post':
        base = BaseDirectPostSerializer
        data_serializer = 'PostDataSerializer'
    else:
        return

    if vertical_slug not in verticals.registry:
        return
    vertical = verticals.registry[vertical_slug]

    return type('InboundSerializer', (base,), {
        'data': getattr(vertical, data_serializer)()
    })
