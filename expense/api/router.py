from rest_framework.routers import DefaultRouter
from expense.api.views import ExpenseApiViewSet, get_expense_by_budget, get_expense_by_category

from django.urls import path, re_path
from django.conf.urls import include


router_expense = DefaultRouter()

router_expense.register(prefix='expense', basename='expense', viewset=ExpenseApiViewSet)

urlpatterns = [
    path('expense/budget/<int:budget_id>/', get_expense_by_budget),
    path('expense/category/<int:category_id>/', get_expense_by_category),
    re_path('', include(router_expense.urls))
]
