from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("details/<int:id>", views.details, name="details"),
    path("load-news/", views.load_news, name="load-news"),
    path("load/", views.load, name="load"),
    path("pagar/", views.payment, name="pagar"),
    path("checkout/", views.checkout, name="checkout"),
    # Views isn't ajax functions
    path("privacy/", views.privacy_policy, name="privacy"),
    path("terminos/", views.terms, name="terminos"),
    path("ayuda/", views.helpme, name="ayuda"),
    path("contactenos/", views.contact, name="contact"),
    path("sobre-nosotros/", views.about, name="sobre-nosotros"),
    path("preguntas-frecuentes/", views.faqs, name="faqs"),
    ]