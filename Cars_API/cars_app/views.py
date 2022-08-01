from rest_framework import generics
from .serializers import *
from rest_framework.permissions import IsAuthenticated


class OnSaleCarsAPIView(generics.ListAPIView):
    queryset = Cars.objects.filter(is_on_sale=True)
    serializer_class = CarsSerializer
    permission_classes = (IsAuthenticated, )


class AllCarsAPIView(generics.ListAPIView):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer
    permission_classes = (IsAuthenticated, )


class ModelsAPIView(generics.ListAPIView):
    queryset = Model.objects.all()
    serializer_class = ModelSerializer
    permission_classes = (IsAuthenticated, )


class BrandsAPIView(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = (IsAuthenticated, )
