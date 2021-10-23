from rest_framework import serializers

from expense.models import Expense


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ['subject', 'description', 'amount', 'category', 'budget_date']