from django.db import models

# Create your models here. 
class User(models.Model):
    name = models.CharField(null = True, blank = True, max_length = 100)
    email = models.EmailField(null = False, unique = True)
    password = models.CharField(null = False, max_length = 128)
    images = models.ImageField(upload_to = 'images/')
    enhanced = models.ImageField(upload_to = 'enhanced/')
    def __str__(self):
        return self.name