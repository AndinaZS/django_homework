from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=10)
    description = models.CharField(max_length=50, blank=True)


class Measurement(models.Model):
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now=True)
    sensor = models.ForeignKey(Sensor, related_name='measurements', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', max_length=50, blank=True, null=True)