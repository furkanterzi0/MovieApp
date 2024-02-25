from django.db import models

class Category(models.Model):
    name= models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Movie(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.CharField(max_length=30)
    home = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name