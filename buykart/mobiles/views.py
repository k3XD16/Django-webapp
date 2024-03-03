from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Feature

# Create your views here.
# def index(request):
#     greet = 'Asslamulaikum Everyone!'
#     context = {
#         'greet': greet,      
#     }
    
#     return render(request,'mob/index.html', context)

def index(request): 
    features = Feature.objects.all()
    return render(request,'mob/index.html', {'features': features})

def register(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password == confirm_password:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email already exists")
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, "Username already exists")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,
                                                email=email,
                                                password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, "Password is not matching")
            return redirect('register')    
    else:
        return render(request,'register.html')


def login(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username,password=password)
        
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request, "Invalid credentials")
            return redirect('login')
    else:
        return render(request, 'login.html')


def pixel(request):
    context ={
        'brand': 'Google',
        'model': 'Pixel 8 Pro',
        'color': 'Bay',
        'processor': 'Tensor G3',
        'battery': '5000mAh',
        'display': 'OLED 120Hz 6.5 inch',
        'camera': '48MP + 13MP + 8MP',
        'ram': '8GB',
        'rom': '128GB',
        'price': 'Rs. 59,999',
    }
    return render(request, 'mob/pixel.html', context)

def counter(request):
    text = request.POST['text']
    totalwords = len(text.split())
    return render(request, 'mob/counter.html',{'amount': totalwords})