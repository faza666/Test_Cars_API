from django.urls import path
from .views import *

urlpatterns = [
    path('user/create', ),  # POST create new user
    path('user/login', ),   # POST login user

    path('cars/', OnSaleCarsAPIView.as_view()),     # GET list of all Car Objects that are on sale
    path('cars/all/', AllCarsAPIView.as_view()),    # GET list of all Car Objects
    path('models/', ModelsAPIView.as_view()),       # GET list of all Model Objects
    path('brands/', BrandsAPIView.as_view()),       # GET list of all Brand Objects
]
