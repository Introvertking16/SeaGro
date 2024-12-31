from django.shortcuts import render

# Define the home view
def home(request):
    return render(request, 'core/home.html')  # Home page

# Define the about view
def about(request):
    return render(request, 'core/about.html')  # About page

# Define the contact view
def contact(request):
    return render(request, 'core/contact.html')  # Contact page

# Define the job_board view
def job_board(request):
    return render(request, 'core/job_board.html')  # Job Board page

# Define the login view
def login(request):
    return render(request, 'core/login.html')  # login page

# Define the register view
def register(request):
    return render(request, 'core/register.html')  # register page