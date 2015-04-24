from django.db import models


#TODO: Move this out of project and into its own app ?
# What metadata should be added to the basic data?
# Think about relationship between parks and users, users and comments/reviews 


class Park(models.Model):
    name = models.CharField(max_length=64)
    feature = models.CharField(max_length=64)
    address = models.CharField(max_length=64)