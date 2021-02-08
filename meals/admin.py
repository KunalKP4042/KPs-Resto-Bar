from django.contrib import admin
from . models import Meals
from . models import Category

# Register your models here.

admin.site.register(Meals)
admin.site.register(Category)