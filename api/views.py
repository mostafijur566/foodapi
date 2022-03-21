from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PopularProductSerializer, RecommendedProductSerializer
from .models import PopularProduct, RecommendedProduct


# Create your views here.

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'name': 'Test',
            'desc': 'This is test'
        }
    ]

    return Response(routes)


@api_view(['GET'])
def getPopularProduct(request):
    products = PopularProduct.objects.all()
    serializer = PopularProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getRecommendedProduct(request):
    products = RecommendedProduct.objects.all()
    serializer = RecommendedProductSerializer(products, many=True)
    return Response(serializer.data)
