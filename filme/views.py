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

    def get(self, request, *args, **kwargs):
        #Contibilizar uma visualização
        filme = self.get_object()
        filme.visualizacoes += 1
        filme.save()#Salva no banco de dados
        return super().get(request, *args, **kwargs)#Redireciona para a url


    def get_context_data(self, **kwargs):#Sobreescrever
        context = super(DetalhesFilme, self).get_context_data(**kwargs)#Garante que a função continue igual
        filmes_relacionados = Filme.objects.filter(categoria=self.get_object().categoria)[0:5]#Filtrar a tabela de filmes de acordo com a categoria
        context['filmes_relacionados'] = filmes_relacionados
        return context
