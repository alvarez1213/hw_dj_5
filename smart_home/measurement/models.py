from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)

    class Meta:
        verbose_name = 'Сенсор'
        verbose_name_plural = 'Сенсоры'
        ordering = ['name']

    def __str__(self):
        return self.name

class Measurement(models.Model):
    sensor_id = models.ForeignKey(Sensor, related_name='measures', on_delete=models.CASCADE)
    temperature = models.DecimalField(max_digits=4, decimal_places=1)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(max_length=None, null=True)

    class Meta:
        verbose_name = 'Измерение'
        verbose_name_plural = 'Измерения'
        ordering = ['-created_at']

    # def __str__(self):
    #     return f'{self.sensor_id} - {self.temperature}'
