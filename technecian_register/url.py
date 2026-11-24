from django.urls import path
from technecian_register import views

urlpatterns = [
    path('technecian_register/', views.technecian_register),
    path('view/', views.view_technecian_register),
    path('accept/<str:idd>', views.accept),
    path('reject/<str:idd>', views.reject),
]