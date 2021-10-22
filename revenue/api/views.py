from datetime import date

from rest_framework.viewsets import ModelViewSet

from revenue.api.serializers import RevenueSerializer
from revenue.api.permissions import IsAdminOrReadOnly
from revenue.models import Revenue


class RevenueViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = RevenueSerializer

    def get_queryset(self):
        try:
            today = date.today()
            if 'start_date' in self.request.query_params and 'end_date' in self.request.query_params:
                start_date = self.request.query_params['start_date']
                end_date = self.request.query_params['end_date']
                return Revenue.objects.filter(created_at__gte=start_date, created_at__lte=end_date)
            elif 'start_date' in self.request.query_params:
                start_date = self.request.query_params['start_date']
                end_date = today.strftime("%Y-%m-%d")
                return Revenue.objects.filter(created_at__gte=start_date, created_at__lte=end_date)
            elif 'end_date' in self.request.query_params:
                start_date = today.strftime("%Y-") + "01-01"
                end_date = self.request.query_params['end_date']
                return Revenue.objects.filter(created_at__gte=start_date, created_at__lte=end_date)

            return Revenue.objects.all()
        except Exception as e:
            print(e)
