from django.shortcuts import render,redirect
from .models import Register


def signin_page(request):
    return render(request,'sigin.html')

def index(request):
    username = request.session.get('username')
    return render(request,'index.html',{'username':username})

def register(request):
    if request.method == "POST":
        username  = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if Register.objects.filter(email=email).exists():
            return render(request, 'register.html', {'error': 'Email already exists',})
        else:
            user = Register(username=username, email=email, password=password)
            user.save()
            request.session['username'] = username
            return redirect('index')
    return render(request, 'register.html')

def signin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if Register.objects.filter(username=username, password=password).exists():
            return render(request,'page.html')
        else:
            return render(request, 'sigin.html', {'error': 'Invalid username or password'})
    return render(request, 'sigin.html')