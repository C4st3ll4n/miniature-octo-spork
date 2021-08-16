import pika, json

from main import Product, db
from decouple import config

MQTT_URL = config('MQTT_URL')

url = MQTT_URL
params = pika.URLParameters(url)

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='main')


def callback(ch, method, properties, body):
    print("Received in main app at main queue")
    data = json.loads(body)
    print(data)

    if properties.content_type == 'product_created':
        print("Product created")
        product = Product(id=data['id'], title=data['title'], image=data['image'])
        db.session.add(product)
        db.session.commit()

    elif properties.content_type == 'product_updated':
        print("Product Updated")
        product = Product.query.get(data['id'])
        product.title = data['title']
        product.image = data['image']
        db.session.commit()

    elif properties.content_type == 'product_deleted':
        print("Product Deleted")
        product = Product.query.get(data)
        db.session.delete(product)
        db.session.commit()


channel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)

print("Started consuming")
channel.start_consuming()
channel.close()
