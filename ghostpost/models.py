from django.db import models
from django.utils import timezone


class BoastsRoasts(models.Model):
    boolean = models.BooleanField()
    body = models.CharField(max_length=280)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    datetime = models.DateTimeField(default=timezone.now)
    score = models.IntegerField(default=0)
    secret_id = models.CharField(unique=True, max_length=10)

    def __str__(self):
        if self.boolean:
            return "Boast"
        return "Roast"
