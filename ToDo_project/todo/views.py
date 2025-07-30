from django.shortcuts import render
from .models import Register


def index(request):
    return render(request,'index.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        Register.objects.create(username=username,email=email,password=password)
    return render(request,'register.html',{'username':username, 'email':email, 'password':password})
