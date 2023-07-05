from django.db import models


# Create your models here.
class ApiDNA(models.Model):
    dna_body = models.FileField()
    dna_parents = models.FileField()
    encoded = models.FileField()
