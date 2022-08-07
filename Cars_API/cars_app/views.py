from rest_framework import generics
from .serializers import *
from .filters import *
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend


class OnSaleCarsAPIView(generics.ListAPIView):
    queryset = Car.objects.filter(is_on_sale=True)
    serializer_class = CarsSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CarFilter


class AllCarsAPIView(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarsSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CarFilter


class ModelsAPIView(generics.ListAPIView):
    queryset = Model.objects.all()
    serializer_class = ModelSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ModelFilter


class BrandsAPIView(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = BrandFilter
