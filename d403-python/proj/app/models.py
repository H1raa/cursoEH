from django.db import models

# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField(max_length = 255)
    idade = models.IntegerField()
