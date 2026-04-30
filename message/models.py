from django.db import models

class Message(models.Model):
    text = models.CharField(max_length=255)
    
    def __str__(self):
        return self.text
    
class Article(models.Model):
    title = models.CharField(max_length=255, null=False)
    article = models.TextField(max_length=2047)
    
    def __str__(self):
        return self.title