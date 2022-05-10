from django.urls import path, re_path

from . import views

urlpatterns = [
    path("", views.index, name="homepage"),
    path("about/", views.about, name="about"),
    path("articles/", views.articles, name="articles"),
    path("articles/<slug:slug>/", views.article_details, name="details"),
]
