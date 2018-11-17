from django.db import models
from django.utils import timezone


class Bici(models.Model):
    codigo = models.CharField(primary_key=True,max_length=20)
    marca = models.CharField(max_length=20)
    annos_vida = models.IntegerField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.codigo
