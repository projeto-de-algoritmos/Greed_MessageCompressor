import pika
import json
def sendMsgRabbitMq(queue,msg):
    parameters = pika.URLParameters('STRING_DE_CONECAO')
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    # channel.queue_declare(queue=queue')
    channel.basic_publish(exchange='',
                        routing_key=queue,
                        body=json.dumps(msg))
    print(" [x] Sent 'Hello World!'")