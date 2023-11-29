from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('category/<slug:category_slug>', views.category_by_slug),
]