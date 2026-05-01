from django.urls import path
from .views import MessageView, ArticleView

urlpatterns = [
    path('', MessageView.as_view(), name='message'),
    path('article/', ArticleView.as_view(), name='article')
]