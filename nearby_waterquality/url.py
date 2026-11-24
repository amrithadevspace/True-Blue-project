from django.urls import path
from nearby_waterquality import views

urlpatterns=[
    path('near/',views.add_nearby),
    path('vie_nr/',views.view),
    path('view/',views.view_admin),
    path('nnnn/',views.nearby.as_view()),
    path("qwer/",views.viewnearby.as_view()),

]