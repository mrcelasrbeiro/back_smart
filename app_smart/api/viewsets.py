# Model padrão do Django para usuários
from django.contrib.auth.models import User

from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status # resultado http

from app_smart.api import serializers
from ..models import (Sensor, 
TemperaturaData, 
UmidadeData, 
ContadorData, 
LuminosidadeData)
from rest_framework import viewsets

from .filters import SensorFilter, TemperaturaDataFilter
from django_filters.rest_framework import DjangoFilterBackend

class CreaterUserAPIViewSet(generics.CreateAPIView):
  queryset = User.objects.all() # trazer todos os dados
  
  # Classe responsável por formatar o retorno dos dados
  serializer_class = serializers.UserSerializer

  # Só irá acessar essa API os superusers
  permission_classes = [permissions.IsAdminUser] 

  # Postar novo usuário
  def post(self, request, *args, **kwargs):
    return self.create(request, *args, **kwargs) # criar na base de dados

class SensorViewSet(viewsets.ModelViewSet):
  queryset = Sensor.objects.all()
  serializer_class = serializers.SensorSerializer

  # Terá que ser autenticado para poder acessar
  permission_classes = [permissions.IsAuthenticated]

  # Aplicar os filtros definidos
  filter_backends = [DjangoFilterBackend]
  filterset_class = SensorFilter


class TemperaturaDataViewSet(viewsets.ModelViewSet):
  queryset = TemperaturaData.objects.all()
  serializer_class = serializers.TemperaturaDataSerializer
  permission_classes = [permissions.IsAuthenticated]

  #Usados no método get
  filter_backends = [DjangoFilterBackend]
  filter_class = TemperaturaDataFilter

class UmidadeDataViewSet(viewsets.ModelViewSet):
  queryset = UmidadeData.objects.all()
  serializer_class = serializers.UmidadeDataSerializer
  permission_classes = [permissions.IsAuthenticated]

class LuminosidadeDataViewSet(viewsets.ModelViewSet):
  queryset = LuminosidadeData.objects.all()
  serializer_class = serializers.LuminosidadeDataSerializer
  permission_classes = [permissions.IsAuthenticated]

class ContadorDataViewSet(viewsets.ModelViewSet):
  queryset = ContadorData.objects.all()
  serializer_class = serializers.ContadorDataSerializer
  permission_classes = [permissions.IsAuthenticated]

