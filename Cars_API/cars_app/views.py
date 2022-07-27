from rest_framework import generics
from .serializers import *


class OnSaleCarsAPIView(generics.ListAPIView):
    queryset = Cars.objects.filter(is_on_sale=True)
    serializer_class = CarsSerializer


class AllCarsAPIView(generics.ListAPIView):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer


class ModelsAPIView(generics.ListAPIView):
    queryset = Model.objects.all()
    serializer_class = ModelSerializer


class BrandsAPIView(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
