from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.title_page, name="title_page"),
    path("wiki", views.title_page, name="entry"),
    path("search", views.search, name="search"),
    path("add", views.add, name="add"),
    path("edit/<str:title>", views.edit, name="edit"),
    path("edit", views.edit, name="edit"),
    path("update", views.update, name="update"),
    path("random", views.random_title, name="random")    
]
