from models import Recipient
from time import sleep
from random import randint
import json

import pika

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='email_queue')
print(' [*] Waiting for messages. To exit press CTRL+C')


def callback(ch, method, properties, body):
    #print(f"{ch}, {method}, {properties}, {body}")
    message = json.loads(body.decode())
    print(f" [x] Received {message}")
    Recipient.objects(message=False).update_one(set__message=True)
    timer = randint(1, 3)
    sleep(timer)
    print(f" [x] Done: {method.delivery_tag}")
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='email_queue', on_message_callback=callback)


if __name__ == '__main__':
    channel.start_consuming()