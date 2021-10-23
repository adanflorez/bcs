from rest_framework.routers import DefaultRouter
from expense.api.views import ExpenseApiViewSet, get_expense_by_budget

from django.urls import path, re_path
from django.conf.urls import include


router_expense = DefaultRouter()

router_expense.register(prefix='expense', basename='expense', viewset=ExpenseApiViewSet)

urlpatterns = [
    path('expense/budget/<int:budget_id>/', get_expense_by_budget),
    re_path('', include(router_expense.urls))
]
