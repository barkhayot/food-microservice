import json
from kafka import KafkaConsumer
from kafka import KafkaProducer


ORDER_KAFKA_TOPIC = "order_details"
ORDER_CONFIRMED_KAFKA_TOPIC = "order_confirmed"

consumer = KafkaConsumer(
    ORDER_KAFKA_TOPIC, 
    bootstrap_servers="localhost:29092"
)
producer = KafkaProducer(bootstrap_servers="localhost:29092")

KafkaConsumer(ORDER_KAFKA_TOPIC, bootstrap_servers="localhost:29092")

print("Gonna start listening")
# while True:
#     for message in consumer:
#         print("Ongoing transaction..")
#         consumed_message = json.loads(message.value.decode())
#         print(consumed_message)
#         # user_id = consumed_message["user_id"]
#         # total_cost = consumed_message["total_cost"]
#         data = {
#             "food": consumed_message["food_name"],
#             "quantity": consumed_message["quantity"],
#             "price": consumed_message["price"]
#         }
#         print("Successful transaction..")
        #producer.send(ORDER_CONFIRMED_KAFKA_TOPIC, json.dumps(data).encode("utf-8"))