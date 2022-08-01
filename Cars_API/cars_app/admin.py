from django.contrib import admin
from .models import Car, Model, Brand

admin.site.register(Car)
admin.site.register(Brand)
admin.site.register(Model)
