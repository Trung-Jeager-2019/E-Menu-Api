from django.db import models

class MenuItem(models.Model):
    category = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    image = models.CharField(max_length=2048)
    decribe = models.CharField(max_length=4096)

    def __str__(self):
        return self.category + " - " + self.name