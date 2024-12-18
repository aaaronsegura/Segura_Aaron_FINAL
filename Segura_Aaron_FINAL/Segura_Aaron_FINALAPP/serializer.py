from rest_framework import serializers
from .models import Inscrito, Institucion

# Serializador para Inscrito
class InscritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inscrito
        fields = '__all__'

# Serializador para Institución
class InstitucionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institucion
        fields = '__all__'
