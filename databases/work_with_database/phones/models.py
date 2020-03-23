from django.db import models

MAX_NAME = 64

class Phone(models.Model):

   # id = models.IntegerField(primary_key=true)

    name = models.CharField(max_length=MAX_NAME)

    price = models.FloatField()

    image = models.TextField()

    release_date = models.DateField()

    lte_exists = models.BooleanField()

    slug = models.SlugField(name)

