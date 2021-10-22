from django.db import models
from django.db.models import SET_NULL

from category.models import Category


class Expense(models.Model):
    subject = models.CharField(max_length=255)
    description = models.TextField()
    amount = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=SET_NULL, null=True)
    budget_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
