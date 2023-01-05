from django.shortcuts import render, get_object_or_404
from . models import Food
import json 
import kafka
from kafka import KafkaProducer

# Create your views here.
ORDER_KAFKA_TOPIC = "order_details"
producer = KafkaProducer(bootstrap_servers="localhost:29092")

def GetFoods(request):
    foods = Food.objects.all()
    # if request.method == 'POST':
    #     for i in foods:
    #         data = {
    #             "food_name" : foods.name,
    #             "quantity" 
    #         }
    context = {
        'foods':foods
    }
    return render(request, 'list.html', context)

def DetailFood(request, pk):
    food = get_object_or_404(Food, pk=pk)
    if request.method == 'POST':
        quantity = request.POST.get('quantity')
        data = {
            "food_name": food.name,
            "quantity": quantity,
            "price":food.price
        }
        print("Data has been sent to Kafka\n")
        print(data)
        producer.send(ORDER_KAFKA_TOPIC, json.dumps(data).encode("utf-8"))
    context = {
        'food':food
    }
    return render(request, 'detail.html', context)