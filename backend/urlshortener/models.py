from django.db import models


class Shortener(models.Model):
    long_url = models.URLField(max_length=200)


class PurgeRecord(models.Model):
    marked = models.OneToOneField("Shortener", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
