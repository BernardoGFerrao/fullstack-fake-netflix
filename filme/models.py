from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
# Create your models here. Tabelas.

LISTA_CATEGORIAS = (
    #(como ficar armazenado no bd, como aparece para escolher),
    ("AÇÃO", "Ação"),
    ("TERROR", "Terror"),
    ("DOCUMENTARIOS", "Documentarios"),
    ("ROMANCE", "Romance"),
    ("COMÉDIA", "Comédia"),
    ("FANTASIA", "Fantasia"),
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

    def __str__(self):
        return self.titulo

#Criar os episódios
class Episodio(models.Model):
    filme = models.ForeignKey('Filme', related_name='episodios', on_delete=models.CASCADE)#Um para muitos, Um filme por episódio ... Vários episódios por filme
    titulo = models.CharField(max_length=100)
    video = models.URLField()

    def __str__(self):
        return self.filme.titulo + " " +self.titulo

class Usuario(AbstractUser):
    filmes_vistos = models.ManyToManyField('Filme', related_name='usuarios', blank=True)
