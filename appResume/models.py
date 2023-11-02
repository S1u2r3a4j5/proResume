from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=200)
    # created_at = models.DateTimeField(auto_now_add=True)