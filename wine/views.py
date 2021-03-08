from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.reverse import reverse

from wine.models import Wine
from wine.serializers import WineSerializer
from rest_framework import mixins, permissions, viewsets
from rest_framework import generics
from basket.models import Basket


class WineViewSet(viewsets.ModelViewSet):
    queryset = Wine.objects.all()
    serializer_class = WineSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(detail=True)
    def add_to_cart(self, request, *args, **kwargs):
        wine = self.get_object()
        basket = Basket.objects.filter(user=request.user).get()
        basket.products.add(wine)
        return Response({'wine': reverse('wine-list', request=request)})
