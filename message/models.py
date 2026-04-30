from django.db import models

class Message(models.Model):
    test = models.CharField(max_length=255)    
    