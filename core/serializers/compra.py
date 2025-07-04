import email
from attr import fields
from cffi import model
from rest_framework.serializers import CharField, ModelSerializer

from core.models import Compra, ItensCompra

class CompraSerializer(ModelSerializer):
    usuario = CharField(source='usuario.email', read_only=True)
    status = CharField(source='get_status_display', read_only=True)
    class Meta:
        model = Compra
        fields = '__all__'
        depth= 2

class ItensCompra(ModelSerializer):
    model = ItensCompra
    fields = ('livro', 'quantidade')
    depth=2
