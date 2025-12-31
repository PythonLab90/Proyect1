from django.shortcuts import render
from pagp.models import Producto

# Create your views here.
def resultado(request):
    producto = Producto.objects.last()
    return render(request, 'resultado.html', {'producto': producto})
