from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('lest1/', views.lest1, name="lest1")
]