from django.core.management.base import BaseCommand, CommandError

from cars_app.models import *
import random


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('count', nargs='+', type=int)

    @staticmethod
    def post_brand():
        brand_name = ['Audi', 'BMW', 'Mercedes', 'Skoda', 'Ford', 'Lexus']
        brand_headquarters = ['Germany', 'Poland', 'USA', 'Japan', 'South Korea']
        brand = {
            'name': random.choice(brand_name),
            'headquarters_country': random.choice(brand_headquarters)
        }
        Brand.objects.create(**brand)

    @staticmethod
    def post_model():
        model_name = ['a6', 'x4', 'a8', 'x5', 'E 200', 'Sierra', 'Golf', 'S 600']
        model_year_of_issue = [str(yoi) for yoi in range(2000, 2022)]
        model_body_style = ['sedan', 'hatchback', 'liftback', 'coupe', 'crossover', 'truck', 'wagon']
        model = {
            'name': random.choice(model_name),
            'year_of_issue': random.choice(model_year_of_issue),
            'body_style': random.choice(model_body_style)
        }
        Model.objects.create(**model)

    @staticmethod
    def post_car(_pk):
        colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
        fuel_types = ['gas', 'diesel']
        transmission_types = ['auto', 'manual']
        car = {
            'brand_name': Brand.objects.get(pk=_pk),
            'model_name': Model.objects.get(pk=_pk),
            'price': random.randint(20, 100) * 1000,
            'mileage': random.randint(10, 250) * 100,
            'exterior_color': random.choice(colors),
            'interior_color': random.choice(colors),
            'fuel_type': random.choice(fuel_types),
            'transmission_type': random.choice(transmission_types),
            'engine_volume': random.randint(14, 55) / 10,
            'is_on_sale': random.randint(0, 1),
        }
        Cars.objects.create(**car)

    def handle(self, *args, **options):
        count = options['count'][0]
        for i in range(count+1):

            self.post_brand()
            self.post_model()
            self.post_car(i+1)

        self.stdout.write(f'{count} of objects have been created')
