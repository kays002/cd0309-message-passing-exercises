import json
from flask import Flask, jsonify, request

from .services import retrieve_orders, create_order

app = Flask(__name__)


@app.route('/health')
def health():
    return jsonify({'response': 'Hello World!'})

@app.route('/api/orders/order_data', methods=['GET','POST'])
def abc(order_data):
    if request.method=='GET':
        return Response(json.dumps(retrieve_orders(order_data)), 200, {Content-Type: application/json})
    if request.method=='POST':
        return.Response(json.dumps(create_order(order_data)))

if __name__ == '__main__':
    app.run()
