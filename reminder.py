import datetime
import json



data = []
with open('orders.json', 'r') as file:
    for line in file:
        data.append(line.strip())



for item in data:
    print('---------')
    print(item)
    print(json.loads(item))


    expiration_date = item['expiration']
    reminder_date = expiration_date - datetime.timedelta(days=3)

    # Compare with the current date
    if datetime.date.today() >= reminder_date:
        print(f"Send reminder for order {item['order_code']} (Chat ID: {item['chat_id']})")
