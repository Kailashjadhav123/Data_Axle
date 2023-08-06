from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('send_mail/', views.schedule_mail, name='send_mail'),
]