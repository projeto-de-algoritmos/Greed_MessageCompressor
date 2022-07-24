from bitarray import bitarray
from producer import sendMsgRabbitMq
from huffman_code import *

msg = huffman()
sendMsgRabbitMq("teste",msg)