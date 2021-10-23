from django.db import models
from django.db.models import SET_NULL

from budget.models import Budget


class Expense(models.Model):
    subject = models.CharField(max_length=255)
    description = models.TextField()
    amount = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    budget = models.ForeignKey(Budget, on_delete=SET_NULL, null=True)

    def __str__(self):
        return self.subject
