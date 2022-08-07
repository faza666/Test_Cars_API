from django.core.management.base import BaseCommand, CommandError
from cars_app.models import *
import random


class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def add_arguments(self, parser):
        parser.add_argument("count", nargs="+", type=int)

    @staticmethod
    def post_brand():

        brand_list = [
            ['Mercedes-Benz', 'Germany'],
            ['BMW', 'Germany'],
            ['Volvo', 'Sweden'],
            ['Audi', 'Sweden'],
            ['Porsche', 'Germany'],
            ['Lexus', 'Japan'],
            ['Lamborghini', 'Italy'],
            ['Ferrari', 'Italy'],
            ['Land Rover', 'United Kingdom'],
            ['Cadillac', 'United States'],
            ['Jaguar', 'United Kingdom'],
            ['Rolls-Royce', 'United Kingdom'],
            ['Bugatti', 'France'],
            ['Aston Martin', 'United Kingdom'],
        ]

        for each_item in brand_list:
            brand = {
                "name": each_item[0],
                "headquarters_country": each_item[1],
            }
            Brand.objects.create(**brand)

    @staticmethod
    def post_model(_number):
        model_name = ["a6", "x4", "a8", "x5", "E 200", "Sierra", "Golf", "S 600"]
        model_year_of_issue = [str(yoi) for yoi in range(2000, 2022)]
        model_body_style = [
            "sedan",
            "hatchback",
            "liftback",
            "coupe",
            "crossover",
            "truck",
            "wagon",
        ]
        for _ in range(_number):
            model = {
                "name": random.choice(model_name),
                "year_of_issue": random.choice(model_year_of_issue),
                "body_style": random.choice(model_body_style),
            }
            Model.objects.create(**model)

    @staticmethod
    def post_car(brand_list, model_list):

        colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
        fuel_types = ["gas", "diesel"]
        transmission_types = ["auto", "manual"]
        car = {
            "brand_name": random.choice(brand_list),
            "model_name": random.choice(model_list),
            "price": random.randint(20, 100) * 1000,
            "mileage": random.randint(10, 250) * 100,
            "exterior_color": random.choice(colors),
            "interior_color": random.choice(colors),
            "fuel_type": random.choice(fuel_types),
            "transmission_type": random.choice(transmission_types),
            "engine_volume": random.randint(14, 55) / 10,
            "is_on_sale": random.randint(0, 1),
        }
        Car.objects.create(**car)

    def handle(self, *args, **options):

        models_number = 20
        self.post_brand()
        self.post_model(models_number)

        brand_list = list(Brand.objects.all())
        model_list = list(Model.objects.all())

        count = options["count"][0]
        for _ in range(count):
            self.post_car(brand_list=brand_list, model_list=model_list)

        self.stdout.write(f"{count} of objects have been created")
