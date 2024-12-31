from django.shortcuts import render

def index(request):
    return render(request, 'tech_news/index.html')
