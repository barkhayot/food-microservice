from django.shortcuts import render, get_object_or_404, redirect
import json
from kafka import KafkaConsumer
from kafka import KafkaProducer
from django.http import JsonResponse
import time
from confluent_kafka import Consumer, KafkaError
from .models import Order

ORDER_KAFKA_TOPIC = "order_details"
DELIVER_KAFKA_TOPIC = "deliver_details"
producer = KafkaProducer(bootstrap_servers="localhost:29092")

#producer = KafkaProducer(bootstrap_servers="localhost:29092")
#consumer = KafkaConsumer(ORDER_KAFKA_TOPIC, bootstrap_servers="localhost:29092")

# # Create your views here.
# def check_kafka():
#     while True:
#         for message in consumer:
#             print("Ongoing transaction..")
#             consumed_message = json.loads(message.value.decode())
#             print(consumed_message)
#             food = consumed_message["food_name"]
#             quantity = consumed_message["quantity"]
#             price = consumed_message['price']
#             data = {
#                 "food": food,
#                 "quantity": quantity,
#                 "price": price
#             }
#             print("Successful transaction..")

# producer = KafkaProducer(bootstrap_servers="localhost:29092")
# consumer = KafkaConsumer(bootstrap_servers="localhost:29092", max_poll_records=10, session_timeout_ms=6000)
# consumer.subscribe(topics=ORDER_KAFKA_TOPIC)
    

# def consume_msg():
#         for message in consumer:
#             print("Ongoing transaction..")
#             consumed_message = json.loads(message.value.decode())
#             print(consumed_message)
#             food = consumed_message["food_name"]
#             quantity = consumed_message["quantity"]
#             price = consumed_message['price']
#             data = {
#                 "food": food,
#                 "quantity": quantity,
#                 "price": price
#             }
#             print("Successful transaction..------------------------")
#                 # yield [
#                 #     message.value['food_name'],
#                 #     message.value['quantity'],
#                 #     message.value['price'],
#                 #     1
#                 # ]

def store_order(request):
    
    # roducer = KafkaProducer(bootstrap_servers="localhost:29092")
    # consumer = KafkaConsumer(bootstrap_servers="localhost:29092", max_poll_records=10, session_timeout_ms=6000)
    # consumer.subscribe(topics=ORDER_KAFKA_TOPIC)


    # conf = {'bootstrap.servers': 'localhost:29092',
    #         'group.id': 'my-group',
    #         'auto.offset.reset': 'earliest'}
    # consumer = Consumer(conf)
    
    # # Subscribe to the desired Kafka topic
    # consumer.subscribe(['order_details'])

    # # Continuously poll for new messages
    # while True:
    #     msg = consumer.poll(1.0)
    #     if msg is None:
    #         continue
    #     if msg.error():
    #         if msg.error().code() == KafkaError._PARTITION_EOF:
    #             continue
    #         else:
    #             print(msg.error())
    #             break
    #     message = msg.value().decode()
    #     print(f'Received message: {message}')
       

    # # for message in consumer:
    # #         print("Ongoing transaction..")
    # #         consumed_message = json.loads(message.value.decode())
    # #         print(consumed_message)
    # #         food = consumed_message["food_name"]
    # #         quantity = consumed_message["quantity"]
    # #         price = consumed_message['price']
    # #         data = {
    # #             "food": food,
    # #             "quantity": quantity,
    # #             "price": price
    # #         }
    # #         print("Successful transaction..------------------------")
    
    return render(request, 'hah.html')
    #producer.send(ORDER_CONFIRMED_KAFKA_TOPIC, json.dumps(data).encode("utf-8"))


def check(request):

    orders = Order.objects.filter(status__isnull=True)
    data = []
    for i in orders:
        val = {}
        val['id'] = i.id
        val['food']= i.food
        val['quantity']= i.quantity
        val['price'] = i.price
        data.append(val)
    return JsonResponse(data, safe=False)

def detail(request, pk):
    
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        order.status = "DELIVERY"
        order.save()
        data = {
            "food_name": order.food,
            "quantity": order.quantity,
            "price":order.price,
            "status":order.status
        }
        print("Data has been sent to Kafka\n")
        print(data)
        producer.send(DELIVER_KAFKA_TOPIC, json.dumps(data).encode("utf-8"))
        return redirect('store')
    context = {
        "order":order
    }
    return render(request, 'detail.html', context)

# def kafka_view(request):
#     consumer = KafkaConsumer('order_details', bootstrap_servers=['localhost:29092'])
#     messages = []
#     counter = 0
#     for message in consumer:
#         consumed_message = json.loads(message.value.decode())
#         messages.append(message.value)
#         food = consumed_message["food_name"]
#         quantity = consumed_message["quantity"]
#         price = consumed_message['price']
#         Order.objects.create(
#             food=food,
#             quantity=quantity,
#             price=price
#         )
#         data = {
#                 "food": food,
#                 "quantity": quantity,
#                 "price": price
#             }
#         counter += 1
#         if counter == 1:
#             break
#     print(data)
#     return JsonResponse(data, safe=False)


