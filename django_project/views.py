import requests
from django.http import response
from django.shortcuts import render

def home(request):
#USING APIS
  response = requests.get(' https://v6.exchangerate-api.com/v6/dac76accd7f2c8dfa2d7e9a1/latest/USD')
  data = response.json()
  result = data['conversion_rates']
  
  return render(request, 'templates/index.html', {'result': result})