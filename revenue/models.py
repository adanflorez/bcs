from django.db import models
from django.db.models import CASCADE

from period.models import Period


class Revenue(models.Model):
    subject = models.CharField(max_length=255)
    amount = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255, unique=True)
    period = models.ForeignKey(Period, on_delete=CASCADE)

    def __str__(self):
        return self.subject
