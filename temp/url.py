from django.urls import path, include
from temp import views

urlpatterns=[
    path('home/',views.home),
    path('user/',views.user),
    path('technician/',views.technician),
    path('admin/',views.admin),
    path('upload/',views.upload),

]