from rest_framework import serializers

from revenue.models import Revenue


class RevenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Revenue
        fields = ['subject', 'amount', 'created_at', 'slug', 'budget_date']
