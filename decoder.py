from bitarray import bitarray
import json

def decoder(binary_body):
    binary_body = b'{"B": "00", "!": "01", "y": "10", "l": "11", "msg": "001011111001"}'
    body = json.loads(binary_body.decode('utf-8'))
    message = body["msg"]
    body.pop('msg', None)

    for key in body:
        body[key] = bitarray(body[key])

    decode = bitarray(message).decode(body)
    print(''.join(decode))