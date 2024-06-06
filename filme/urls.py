from django.urls import path, include
from .views import Homepage, Homefilmes, DetalhesFilme

urlpatterns = [
    path('', Homepage.as_view()),
    path('filmes/', Homefilmes.as_view()),
    path('filmes/<int:pk>', DetalhesFilme.as_view()), #<int pk> -> primary key inteira do modelo passada nas views
]
