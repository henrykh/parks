from django.db import models
import os

# What metadata should be added to the basic data?
# Think about relationship between parks and users, users and comments/reviews 


# Read parks geojson and pass into database
def initialize_parks():
    pass


class Park(models.Model):
    name = models.CharField(max_length=64)
    feature = models.CharField(max_length=64)
    address = models.CharField(max_length=64)
    latitude = models.FloatField()
    longitude = models.FloatField()
