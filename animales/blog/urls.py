from django.urls import path
from . import views

urlpatterns= [
    path('', views.blogs, name='blogs'),
    path('animales/',views.animale, name='animale'),
    path('protectoras/',views.protectora, name='protectora'),
    path('colaboradores/',views.colaboradore, name='colaboradore'),
]