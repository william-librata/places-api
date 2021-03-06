from rest_framework import serializers
from rest_framework.reverse import reverse
from places.models import State, Locality, LocalityClassAut, GeocodeReliabilityAut, Address
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'last_login']


class StateSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='state-detail', read_only=True, lookup_field='state_pid')

    class Meta:
        model = State
        fields = '__all__'


class LocalitySerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='locality-detail', read_only=True, lookup_field='locality_pid')
    state_pid = serializers.HyperlinkedRelatedField(view_name='state-detail', read_only=True, lookup_field='state_pid')

    class Meta:
        model = Locality
        fields = '__all__'


class LocalityClassAutSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LocalityClassAut
        fields = '__all__'


class GeocodeReliabilityAutSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GeocodeReliabilityAut
        fields = '__all__'


class AddressSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='address-detail', lookup_field='address_detail_pid')

    class Meta:
        model = Address
        fields = ['url', 'address_detail_pid', 'date_created', 'date_last_modified', 'date_retired', 'building_name',
                  'lot_number_combined', 'flat_number_combined', 'level_number_combined',
                  'house_number', 'street_name', 'street_type', 'street_suffix_name', 'street',
                  'locality_name', 'state', 'postcode', 'latitude', 'longitude']


class ParsedAddressSerializer(serializers.Serializer):
    house = serializers.CharField()
    category = serializers.CharField()
    near = serializers.CharField()
    house_number = serializers.CharField()
    road = serializers.CharField()
    unit = serializers.CharField()
    level = serializers.CharField()
    staircase = serializers.CharField()
    entrance = serializers.CharField()
    po_box = serializers.CharField()
    postcode = serializers.CharField()
    suburb = serializers.CharField()
    city_district = serializers.CharField()
    city = serializers.CharField()
    island = serializers.CharField()
    state_district = serializers.CharField()
    state = serializers.CharField()
    country_region = serializers.CharField()
    country = serializers.CharField()
    world_region = serializers.CharField()


class GeocodeResultSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='address-detail', lookup_field='address_detail_pid')

    class Meta:
        model = Address
        fields = ['url', 'address_detail_pid', 'latitude', 'longitude']
