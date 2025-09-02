from django.shortcuts import render

# Create your views here.
def dashboard(request):
    return render(request, 'inventario/dashboard.html')

def productos(request):
    return render(request, 'inventario/productos.html')
