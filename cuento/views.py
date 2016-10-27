from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Cuento
from .models import Capitulo

# Create your views here.
def show_main_cuentos(request):
	cuentos = Cuento.objects.order_by("title")
	return render(request, "cuento/main.html", {'cuentos':cuentos})

def show_cuento(request, pk):
	exist = get_object_or_404(Cuento, pk=pk) # su la id no existe
	titulo = Cuento.objects.get(pk=pk)
	capitulos = Capitulo.objects.filter(cuento=titulo).order_by('id')
	return render (request, "cuento/cuento.html", {'capitulos':capitulos, 'titulo': titulo })