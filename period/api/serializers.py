from rest_framework import serializers

from period.models import Period


class PeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Period
        fields = ['title', 'description', 'start_date', 'end_date']
