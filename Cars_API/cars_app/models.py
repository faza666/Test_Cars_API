from django.db import models


# Create your models here.
class Car(models.Model):
    brand_name = models.ForeignKey('Brand', on_delete=models.PROTECT)
    model_name = models.ForeignKey('Model', on_delete=models.PROTECT)
    price = models.IntegerField()
    mileage = models.IntegerField()
    exterior_color = models.CharField(max_length=255)
    interior_color = models.CharField(max_length=255)
    fuel_type = models.CharField(max_length=50)
    transmission_type = models.CharField(max_length=50)
    engine_volume = models.FloatField()
    is_on_sale = models.BooleanField()

    def __str__(self):
        return f'{self.brand_name} {self.model_name}'

    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'


class Brand(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    headquarters_country = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'


class Model(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    year_of_issue = models.CharField(max_length=4)
    body_style = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Model'
        verbose_name_plural = 'Models'
