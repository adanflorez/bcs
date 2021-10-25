from rest_framework.viewsets import ModelViewSet

from period.api.serializers import PeriodSerializer
from period.models import Period


class PeriodApiViewSet(ModelViewSet):
    serializer_class = PeriodSerializer
    queryset = Period.objects.all()
