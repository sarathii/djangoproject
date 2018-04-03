from django.db import models


class Items(models.Model):
    iname=models.CharField(max_length=100)
    ipic = models.CharField(max_length=200)
    iprice = models.CharField(max_length=100)
    ides = models.CharField(max_length=900)


    def __str__(self):
        return self.iname +"  -rs" +self.iprice