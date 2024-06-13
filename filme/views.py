from django.shortcuts import render, redirect, reverse
from .models import Filme, Usuario
from django.views.generic import ListView, TemplateView, DetailView, FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CriarContaForm, HomeForm
# Create your views here.


# def homepage(request):#Request -> Requisição(GET/POST)
#     return render(request, 'homepage.html')

class Homepage(FormView):
    template_name = 'homepage.html'
    form_class = HomeForm

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('filme:homefilmes')
        else:
            return super().get(request, *args, **kwargs)#Redireciona para a homepage

    def get_success_url(self):
        email = self.request.POST.get('email')
        usuario = Usuario.objects.filter(email=email)#Verifica se existe um usuário com o email
        if usuario:
            url = reverse('filme:login')  # Link

        else:
            url = reverse('filme:criarconta')  # Link
        return url

# def homefilmes(request):
#     context = {}
#     lista_filmes = Filme.objects.all()
#     context['lista_filmes'] = lista_filmes
#     return render(request, 'homefilmes.html', context)
# #Context -> Dict python que é passado, que permita com que o html possa usar tags

class Homefilmes(LoginRequiredMixin, ListView):
    template_name = 'homefilmes.html'
    model = Filme
    #object_list -> Lista de itens

class DetalhesFilme(LoginRequiredMixin, DetailView): #Para cada filme aparecerá um detalhe diferente
    template_name = 'detalhesfilme.html'
    model = Filme
    #object_list -> Um item do nosso modelo

    def get(self, request, *args, **kwargs):
        #Contibilizar uma visualização
        filme = self.get_object()
        filme.visualizacoes += 1
        filme.save()#Salva no banco de dados

        usuario = request.user
        usuario.filmes_vistos.add(filme)
        return super().get(request, *args, **kwargs)#Redireciona para a url


    def get_context_data(self, **kwargs):#Sobreescrever
        context = super(DetalhesFilme, self).get_context_data(**kwargs)#Garante que a função continue igual
        filmes_relacionados = Filme.objects.filter(categoria=self.get_object().categoria)[0:5]#Filtrar a tabela de filmes de acordo com a categoria
        context['filmes_relacionados'] = filmes_relacionados
        return context

class PesquisaFilme(ListView):
    template_name = 'pesquisa.html'
    model = Filme


    def get_queryset(self):
        termo_pesquisa = self.request.GET.get('query')
        if termo_pesquisa:
            object_list = Filme.objects.filter(titulo__icontains=termo_pesquisa)#Alterando a lista de filmes
            return object_list
        else:
            return None

class EditarPerfil(LoginRequiredMixin, UpdateView):
    template_name = 'editarperfil.html'
    model = Usuario
    fields = ['first_name', 'last_name', 'email']

    def get_success_url(self):
        return reverse('filme:homefilmes')

class CriarConta(FormView):
    template_name = 'criarconta.html'
    form_class = CriarContaForm

    def form_valid(self, form):
        form.save()#Salva o usuário no banco de dados
        return super().form_valid(form)

    def get_success_url(self):
        url = reverse('filme:login')#Link
        return url