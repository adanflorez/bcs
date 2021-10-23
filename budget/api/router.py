from rest_framework.routers import DefaultRouter

from budget.api.views import BudgetApiViewSet


router_budget = DefaultRouter()

router_budget.register(prefix='budget', basename='budget', viewset=BudgetApiViewSet)