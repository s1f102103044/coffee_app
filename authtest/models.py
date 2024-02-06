from django.db import models

class Coffee(models.Model):
    co_name = models.CharField(max_length=255)
    roast_level = models.CharField(max_length=255)
    acidity = models.CharField(max_length=255)
    com = models.CharField(max_length=255)
    three_letters = models.CharField(max_length=3)

    def __str__(self):
        return self.co_name