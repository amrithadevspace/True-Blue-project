from django.urls import path
from django.urls import path
from reading import views

urlpatterns=[
    path('near/',views.reading),
    path('upload/(?P<idd>\w+)',views.post),
    path('reading_api/', views.reading_api),
    path('reading_post_api/<int:idd>/', views.reading_post_api),
]