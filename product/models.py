from django.db import models

# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField(null=True)
    link = models.TextField()
    description = models.TextField()
    def __str__(self):
        return self.name