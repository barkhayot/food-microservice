from django.shortcuts import render
from django.http import JsonResponse
from . models import Deliver
# Create your views here.

def index(request):
    return render(request, 'index.html')

def get_data(request):
    data = []
    deliver = Deliver.objects.all()
    for i in deliver:
        val = {}
        val['id'] = i.id
        val['food']= i.food
        val['quantity']= i.quantity
        val['price'] = i.price
        val['status'] = i.status
        data.append(val)
    return JsonResponse(data, safe=False)