from django.db import models


class Text(models.Model):
    text = models.TextField()
    image = models.ImageField()