from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView
from .models import Message

# def messageView(request):
#     return render(request, 'home.html')

# class MessageView(View):    
#     def get(self, request):
#         return render(request, 'home.html')

# class MessageView(TemplateView):
#     template_name = 'home.html'

class MessageView(ListView):
    model = Message    
    template_name = 'home.html'