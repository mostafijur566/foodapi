from django.contrib import admin
from .models import PopularProduct, RecommendedProduct

# Register your models here.

admin.site.register(PopularProduct)
admin.site.register(RecommendedProduct)
