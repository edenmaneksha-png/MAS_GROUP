from django.db import models

class Admission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()