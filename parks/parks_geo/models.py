from django.db import models

# What metadata should be added to the basic data?
# Think about relationship between parks and users, users and comments/reviews 


# Read parks geojson and pass into database

class Park(models.Model):
    name = models.CharField(max_length=128)
    feature = models.CharField(max_length=128, null=True)
    address = models.CharField(max_length=128, null=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    # comments = models.ForeignKey