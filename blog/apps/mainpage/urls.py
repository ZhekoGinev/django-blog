from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="homepage"),
    path("about/", views.about, name="about"),
    path("contact/", views.about, name="contact"),
    path("articles/", views.about, name="articles"),
]
