from django.urls import path

from pwdj.galeria import views

app_name = 'galeria'
urlpatterns = [
    path('', views.index, name='index'),
]
