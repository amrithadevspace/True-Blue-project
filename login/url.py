from django.urls import path
from login import views

urlpatterns = [
    path('login/', views.login),
    path('login_app/', views.login_app.as_view())
    # url('llll/',views.log.as_view())
]


