from django.urls import path
from .views import *

urlpatterns = [
    path(
        "cars/", OnSaleCarsAPIView.as_view(), name="cars"
    ),  # GET list of all Car Objects that are on sale
    path(
        "cars/all/", AllCarsAPIView.as_view(), name="cars_all"
    ),  # GET list of all Car Objects
    path(
        "models/", ModelsAPIView.as_view(), name="models"
    ),  # GET list of all Model Objects
    path(
        "brands/", BrandsAPIView.as_view(), name="brands"
    ),  # GET list of all Brand Objects
]
