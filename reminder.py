from datetime import datetime, date, timedelta
import json


with open('orders.json') as json_file:
    json_data = json_file.read()
python_obj = json.loads(json_data)

for item in python_obj:
    expiration_date = datetime.strptime(item['expiration'], "%Y-%m-%d")
    reminder_date = expiration_date - timedelta(days=3)
    today = datetime.combine(date.today(), datetime.min.time())
    if today >= reminder_date:
        print(f"Send reminder for order {item['order_code']} (Chat ID: {item['chat_id']})")
        context.bot.send_message(chat_id=item['chat_id'], text=f"your service expiration is {item['expiration']}")
