from django.db import models
from django.utils import timezone
# Create your models here. Tabelas.

LISTA_CATEGORIAS = (
    #(como ficar armazenado no bd, como aparece para escolher),
    ("ANALISES", "Análises"),
    ("PROGRAMACAO", "Programação"),
    ("APRESENTACAO", "Apresentação"),
    ("OUTROS", "Outros"),
)

#Criar o filme
class Filme(models.Model): #Model -> Padrão Django
    titulo = models.CharField(max_length=100)
    thumb = models.ImageField(upload_to="thumb_filmes") #Nome da pasta onde fica armazenada as thumbs
    descricao = models.TextField(max_length=1000)
    categoria = models.CharField(max_length=15, choices=LISTA_CATEGORIAS)
    visualizacoes = models.IntegerField(default=0)
    data_de_criacao = models.DateTimeField(default=timezone.now)



#Criar os episódios
