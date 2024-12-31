from django.shortcuts import render

def index(request):
    return render(request, 'job_board/index.html')


