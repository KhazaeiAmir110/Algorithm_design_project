from django.db import models


# Create your models here.
class ApiDNA(models.Model):
    dna_body = models.FileField()
    dna_parents = models.FileField()
    encoded = models.FileField()


class Message(models.Model):
    sender = models.CharField(max_length=100)
    receiver = models.CharField(max_length=100)
    message = models.TextField()
    compressed_message = models.FileField(upload_to='compressed_messages/', null=True)