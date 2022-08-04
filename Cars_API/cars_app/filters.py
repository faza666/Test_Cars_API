from django_filters import rest_framework as filters
from cars_app.models import Car, Model, Brand


class CarFilter(filters.FilterSet):
    price = filters.RangeFilter()
    mileage = filters.RangeFilter()
    exterior_color = filters.CharFilter()
    interior_color = filters.CharFilter()
    fuel_type = filters.CharFilter()
    transmission_type = filters.CharFilter()
    engine_volume = filters.RangeFilter()
    is_on_sale = filters.BooleanFilter()

    class Meta:
        model = Car
        fields = '__all__'


class ModelFilter(filters.FilterSet):
    name = filters.CharFilter()
    year_of_issue = filters.RangeFilter()
    body_style = filters.CharFilter()

    class Meta:
        model = Model
        fields = '__all__'


class BrandFilter(filters.FilterSet):
    name = filters.CharFilter()
    headquarters_country = filters.CharFilter()

    class Meta:
        model = Brand
        fields = '__all__'
