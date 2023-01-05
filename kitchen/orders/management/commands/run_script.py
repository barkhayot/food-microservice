from django.core.management.base import BaseCommand
import multiprocessing
from django.shortcuts import render
import json
from kafka import KafkaConsumer
from kafka import KafkaProducer
from django.http import JsonResponse
import time
from confluent_kafka import Consumer, KafkaError
import django
django.setup()
from orders.models import Order





class Command(BaseCommand):
    def handle(self, *args, **options):
        django.setup()
        # start the script in a separate process
        p = multiprocessing.Process(target=run_script)
        p.start()

def run_script():
            django.setup()
            consumer = KafkaConsumer('order_details', bootstrap_servers=['localhost:29092'])
            messages = []
            counter = 0
            for message in consumer:
                consumed_message = json.loads(message.value.decode())
                messages.append(message.value)
                food = consumed_message["food_name"]
                quantity = consumed_message["quantity"]
                price = consumed_message['price']
                Order.objects.create(
                    food=food,
                    quantity=quantity,
                    price=price
                )
                data = {
                        "food": food,
                        "quantity": quantity,
                        "price": price
                    }
                counter += 1
                # if counter == 10000:
                #     break
            print(data)
            return JsonResponse(data, safe=False)