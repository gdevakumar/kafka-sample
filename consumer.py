from confluent_kafka import Consumer
from config import config

consumer = Consumer(config)
consumer.subscribe(["my-topic"])
try:
    while True:
        msg = consumer.poll(1.0)
        if msg is not None and msg.error() is None:
            print("key = {key:12} value = {value:12}".format(key=msg.key().decode('utf-8'), value=msg.value().decode('utf-8')))
except KeyboardInterrupt:
    pass
finally:
    consumer.close()
    