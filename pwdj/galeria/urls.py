from django.urls import path

from pwdj.galeria import views

app_name = 'galeria'
urlpatterns = [
    path('', views.index, name='index'),
    path('novo', views.new, name='new'),
    path('criar', views.create, name='create'),
]
