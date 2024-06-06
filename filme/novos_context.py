from .models import Filme

def lista_filmes_recentes(request):
    lista_filmes = Filme.objects.all().order_by('-data_de_criacao')[0:10]#- Decrescente
    return {"lista_filmes_recentes": lista_filmes}

def lista_filmes_alta(request):
    lista_filmes = Filme.objects.all().order_by('-visualizacoes')[0:10]#- Decrescente
    return {"lista_filmes_alta": lista_filmes}