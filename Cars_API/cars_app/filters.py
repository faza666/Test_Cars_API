from django_filters import rest_framework as filters
from cars_app.models import Car, Model, Brand


class CarFilter(filters.FilterSet):
    brand_name = filters.CharFilter(field_name='brand_name__name', lookup_expr='icontains')
    model_name = filters.CharFilter(field_name='model_name__name', lookup_expr='icontains')
    price = filters.RangeFilter()
    mileage = filters.RangeFilter()
    engine_volume = filters.RangeFilter()
    is_on_sale = filters.BooleanFilter()

    class Meta:
        model = Car
        fields = '__all__'


class ModelFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')
    body_style = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Model
        fields = '__all__'


class BrandFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')
    headquarters_country = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Brand
        fields = '__all__'
