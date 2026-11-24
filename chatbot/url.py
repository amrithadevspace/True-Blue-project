from django.urls import path, include
from chatbot import views

urlpatterns = [
    path('bot/',views.chatbot),
    path('bot_tech/',views.chatbot_tech),
]