from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

# Create a router and register our viewset with it.
router = DefaultRouter()
router.register(r'cars', CarViewSet)
router.register(r'brands', BrandViewSet)
router.register(r'resiUser', ResiUserViewSet)
router.register(r'city', CityViewSet)
router.register(r'country', CountryViewSet)
router.register(r'residentialDistrict', ResidentialDistrictViewSet)
router.register(r'user-roles', UserRoleViewSet)
router.register(r'authorization-statuses', AuthorizationStatusViewSet)
router.register(r'authorization-types', AuthorizationTypeViewSet)
router.register(r'access-authorizations', AccessAuthorizationViewSet)
router.register(r'access-statuses', AccessStatusViewSet)
router.register(r'access-history', AccessHistoryViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
