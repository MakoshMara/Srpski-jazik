from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

def index(request):
    text = 'Приветы'
    return render(request, 'mainapp/index.html',
                      context={
                          'text': 'text',
                      },
                      )