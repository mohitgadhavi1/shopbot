from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated

class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
