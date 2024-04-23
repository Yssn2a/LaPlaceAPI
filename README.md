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
The SS response if true :
```
{"success":"LINK TO PDF FILE CONTAINGING ORDER INFOS"}
```
The SS response is False :
```
{"False"}
```


# Delete Order
Gives The Client the Chance To Delete Order Using Two Inputs (Orderid,Name)
```
{
"OrderId": "15751",
"Name": "Yassine"
}
```
Url = http://127.0.0.1:5000/Delete,
The Request Sent To Server, Opens Archive Checks if OrderId and Name Matches Same Entry and If they are available if this all true it Gets Message_id Value and Edit Messsage on Telegram that it was cancelled

Response If:
OrderId and Name Found And order cancelled:
```
{
"result": 1
}
```
OrderId and Name Found And But order Already cancelled:
```
{
"result": 0
}
```
OrderId Or Username Inccorect :
```
{
"result": "OrderId Or Name are incorrect"
}
```


