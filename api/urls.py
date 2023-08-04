from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name = "routes"),
    path('info/', views.getInfo, name = "confirm"),
    path('enhanced/<str:username>/', views.getImage, name = 'enhanced'),
    path('upload/', views.upload_image, name = "upload"),
]