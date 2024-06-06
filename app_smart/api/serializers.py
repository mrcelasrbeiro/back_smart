# Importando o models de usuário do Django
from django.contrib.auth.models import User
from ..models import (Sensor, 
TemperaturaData, 
UmidadeData, 
LuminosidadeData, 
ContadorData
)

# Definir como serializer
from rest_framework import serializers

# Classe responsável por criptografar a senha
from django.contrib.auth.hashers import make_password 

# Classe para usuários comuns
class UserSerializer(serializers.ModelSerializer):
  # Método para criptografar a senha no banco
  def create(self, validated_data):
    validated_data['password'] = make_password(validated_data['password'])
    return super().create(validated_data)
  
  # Metadados da classe
  class Meta:
    model = User # model utilizado
    fields = ['id', 'username', 'password', 'email'] # campos que quero do model
    extra_kwargs = {'password': {'write_only':True}} # definir que quando a API devolver informações não devolver a senha

# Classe de sensor
class SensorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Sensor
    # Pegar todos os campos
    fields = '__all__'

class TemperaturaDataSerializer(serializers.ModelSerializer):
  class Meta:
    model = TemperaturaData
    fields = '__all__'

class UmidadeDataSerializer(serializers.ModelSerializer):
  class Meta:
    model = UmidadeData
    fields = '__all__'

class LuminosidadeDataSerializer(serializers.ModelSerializer):
  class Meta:
    model = LuminosidadeData
    fields = '__all__'

class ContadorDataSerializer(serializers.ModelSerializer):
  class Meta:
    model = ContadorData
    fields = '__all__'
