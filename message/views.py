from django.shortcuts import render

def message_view(request):
    return render(request, 'home.html')
