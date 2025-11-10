from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('about/mission/', views.mission_view, name='mission'),
    path('contact/', views.contact, name='contact'),
]
