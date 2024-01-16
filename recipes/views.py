from django.shortcuts import render
from django.http import HttpResponse

def my_view(request):
    return HttpResponse("Aqui temos receitas incríveis!!!")
def main_page(request):
    return render(request, 'recipes/home.html')

