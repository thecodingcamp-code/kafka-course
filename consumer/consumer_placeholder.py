import json

from confluent_kafka import Consumer

BOOTSTRAP_SERVERS = "localhost:9092"
TOPIC = "orders"
GROUP_ID = "order-notifications"

# TODO 1: create the consumer and configure its group

# TODO 2: subscribe to the topic

try:
    while True:
        # TODO 3: poll for a message, skipping empty polls and errors

        # TODO 4: decode the order and print the notification
        pass
except KeyboardInterrupt:
    pass
finally:
    consumer.close()
