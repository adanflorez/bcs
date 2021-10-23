from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from expense.api.serializers import ExpenseSerializer
from expense.models import Expense


@api_view(['GET'])
def get_expense_by_budget(request, budget_id):
    expenses = Expense.objects.filter(budget=budget_id, budget__category='4')
    serializer = ExpenseSerializer(expenses, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_expense_by_category(request, category_id):
    expenses = Expense.objects.filter(budget__category=category_id)
    serializer = ExpenseSerializer(expenses, many=True)
    return Response(serializer.data)


class ExpenseApiViewSet(ModelViewSet):
    serializer_class = ExpenseSerializer
    queryset = Expense.objects.all()
