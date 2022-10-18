from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('shop/', views.shop, name='shop'),
    path('<int:pk>', views.NewsDatailView.as_view(), name='news_pro')
]