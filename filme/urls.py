from django.urls import path, include
from .views import Homepage, Homefilmes, DetalhesFilme, PesquisaFilme

app_name = 'filme'

urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),
    path('filmes/', Homefilmes.as_view(), name='homefilmes'),
    path('filmes/<int:pk>', DetalhesFilme.as_view(), name='detalhesfilme'), #<int pk> -> primary key inteira do modelo passada nas views
    path('pesquisa/', PesquisaFilme.as_view(), name='pesquisafilme'),
]
