from django.db import models


class Item(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    url = models.URLField(max_length=200, blank=True, null=True)
    text = models.CharField(max_length=1024, blank=True, null=True)

    def __str__(self):
        return self.text if self.text else "{} - {}".format(self.title, self.url)
