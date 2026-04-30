from django.contrib import admin
from .models import Message, Article

admin.site.register(Message)
admin.site.register(Article)