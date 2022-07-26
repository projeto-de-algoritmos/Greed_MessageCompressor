import pika, sys, os
from decoder import *

def main():
    parameters = pika.URLParameters('amqps://urjdtuuy:QQRrX2E2oquZA44mUB_gHm9m9HS270ME@beaver.rmq.cloudamqp.com/urjdtuuy')
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)
        print(body)
        decoder(body)
    
    channel.basic_consume(queue='rabbitmq-queue', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)