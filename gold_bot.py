import os
import time
import requests
 
BOT_TOKEN = os.environ["8829074599:AAGqPXyaS6HTr6Qkw-TADEHY8gXC-O_UWrA"]
CHAT_ID = "1151138873"

STEP = 50
last_price = None

def get_gold_price():
    url = "https://api.metals.live/v1/spot/gold"
    data = requests.get(url, timeout=10).json()
    return float(data[0]["price"])

def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={
        "chat_id": CHAT_ID,
        "text": text
    })

while True:
    try:
        price = get_gold_price()

        if last_price is None:
            last_price = price
            send_message(f"🟡 Aukso stebėjimas pradėtas.\nDabartinė kaina: {price}$")

        elif price >= last_price + STEP:
            send_message(f"📈 Auksas pakilo +50 USD\nKaina: {price}$")
            last_price = price

        elif price <= last_price - STEP:
            send_message(f"📉 Auksas nukrito -50 USD\nKaina: {price}$")
            last_price = price

        time.sleep(60)

    except Exception as e:
        time.sleep(60)
