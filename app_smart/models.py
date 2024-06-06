from django.db import models

# Create your models here.
class Sensor(models.Model):

  # Lista de valores
  TIPO_SENSORES_CHOICES = [
    # _CHOICES: define o nome a ser gravado e nome a ser exibido
    ('Temperatura', 'Temperatura'),
    ('Umidade', 'Umidade'),
    ('Contador', 'Contador'),
    ('Luminosidade', 'Luminosidade'),
  ]

  # Escolher entre os tipos definidos
  tipo= models.CharField(max_length=50, choices=TIPO_SENSORES_CHOICES)
  # Endereço de rede da placa conectada no sensor
  mac_address = models.CharField(max_length=20, null=True)
  
  latitude = models.FloatField()
  longitude = models.FloatField()
  localizacao = models.CharField(max_length=100)
  responsavel = models.CharField(max_length=100)
  unidade_medida = models.CharField(max_length=20, blank=True, null=True)
  # Ligado ou não
  status_operacional = models.BooleanField(default=True)
  observacao = models.TextField(blank=True)

  # Campo a ser exibido no administrador
  def __str__(self):
    return f"{self.tipo} - {self.localizacao}"

class TemperaturaData(models.Model):
  sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
  valor = models.FloatField()
  # timestamp = models.DateTimeField(auto_now_add=True) # pegar a hora automatica do servidor
  timestamp = models.DateTimeField()

  def __str__(self):
    return f"Temperatura: {self.valor}°C - {self.timestamp}"

# contador luminosidade
class UmidadeData(models.Model):
  sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
  valor = models.FloatField()
  # timestamp = models.DateTimeField(auto_now_add=True)
  timestamp = models.DateTimeField()

  def __str__(self):
    return f"Umidade: {self.valor}% - {self.timestamp}"
  
class ContadorData(models.Model):
  sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
  # timestamp = models.DateTimeField(auto_now_add=True)
  timestamp = models.DateTimeField()

  def __str__(self):
    return f"Contagem: {self.timestamp}"

class LuminosidadeData(models.Model):
  sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
  valor = models.FloatField()
  # timestamp = models.DateTimeField(auto_now_add=True)
  timestamp = models.DateTimeField()
  
  def __str__(self):
    return f"Luminosidade: {self.valor} Lux - {self.timestamp}"