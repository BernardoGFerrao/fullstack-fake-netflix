from .models import Filme

def lista_filmes_recentes(request):
    lista_filmes = Filme.objects.all().order_by('-data_de_criacao')[0:8]#- Decrescente
    return {"lista_filmes_recentes": lista_filmes}

def lista_filmes_alta(request):
    lista_filmes = Filme.objects.all().order_by('-visualizacoes')[0:8]#- Decrescente
    return {"lista_filmes_alta": lista_filmes}

def filme_destaque(request):
    if Filme.objects.all().count() == 0:
        return {"filme_destaque": None}
    else:
        filme = Filme.objects.order_by('-data_de_criacao')[0]#- Decrescente
        return {"filme_destaque": filme}