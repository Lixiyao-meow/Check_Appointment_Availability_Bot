import requests
import json

def send_telegram_msg(message):

    with open("config.json", "r") as f:
        config = json.load(f)
    
    TOKEN = config["TOKEN"]
    chat_id = config["chat_id"]

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"

    # send message
    requests.get(url).json()