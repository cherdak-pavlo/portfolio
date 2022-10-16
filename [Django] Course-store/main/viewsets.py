from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import MenuItemSerializer
from .models import MenuItem


class MenuItemViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = MenuItem.objects.all()
        serializer = MenuItemSerializer(queryset, many=True)
        return Response(serializer.data)
