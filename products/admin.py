from django.contrib import admin
from .models import (
    Product,
    Color,
    Manufacturer,
    Category,
)



admin.site.register(Product)
admin.site.register(Color)
admin.site.register(Manufacturer)
admin.site.register(Category)