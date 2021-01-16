from django.shortcuts import render

# Third party import
from rest_framework import mixins, generics

from .serializers import MenuItemSerializers
from .models import MenuItem

# def Scraping(request):
#     # Scraping data form web "The Coffee House"

#     return ""

class ItemsView( mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    serializer_class = MenuItemSerializers
    queryset = MenuItem.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)