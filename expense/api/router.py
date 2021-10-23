from rest_framework.routers import DefaultRouter
from expense.api.views import ExpenseApiViewSet


router_expense = DefaultRouter()

router_expense.register(prefix='expense', basename='expense', viewset=ExpenseApiViewSet)