from django.db import models


class Item(models.Model):
    url = models.URLField(max_length=200)
