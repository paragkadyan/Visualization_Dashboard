from django.db import models

class Data(models.Model):
    intensity = models.IntegerField()
    likelihood = models.IntegerField()
    relevance = models.IntegerField()
    year = models.IntegerField()
    country = models.CharField(max_length=100)
    topics = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.country
