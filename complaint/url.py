from django.urls import path
from complaint import views

urlpatterns = [
    path('complaint/',views.complaint),
    path('view/',views.view_complaint),
    path('view_admin/',views.view_complaint_admin),
    path('re/<str:idd>', views.replay),
    path('re_admin/<str:idd>', views.replay_admin),
    path('view_reply/', views.view_complaint_replay),
    path('cccc/',views.com.as_view()),
    path('vv/',views.viewwreply.as_view())
]