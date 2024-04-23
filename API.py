import json
import datetime
import requests
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph
from datetime import datetime
from pdf_creator.creator import pdf_creator
import fileuploader
import asyncio
import os

BOT = "7078492310:AAEUgsBqUIaZ59JYFwCzZD5bnnGseWbp22c"

async def run(OrderId):
    """Upload The pdf"""
    f = open(f"{OrderId}.pdf", "rb")  # Open file as bytes
    response = await fileuploader.upload(f.read(), f.name) 
    return (response.file_url_full) 



def Cpdf(pdf_file, content):
    """create pdf file with given content"""
    new_pdf = pdf_creator(pdf_file)


    content_data = [
        ['Field', 'Value'],
        ['Order ID', content.get('OrderId', '')],
        ['Name', content.get('Name', '')],
        ['Last Name', content.get('LastName', '')],
        ['Phone Number', content.get('PhoneNumber', '')],
        ['Order', content.get('Order', '')],
        ['Created Time', content.get('CreatedTime', '')]
    ]

    new_pdf.table(content_data, 100, 600)
    new_pdf.save()

    return f'{pdf_file}.pdf'

def ReceiveOrder(bot_token, chat_id, message):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    params = {"chat_id": chat_id, "text": message,'parse_mode': 'Markdown'}
    response = requests.post(url, params=params)
    json_response = response.json()
    if json_response['ok']:
        MID = json_response['result']['message_id']
        return MID
    else:
        print("Failed to send message")
        return None

def SendOrder(OrderId=None,
              Name=None,
              LastName=None,
              PhoneNumber=None,
              Order=None,
              CustomMessage=None,
              Reservation=None):
    """Send order to telegram and save it to archive."""
    content = {
        "OrderId": OrderId,
        "Name": Name,
        "LastName": LastName,
        "PhoneNumber": PhoneNumber,
        "Order": Order,
        "CustomMessage": CustomMessage,
        "Reservation": Reservation,
        "CreatedTime": str(datetime.now()),
    }

    Message = f"Order: *#{OrderId}* 🟢\nReservation Pour: *{Reservation}*\nPrénom: *{Name}*\nNom: *{LastName}*\nTéléphone: *{PhoneNumber}*\n\nCommande:\n{Order}\n\nDétail:\n{CustomMessage}"
    MessageId = ReceiveOrder(BOT, "-4188869977", Message)
    content["Message_id"] = MessageId

    with open('Archive.json', 'r+') as f:
        Archive = json.load(f)
        Archive.append(content)
        f.seek(0)  
        json.dump(Archive, f, indent=4) 

    PDF = Cpdf(f'{OrderId}.pdf', content)
    LPDF = asyncio.run(run(OrderId))
    os.remove(f'{OrderId}.pdf')
    return LPDF

def DeleteOrder(OrderId, Name):
    """cancelling an order from the Telegram by its id and name."""
    with open("Archive.json", 'r+') as f:
        Data = json.load(f)

        for entry in Data:
            if entry.get('OrderId') == OrderId and entry.get('Name') == Name:
                order_id = entry.get('OrderId')
                name = entry.get('Name')
                last_name = entry.get('LastName')
                phone_number = entry.get('PhoneNumber')
                order = entry.get('Order')
                custom_message = entry.get('CustomMessage')
                reservation = entry.get('Reservation')
                message_id = entry.get('Message_id')

                if message_id:
                    Message = f"Order: *#{order_id}* 🔴\nReservation Pour: *{reservation}*\nPrénom: *{name}*\nNom: *{last_name}*\nTéléphone: *{phone_number}*\n\nCommande:\n{order}\n\nDétail:\n{custom_message}"
                    url = f"https://api.telegram.org/bot{BOT}/editMessageText"
                    params = {
                        "chat_id": "-4188869977",
                        "message_id": message_id,
                        "text": Message,
                        'parse_mode': 'Markdown',
                    }
                    response = requests.post(url, params=params)
                    if response.ok:
                        response = 1
                    else:
                        response = 0
                else:
                    print("Message ID not found in the data.")
            else:
                response = "OrderId Or Name are incorrect"
    return response

