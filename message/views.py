from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

# def messageView(request):
#     return render(request, 'home.html')

# class MessageView(View):    
#     def get(self, request):
#         return render(request, 'home.html')

class MessageView(TemplateView):
    template_name = 'home.html'