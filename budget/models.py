from django.db import models
from django.db.models import SET_NULL, CASCADE

from category.models import Category
from period.models import Period


class Budget(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=SET_NULL, null=True)
    period = models.ForeignKey(Period, on_delete=CASCADE)

    def __str__(self):
        return self.title
