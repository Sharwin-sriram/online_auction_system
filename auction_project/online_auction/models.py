from django.db import models
import uuid

# Create your models here.

class Listings(models.Model):
    item_name = models.CharField(max_length=100)
    item_description = models.TextField()

    def __str__(self):
        return self.item_name