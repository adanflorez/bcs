from rest_framework.viewsets import ModelViewSet

from expense.api.serializers import ExpenseSerializer
from expense.models import Expense


class ExpenseApiViewSet(ModelViewSet):
    serializer_class = ExpenseSerializer
    queryset = Expense.objects.all()
