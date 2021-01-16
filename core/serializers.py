from django.db.models import fields
from rest_framework import serializers

from .models import MenuItem

class MenuItemSerializers(serializers.ModelSerializer):
    class Meta():
        model = MenuItem
        fields = (
            'category',
            'name',
            'price',
            'image',
            'decribe'
        )