from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def abre_index(request):
  mensagem = 'Olá, bem-vindo(a)!'

  # Retornar uma mensagem
  return HttpResponse(mensagem)