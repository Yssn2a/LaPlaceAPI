from flask import Flask, request
import API
import random
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/Create', methods=['POST'])
def CreateOrder():
    if request.method == 'POST':
        data = request.json
        OrderId = random.randint(0, 100000)
        Name = data.get('Name')
        LastName = data.get('LastName')
        PhoneNumber = data.get('PhoneNumber')
        Order = data.get('Order')
        CustomMessage = data.get('CustomMessage')
        Reservation = data.get('Reservation')
        Link =API.SendOrder(OrderId=OrderId, Name=Name, LastName=LastName, PhoneNumber=PhoneNumber, Order=Order, CustomMessage=CustomMessage, Reservation=Reservation)
        return {"success":f"{Link}"}
    else:
        return {"False"}

@app.route('/Delete', methods=['POST'])
def DeleteOrderx():
    if request.method == 'POST':
        data = request.json
        Name = data.get('Name')
        OrderId = data.get('OrderId')
        resp = API.DeleteOrder(int(OrderId), f"{Name}")
        return {"result": resp}
    else:
        return {"error": "Message ID not found"}


if __name__ == '__main__':
    app.run(debug=True)