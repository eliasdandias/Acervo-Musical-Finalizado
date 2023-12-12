from django.shortcuts import render
from . models import*

# Create your views here.
def consulta (request):
    consultas ={
        'consultas':Musica.objects.all()
    }

    return render(request, 'consultas/consultas.html', consultas)



