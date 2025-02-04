from django.urls import path
from . import views

app_name = "taxi"

urlpatterns = [
    path("", views.index, name="index"),
    path("manufacturers/", views.manufacturers_list, name="manufacturers"),

    path("cars/", views.cars_list, name="cars"),
    path("drivers/", views.drivers_list, name="drivers"),

]
