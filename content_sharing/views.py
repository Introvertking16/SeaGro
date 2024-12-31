from django.shortcuts import render

def index(request):
    return render(request, 'content_sharing/index.html')
