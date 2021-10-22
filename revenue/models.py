from django.db import models


class Revenue(models.Model):
    subject = models.CharField(max_length=255)
    amount = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255, unique=True)
    budget_date = models.DateField()

    def __str__(self):
        return self.subject
