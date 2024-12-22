from django.contrib import admin
from .models import CarMake, CarModel

# Register the CarMake and CarModel models with the Django admin site
admin.site.register(CarMake)
admin.site.register(CarModel)
