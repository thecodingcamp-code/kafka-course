import json

from confluent_kafka import Producer

BOOTSTRAP_SERVERS = "localhost:9092"
TOPIC = "orders"

with open("sample_orders.json") as file:
    orders = json.load(file)

producer = Producer({"bootstrap.servers": BOOTSTRAP_SERVERS})


def on_delivery(error, message):
    if error is not None:
        print(f"Delivery failed for {message.key().decode()}: {error}")
    else:
        print(f"Delivered {message.key().decode()} to partition {message.partition()} at offset {message.offset()}")


for order in orders:
    producer.produce(
        TOPIC,
        key=order["order_id"],
        value=json.dumps(order),
        on_delivery=on_delivery,
    )

producer.flush()


