from django.db import models
from django.utils import timezone

# Create your models here.


class BoastsRoasts(models.Model):
    boolean = models.BooleanField()
    body = models.CharField(max_length=280)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    datetime = models.DateTimeField(default=timezone.now)
    score = models.IntegerField(default=0)

    def __str__(self):
        if self.boolean:
            return "Boast"
        return "Roast"
