from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import CarSerializer, BrandSerializer, ResiUserSerializer,  CitySerializer, CountrySerializer, ResidentialDistrictSerializer
from .serializers import UserRoleSerializer, AuthorizationStatusSerializer, AuthorizationTypeSerializer, AccessAuthorizationSerializer
from .serializers import AccessStatusSerializer, AccessHistorySerializer


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class ResiUserViewSet(viewsets.ModelViewSet):
    queryset = ResiUser.objects.all()
    serializer_class = ResiUserSerializer

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class ResidentialDistrictViewSet(viewsets.ModelViewSet):
    queryset = ResidentialDistrict.objects.all()
    serializer_class = ResidentialDistrictSerializer

class UserRoleViewSet(viewsets.ModelViewSet):
    queryset = UserRole.objects.all()
    serializer_class = UserRoleSerializer

class AuthorizationStatusViewSet(viewsets.ModelViewSet):
    queryset = AuthorizationStatus.objects.all()
    serializer_class = AuthorizationStatusSerializer

class AuthorizationTypeViewSet(viewsets.ModelViewSet):
    queryset = AuthorizationType.objects.all()
    serializer_class = AuthorizationTypeSerializer

class AccessAuthorizationViewSet(viewsets.ModelViewSet):
    queryset = AccessAuthorization.objects.all()
    serializer_class = AccessAuthorizationSerializer

class AccessStatusViewSet(viewsets.ModelViewSet):
    queryset = AccessStatus.objects.all()
    serializer_class = AccessStatusSerializer

class AccessHistoryViewSet(viewsets.ModelViewSet):
    queryset = AccessHistory.objects.all()
    serializer_class = AccessHistorySerializer