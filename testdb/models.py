
import datetime


from django.db import models
from django.utils import timezone

# Create your models here.


class Bean(models.Model):
    

    name = models.CharField(max_length=20)

    countryOfProduction = models.CharField(max_length=30)

    def __str__(self):
        return self.name


    def was_published_recently(self):
        return self.pub_date>= timezone.now() - datetime.delta(days=1)
