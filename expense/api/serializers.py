from rest_framework import serializers

from budget.api.serializers import BudgetSerializer
from expense.models import Expense


class ExpenseSerializer(serializers.ModelSerializer):
    budget = BudgetSerializer()

    class Meta:
        model = Expense
        fields = ['subject', 'description', 'amount', 'budget']
