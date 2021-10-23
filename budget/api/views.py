from rest_framework.viewsets import ModelViewSet
from budget.models import Budget
from budget.api.serializers import BudgetSerializer


class BudgetApiViewSet(ModelViewSet):
    serializer_class = BudgetSerializer
    queryset = Budget.objects.all()
