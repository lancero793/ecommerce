from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("details/<int:id>", views.details, name="details"),
    path("privacy/", views.privacy, name="privacy"),
    path("terminos/", views.terminos, name="terminos"),
    path("ayuda/", views.ayuda, name="ayuda"),
    path("contactenos/", views.contact, name="contact"),
    path("load/", views.load, name="load"),
    ]