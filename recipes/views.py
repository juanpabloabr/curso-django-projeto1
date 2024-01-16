from django.shortcuts import render
from django.http import HttpResponse

def my_view(request):
    return HttpResponse("VAI TOMAR NO CU PIRANHAAAAAAA...")

def main_page(request):
    return HttpResponse("Hola! Que tae")