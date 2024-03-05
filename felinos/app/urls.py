from django.urls import path

from . import views

urlpatterns = [
  path("", views.IndexView, name="index"),
  path("felino/<int:id>/", views.DetailView, name="detail"),
  path("criar/", views.CreateView, name="create"),
  path("api/", views.criar, name="api"),
]