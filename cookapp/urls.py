
from django.contrib import admin
from django.urls import path,include

from .import views
urlpatterns = [
    path("",views.namei,name="namei"),
    path("surnamei",views.surnamei,name="surnamei"),
    path("cityi",views.cityi,name="cityi"),
    path("alli",views.alli,name="alli"),
]
