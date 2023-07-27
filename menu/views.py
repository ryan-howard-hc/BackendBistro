from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import MenuItem
# Create your views here.
def index(request):
    return HttpResponse("skrrt")

def get_table(request):
    getit = list(MenuItem.objects.values())
    return JsonResponse({'data':getit})