from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('popular/', views.getPopularProduct),
    path('recommended/', views.getRecommendedProduct),
]
