from django.core.paginator import Paginator
from rest_framework.viewsets import ModelViewSet

from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    search_fields = ['title', 'description']


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all().prefetch_related('positions').prefetch_related('products').order_by('id')
    serializer_class = StockSerializer

    def get_queryset(self):
        product = self.request.GET.get('product', '')
        queryset = Stock.objects.all().filter(positions__product__title__icontains=product)
        return queryset.order_by('id')