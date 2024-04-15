import json

from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

products = {
    'pepsi': {'type': '2 lt bottle', 'price': 120, 'qty': 250},
    'coke': {'type': '500 ml bottle', 'price': 60, 'qty': 180},
    'thumbs_up':{'type': '300 ml can', 'price':50, 'qty': 120}
}

class Products(Resource):

    def get(self, product):
        return {product: products[product]}

    def put(self, product):
        products[product]['cat'] = request.form['cat']
        return {product: products[product]}

    def patch(self, product):
        data1 = request.json
        print(f"data1: {data1}")
        data = json.loads(data1)
        print(type(data))
        print(f"data: {data}")
        products[product][list(data.keys())[0]] = data[list(data.keys())[0]]
        return products[product]

    def post(self, product):
        print("property :", request.json)
        data1 = request.json
        print(f"data1: {data1}")
        data = json.loads(data1)
        # print(type(data))
        # print(f"data: {data}")
        products[product] = data
        return products

    def delete(self, product):
        if product in products:
            del products[product]
            return products
        else:
            return {'KeyError': "Invalid Key, Please enter a valid key....."}

api.add_resource(Products, "/getproduct/<string:product>")

if __name__ == '__main__':
    app.run(debug=True, use_reloader= True)

