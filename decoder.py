from bitarray import bitarray
import json

def decoder(binary_body):
    body = json.loads(binary_body.decode('utf-8'))
    message = body["msg"]
    body.pop('msg', None)
    print(message)
    for key in body:
        body[key] = bitarray(body[key])
    print(body)
    decode = bitarray(message).decode(body)
    print(''.join(decode))