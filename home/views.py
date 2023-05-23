from django.shortcuts import render
from django.views.generic import ListView
from home.models import Producto

# Create your views here.

class index(ListView):
    model = Producto
    template_name = 'home/index.html'

    def get_queryset(self):
        return self.model.objects.filter()