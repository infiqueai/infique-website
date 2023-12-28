from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('gallery/', views.gallery, name='gallery'),
    path('videogallery/', views.videogallery, name='videogallery'),
    path('contact/', views.contact, name='contact'),
    path('course1/', views.course1, name='course1'),
    path('course2/', views.course2, name='course2'),
    path('course3/', views.course3, name='course3'),
    
]
