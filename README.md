# LaPlaceAPI
Fully API Create and Delete Order

# How To Run It
```bash
pip install -r requirement.txt
```
Then Run Main.py

# Create Order
API to send Request to Server and Get Pdf File as Return , Request Accept json Data in this Format :
```
{
    "Name": "John",
    "LastName": "Doe",
    "PhoneNumber": "XXXXXXXXXXX",
    "Reservation": "X",
    "Order": "X",
    "CustomMessage": "X"
}
```
Url = http://127.0.0.1:5000/Create,
The Request Sent To Server ,It genereate a Random Orderid , the content Get Sent to Telegram Group And Get back the *Message_id* value (So we can Edit message when Order is cancelled)
and then get saved To Archive in this format Example: 
```
    {
        "OrderId": 15751,
        "Name": "Ait Alaya",
        "LastName": "Yassine",
        "PhoneNumber": "0603692253",
        "Order": "Pizza Champinion x 2 \n Boisson",
        "CustomMessage": "avec Mayonaise",
        "Reservation": "23/04/2024",
        "CreatedTime": "2024-04-22 22:42:05.780152",
        "Message_id": 25
    },
```
