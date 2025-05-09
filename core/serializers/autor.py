from attr import fields
from pydantic import field_serializer
from rest_framework.serializers import ModelSerializer

from core.models import Autor


class AutorSerializer(ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'
