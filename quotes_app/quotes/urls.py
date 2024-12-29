from django.urls import path

from . import views

app_name = "quotes"
urlpatterns = [
    path("", views.main, name="main"),
    path("<int:page>", views.main, name="root_paginate"),
    path("author/<int:author_id>", views.author_detail, name="author_detail"),
    path("tag/<int:tag_id>", views.tag, name="tag"),
    path("adding_tag", views.add_tag, name="tag_input"),
    path("adding_author", views.add_author, name="author_input"),
    path("adding_quote", views.add_quote, name="quote_input"),
]
