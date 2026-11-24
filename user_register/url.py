
from django.urls import path
from user_register import views

urlpatterns = [
    path('user_register/', views.user_register),
    path('view/', views.view_user_register),
    path('delete/(?P<idd>\w+)',views.delete),
    path('reject/(?P<idd>\w+)',views.reject),
    path('uuuu/',views.user.as_view()),
    path('profile/',views.view_profile.as_view())
]
