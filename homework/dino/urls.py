from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('int<post_id>', views.post, name='post'),
    path("group/<slug:slug>/", views.posts_group, name="posts_group"),
]
