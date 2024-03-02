from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature

# Create your views here.
# def index(request):
#     greet = 'Asslamulaikum Everyone!'
#     context = {
#         'greet': greet,      
#     }
    
#     return render(request,'mob/index.html', context)

def index(request): 
    feature1 = Feature()
    feature1.id = 1
    feature1.name = 'Trust'
    feature1.details = 'We are a trusted brand in the market for 10 years now.'
    feature1.is_active = True
    
    feature2 = Feature()
    feature2.id = 1
    feature2.name = 'Quality'
    feature2.details = 'We provide the best quality products in the market at the best price.'
    feature2.is_active = True
    
    feature3 = Feature()
    feature3.id = 1
    feature3.name = 'Fast Delivery'
    feature3.details = 'We deliver the products within 24 hours of order placement'
    feature3.is_active = True

    features = [feature1, feature2, feature3]
    return render(request,'mob/index.html', {'features': features})


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