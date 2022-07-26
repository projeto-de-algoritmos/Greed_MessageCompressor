from flask import (
    Flask, jsonify,request
)
from flask_cors import CORS
import json
from bitarray import bitarray
from producer import sendMsgRabbitMq
from huffman_code import *

app = Flask("application")
cors = CORS(app, resources={r"/*": {"origins": "*"}})
# Define error when status code is 404 
@app.errorhandler(404)
def page_not_found(error):
    return jsonify({"error_message":"This page doesn't exist"}),404

# Define error when status code is 500
@app.errorhandler(500)
def page_not_found(error):
    return jsonify({"error_message":"O id desse campeão não existe"}),500

# Home page
@app.route('/',methods=['GET'])
def index():
    return jsonify({"status":"API is up","version":"1"})

@app.route('/huffman',methods=['POST'])
def compressData():
    msg = ""
    body = request.json
    msg = huffman(body["msg"])
    sendMsgRabbitMq("rabbitmq-queue",msg)

    return jsonify(msg)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8081)

