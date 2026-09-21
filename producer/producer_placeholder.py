import json

from confluent_kafka import Producer

BOOTSTRAP_SERVERS = "localhost:9092"
TOPIC = "orders"

with open("sample_orders.json") as file:
    orders = json.load(file)

# TODO 1: create the producer


# TODO 2: define the delivery callback


for order in orders:
    # TODO 3: publish the order
    pass

# TODO 4: flush before exiting
