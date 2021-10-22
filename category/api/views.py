from rest_framework.viewsets import ModelViewSet

from category.api.permissions import IsAdminOrReadOnly
from category.models import Category
from category.api.serializers import CategorySerializer


class CategoryApiViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    lookup_field = 'slug'
