from django.contrib import admin
# 1. import
from .models import Product, Offer


# customize the admin, ProductAdmin inherit all the admin.ModelAdmin functions and methods.
class ProductAdmin(admin.ModelAdmin):
    # from models.py, we choose what contributes we want to display
    list_display = ('name', 'price', 'stock')

# create a new class for OfferAdmin, inherit from admin.ModelAdmin class
class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')


# 2. register and path new class,(a pair of it)
admin.site.register(Product, ProductAdmin)
admin.site.register(Offer, OfferAdmin)

