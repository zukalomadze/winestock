from django.db.models import Sum
from rest_framework import permissions, generics
from rest_framework.response import Response

from basket.models import Basket
from basket.serializers import BasketSerializer
from wine.models import Wine


class BasketDetail(generics.RetrieveAPIView):
    queryset = Basket.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = BasketSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        all_sum = Wine.objects.filter(baskets=instance).aggregate(Sum('price'))['price__sum']
        return Response({'sum': all_sum if all_sum else 0, 'products': serializer.data})
