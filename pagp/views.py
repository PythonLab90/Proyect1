from django.shortcuts import render, redirect
from .forms import ProductoForm



# Create your views here.
def index(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('resultado')
    else:
        form = ProductoForm()
    return render(request, 'buscar.html', {'form': form})
    
