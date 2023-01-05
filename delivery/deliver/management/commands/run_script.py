from django.core.management.base import BaseCommand
import multiprocessing
import json
from kafka import KafkaConsumer
from kafka import KafkaProducer
from django.http import JsonResponse
import time
from confluent_kafka import Consumer, KafkaError
import django
django.setup()
from deliver.models import Deliver




class Command(BaseCommand):
    def handle(self, *args, **options):
        django.setup()
        # start the script in a separate process
        p = multiprocessing.Process(target=run_script)
        p.start()

def run_script():
            django.setup()
            consumer = KafkaConsumer('deliver_details', bootstrap_servers=['localhost:29092'])
            messages = []
            counter = 0
            for message in consumer:
                consumed_message = json.loads(message.value.decode())
                messages.append(message.value)
                food = consumed_message["food_name"]
                quantity = consumed_message["quantity"]
                price = consumed_message['price']
                status = consumed_message['status']
                Deliver.objects.create(
                    food=food,
                    quantity=quantity,
                    price=price,
                    status=status
                )
                data = {
                        "food": food,
                        "quantity": quantity,
                        "price": price,
                        "status":status
                    }
                counter += 1
                # if counter == 10000:
                #     break
            print(data)
            return JsonResponse(data, safe=False)