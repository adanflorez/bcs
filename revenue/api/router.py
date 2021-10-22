from rest_framework.routers import DefaultRouter
from revenue.api.views import RevenueViewSet


router_revenue = DefaultRouter()

router_revenue.register(prefix='revenue', basename='revenue', viewset=RevenueViewSet)
