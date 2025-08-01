from django.shortcuts import render,redirect
from .models import Register


def signin_page(request):
    return render(request,'sigin.html')

def index(request):
    return render(request,'index.html')

def register(request):
    if request.method == "POST":
        username  = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if Register.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': 'Username already exists'})
        else:
            user = Register(username=username, email=email, password=password)
            user.save()
            return redirect('sigin_page')
    return render(request, 'register.html')

def signin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            Register.objects.get(username=username, password=password)
            return redirect('index')  # Assuming you have an index view to redirect to
        except Register.DoesNotExist:
            return render(request, 'sigin.html', {'error': 'Invalid credentials'})
    return render(request, 'sigin.html')