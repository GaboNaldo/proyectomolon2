from django.urls import path
from prueba import views


urlpatterns = [
    path('hola', views.hola, name='hola'),
]