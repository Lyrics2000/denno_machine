from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request,'index.html')


def map_filter(request):
    return render(request,'map_page.html')