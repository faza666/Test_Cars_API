from django.contrib import admin
from .models import Cars, Model, Brand

admin.site.register(Cars)
admin.site.register(Brand)
admin.site.register(Model)
