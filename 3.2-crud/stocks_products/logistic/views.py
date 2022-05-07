from django.core.paginator import Paginator
from rest_framework.viewsets import ModelViewSet

from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def get_queryset(self):
        title = self.request.GET.get('title', '')
        description = self.request.GET.get('description', '')
        queryset = Product.objects.all().filter(title__icontains=title, description__icontains=description)
        return queryset.order_by('id')


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all().prefetch_related('positions').prefetch_related('products').order_by('id')
    serializer_class = StockSerializer
    search_fields = ['positions__product__title']
    filter_fields = ['positions__product__id']

