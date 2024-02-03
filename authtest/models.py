from django.db import models

class Coffee(models.Model):
    co_name = models.CharField(max_length=100)
    roast_level = models.CharField(max_length=50)
    acidity = models.CharField(max_length=50)
    com = models.CharField(max_length=100)
    three_letters = models.CharField(max_length=3)

    def __str__(self):
        return self.co_name
