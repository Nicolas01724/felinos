from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect, QueryDict
from django.views import generic
from django.urls import reverse

from .models import Felino

def IndexView(request):
  felines = Felino.objects.order_by("-portuguese_name")[:5]
  context = {
    "felines": felines
  }

  return render(request, "app/index.html", context)

def DetailView(request, id):
  try:
    feline = Felino.objects.get(pk=id)
  except Felino.DoesNotExist:
    raise Http404("Esse felino não existe aqui 😶")
  return render(request, "app/detail.html", {"feline": feline})

def CreateView(request):
  return render(request, "app/create.html")

def criar(request):
  body = QueryDict(request.body)
  
  print(body)

  felino = Felino(
    gender=body.get("gender"),
    portuguese_name=body.get("portuguese_name"),
    english_name=body.get("english_name"),
    scientific_name=body.get("scientific_name"),
    image_url=body.get("image_url"),
    image_name=body.get("image_url"),
    habitat=body.get("habitat"),
    curiosities=body.get("curiosities"),
    
  )

  felino.asave()
  # felino.save()
  

  return HttpResponseRedirect('/')