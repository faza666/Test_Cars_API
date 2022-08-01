from django.urls import path
from .views import *

urlpatterns = [
    path('create/', RegisterView.as_view()),        # path('user/create', ),  # POST create new user
]
