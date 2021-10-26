from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from budget.api.serializers import BudgetSerializer
from budget.models import Budget
from revenue.models import Revenue


class BudgetApiViewSet(ModelViewSet):
    serializer_class = BudgetSerializer
    queryset = Budget.objects.all()

    def create(self, request):
        budgets = Budget.objects.filter(period=request.data['period'])
        budget_total_amount = int(request.data['amount'])
        for budget in budgets:
            budget_total_amount += budget.amount

        revenues = Revenue.objects.filter(period=request.data['period'])
        revenues_total_amount = 0
        for revenue in revenues:
            revenues_total_amount += revenue.amount

        serializer = BudgetSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True) and budget_total_amount <= revenues_total_amount:
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data='El presupuesto supera los ingresos')
