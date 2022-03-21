from rest_framework.serializers import ModelSerializer
from .models import PopularProduct, RecommendedProduct


class PopularProductSerializer(ModelSerializer):
    class Meta:
        model = PopularProduct
        fields = '__all__'


class RecommendedProductSerializer(ModelSerializer):
    class Meta:
        model = RecommendedProduct
        fields = '__all__'
