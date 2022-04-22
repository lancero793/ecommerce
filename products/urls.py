from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("details/<int:id>", views.details, name="details"),
    path("privacy/", views.privacy_policy, name="privacy"),
    path("terminos/", views.terms, name="terminos"),
    path("ayuda/", views.helpme, name="ayuda"),
    path("contactenos/", views.contact, name="contact"),
    path("checkout/", views.checkout, name="checkout"),
    path("sobre-nosotros/", views.about, name="sobre-nosotros"),
    path("pagar/", views.payment, name="pagar"),
    path("preguntas-frecuentes/", views.faqs, name="faqs"),
    path("load/", views.load, name="load"),
    ]