from attr import fields
from pydantic import field_serializer
from rest_framework.serializers import ModelSerializer

from core.models import autor


class AutorSerializer(ModelSerializer):
    class Meta:
        model = autor
        fields = '__all__'
        depth = 1