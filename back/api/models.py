from django.db import models

# Create your models here.

class Orders(models.Model):
    lights = models.CharField(max_length=9, default=000000000)
    cover = models.BooleanField(default=False)
    irrigate = models.BooleanField(default=False)
    irrigate_since = models.DateTimeField(auto_now=True)

    def serialise(self):
        return {
            'lights': self.lights,
            'cover': self.cover,
            'irrigate': self.irrigate,
            'irrigate_since': self.irrigate_since
            }


class Telemetry(models.Model):
    ground_humidity = models.IntegerField(default=0)
    air_humidity = models.IntegerField(default=0)
    air_temperature = models.IntegerField(default=-1)
    ambient_light = models.IntegerField(default=0)
    lights = models.CharField(max_length=9, default=000000000)
    cover = models.BooleanField(default=False)
    irrigate = models.BooleanField(default=False)
