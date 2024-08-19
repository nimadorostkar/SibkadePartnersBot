import json
from datetime import datetime, timedelta, date
import time
import telebot


TOKEN = "7445678382:AAG3-dxleieDz_dBJh4YCeMHQeuj389gM6U"

def reminderrr():
    with open('orders.json') as json_file:
        json_data = json_file.read()
    python_obj = json.loads(json_data)

    for item in python_obj:
        expiration_date = datetime.strptime(item['expiration'], "%Y-%m-%d")
        reminder_date = expiration_date - timedelta(days=3)
        today = datetime.combine(date.today(), datetime.min.time())
        if today >= reminder_date:
            #print(f"Send reminder for order {item['order_code']} (Chat ID: {item['chat_id']})")
            bot = telebot.TeleBot(TOKEN)
            bot.send_message(chat_id=item['chat_id'],
                             text=f"3 days until the end of your service. \norder_code: {item['order_code']} \nyour service expiration is {item['expiration']}",
                             reply_to_message_id=item['message_id'])


while True:
    reminderrr()
    # Sleep for 24 hours (86400 seconds)
    time.sleep(86400)