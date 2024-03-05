from django.db import models

# Create your models here.
class Felino(models.Model):
  gender = models.CharField(max_length=200)
  portuguese_name = models.CharField(max_length=200)
  english_name = models.CharField(max_length=200)
  scientific_name = models.CharField(max_length=200)
  image_url = models.CharField(max_length=250)
  image_name = models.CharField(max_length=200)
  habitat = models.CharField(max_length=200)
  curiosities = models.TextField()
