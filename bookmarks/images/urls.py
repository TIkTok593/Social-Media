from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.image_create, name='create'),
    path('detail/<int:id>/<int:slug>/',
         views.image_detail, name='detail'),
    path('like/', views.image_like, name='like'),
    path('', views.image_list, name='list'),
]