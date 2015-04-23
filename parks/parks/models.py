from django.db import models


class Park(models.Model):
    name = models.CharField(max_length=64)
    feature = models.CharField(max_length=64)
    address = models.CharField(max_length=64)