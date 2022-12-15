from django.db import models

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=40)

    def __str__(self):
        return self.name