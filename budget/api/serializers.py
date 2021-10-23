from rest_framework import serializers
from budget.models import Budget


class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = ['title', 'start_date', 'end_date', 'amount', 'category']
