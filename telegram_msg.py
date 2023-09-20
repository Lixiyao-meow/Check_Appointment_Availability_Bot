import requests
import os
import dotenv

def send_telegram_msg(message: str):
    token = os.getenv("TOKEN")
    chat_id = os.getenv("CHAT_ID")

    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"

    # send message
    return requests.get(url).status_code