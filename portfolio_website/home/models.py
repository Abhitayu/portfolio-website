from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length = 30)
    email = models.CharField(max_length = 40)
    desc = models.TextField()
    date = models.DateField()