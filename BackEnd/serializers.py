from rest_framework import serializers
from .models import *

class CarSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Car
        fields = "__all__"

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"

class ResiUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResiUser
        fields = "__all__"

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = "__all__"

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class ResidentialDistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResidentialDistrict
        fields = '__all__'

class UserRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRole
        fields = '__all__'

class AuthorizationStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorizationStatus
        fields = '__all__'

class AuthorizationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorizationType
        fields = '__all__'

class AccessAuthorizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessAuthorization
        fields = '__all__'

class AccessStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessStatus
        fields = '__all__'

class AccessHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessHistory
        fields = '__all__'