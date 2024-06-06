from django.shortcuts import render
from filme.models import Filme
from .models import Filme
from django.views.generic import ListView, TemplateView, DetailView
# Create your views here.


# def homepage(request):#Request -> Requisição(GET/POST)
#     return render(request, 'homepage.html')

class Homepage(TemplateView):
    template_name = 'homepage.html'

# def homefilmes(request):
#     context = {}
#     lista_filmes = Filme.objects.all()
#     context['lista_filmes'] = lista_filmes
#     return render(request, 'homefilmes.html', context)
# #Context -> Dict python que é passado, que permita com que o html possa usar tags

class Homefilmes(ListView):
    template_name = 'homefilmes.html'
    model = Filme
    #object_list -> Lista de itens

class DetalhesFilme(DetailView): #Para cada filme aparecerá um detalhe diferente
    template_name = 'detalhesfilme.html'
    model = Filme
    #object_list -> Um item do nosso modelo