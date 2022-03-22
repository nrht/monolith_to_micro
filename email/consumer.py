from confluent_kafka import Consumer
from django.core.mail import send_mail
import json
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
django.setup()

consumer = Consumer({
    'bootstrap.servers': 'pkc-l6ojq.asia-northeast1.gcp.confluent.cloud:9092',
    'security.protocol': 'SASL_SSL',
    'sasl.username': 'QHQFIXFP5L6YZR4I',
    'sasl.password': 'k6tr9eU/TgJxWmhRCdCSKBp6ep4Oj+nQqIrnRCKGAnjZW3z7Ce/ofecbcZP2//G6',
    'sasl.mechanism': 'PLAIN',
    'group.id': 'myGroup',
    'auto.offset.reset': 'earliest'
})


consumer.subscribe(['default'])

while True:
    msg = consumer.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        print(f'Consumer error: {msg.error()}')
        continue

    print(f'Received message: {msg.value()}')

    order = json.loads(msg.value())

    # Admin Email
    send_mail(
        subject='An Order has been completed',
        message='Order #' + str(order['id']) + 'with a total of $' +
        str(order['admin_revenue']) + ' has been completed!',
        from_email='from@email.com',
        recipient_list=['admin@admin.com']
    )

    send_mail(
        subject='An Order has been completed',
        message='You earned $' +
        str(order['ambassador_revenue']) + ' from the link #' + order['code'],
        from_email='from@email.com',
        recipient_list=[order['ambassador_email']]
    )

consumer.close()
