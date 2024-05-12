from django.db import models


class Editorial(models.Model):
    name = models.CharField(max_length=250)
    site = models.URLField()
    