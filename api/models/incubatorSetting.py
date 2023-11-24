from django.db import models
from .user import CustomUser


class IncubatorSetting(models.Model):
    name = models.CharField(max_length=255)
    temperature = models.FloatField()
    humidity = models.FloatField()
    incubation_duration = models.DurationField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.name