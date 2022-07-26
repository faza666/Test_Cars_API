from django.urls import path

urlpatterns = [
    path('user/create', ),  # POST create new user
    path('user/login', ),   # POST login user

    path('cars/', ),        # GET list of all Car Objects that are on sale
    path('cars/all/', ),    # GET list of all Car Objects
    path('models/', ),      # GET list of all Model Objects
    path('brands/', )       # GET list of all Brand Objects
]
