from rest_framework import serializers
from .models import Car, Model, Brand


class CarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"


class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = "__all__"


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"
