from django.db import models
from . import CustomUser, IncubatorSetting
import uuid
from django.utils import timezone

class IncubatorDevice(models.Model):
    unique_id = models.CharField(max_length=255, unique=True, primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    current_setting = models.ForeignKey(IncubatorSetting, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_devices')
    is_on = models.BooleanField(default=False)
    humidity_sensor = models.CharField(max_length=100)
    temperature_sensor = models.CharField(max_length=100)
    start_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Incubator Device"

    def turn_on(self):
        self.is_on = True
        self.start_time = timezone.now()
        self.save()

    def turn_off(self):
        self.is_on = False
        self.save()
