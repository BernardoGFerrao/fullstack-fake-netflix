from django.shortcuts import render

# Create your views here.
def homepage(request):#Request -> Requisição(GET/POST)
    return render(request, 'homepage.html')
