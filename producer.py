import pika
import json
def sendMsgRabbitMq(queue,msg):
    parameters = pika.URLParameters('amqps://urjdtuuy:QQRrX2E2oquZA44mUB_gHm9m9HS270ME@beaver.rmq.cloudamqp.com/urjdtuuy')
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    channel.basic_publish(exchange='',
                        routing_key=queue,
                        body=json.dumps(msg))
    print(" [x] Sent",json.dumps(msg))
    return msg