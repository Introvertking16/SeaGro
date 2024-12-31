from django.shortcuts import render

def index(request):
    return render(request, 'bike_sharing/index.html')
