from django.db.models import fields
from rest_framework import serializers
from inicio.models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'