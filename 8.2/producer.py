from time import sleep
import json
from datetime import datetime
from models import Recipient
from random import randint
from faker import Faker
import pika


fake = Faker()

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

channel.exchange_declare(exchange='email_exchange', exchange_type='direct')
channel.queue_declare(queue='email_queue')
channel.queue_bind(exchange='email_exchange', queue='email_queue')


def add_data():
    for _ in range(10):
        fake_fullname = fake.name()
        fake_email = fake.email()
        document = Recipient(fullname=fake_fullname, email=fake_email)
        document.save()


def main():
    add_data()
    recipients = Recipient.objects()
    for recipient in recipients:
        message = {
            "id": str(recipient.id),
            "payload": [recipient.fullname, recipient.email],
            "date": datetime.now().isoformat(),
            "text": fake.text()
        }

        channel.basic_publish(
            exchange='email_exchange',
            routing_key='email_queue',
            body=json.dumps(message).encode(),
            properties=pika.BasicProperties(delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE)
            )
        print("Sent %r" % message)
        timer = randint(1, 3)
        sleep(timer)
    connection.close()


if __name__ == "__main__":
   main()