from rest_framework.routers import DefaultRouter

from period.api.views import PeriodApiViewSet


router_period = DefaultRouter()

router_period.register(prefix='period', basename='period', viewset=PeriodApiViewSet)