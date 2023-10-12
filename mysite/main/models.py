from django.db import models

# Create your models here.

class Car(models.Model):

    model = models.CharField('Model', max_length=60)
    price = models.PositiveIntegerField('Price')

    def __str__(self):
        return self.model