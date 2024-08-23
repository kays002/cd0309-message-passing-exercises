import json
from flask import Flask, jsonify, request

from .services import retrieve_orders, create_order

app = Flask(__name__)


@app.route('/health')
def health():
    return jsonify({'response': 'Hello World!'})

@app.route('/api/orders/computers', methods=['GET','POST'])
def abc():
    if request.method=='GET':
        return jsonify(retrieve_orders())
    if request.method=='POST':
        order_data=request.json
        return jsonify(create_order(order_data))
    else:
        raise Exception('Unsupported HTTP request type.')

if __name__ == '__main__':
    app.run()
