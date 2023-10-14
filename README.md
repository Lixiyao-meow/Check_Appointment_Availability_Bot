# 🤖 Check Appointment Availability Bot | Préfecture RDV Bot 🤖

**⚠️For Non-Commercial Use Only⚠️**

We all know that extending one's residency permit in France is a pain in the ass. And booking an appointment in the prefecture is even a bigger pain in the ass. 

This repository is designed to automate the process of checking for newly released appointments and notifying you via Telegram.

**French version below:**

Nous savons tous que prolonger son titre de séjour en France est une vraie galère. Et prendre rendez-vous à la préfecture, c'est encore plus compliqué.

Ce GitHub a été conçu pour checker automatiquement de nouveaux créneaux de rendez-vous disponibles et vous avertir via Telegram.

## Environment setup

### Packages

Installation with [poetry](https://python-poetry.org)
```
poetry install
```

Installation with pip
```
poetry add requests selenium python-dotenv
```

The message sending process requires you to set up your own Telegram bot. You can follow the process [here](https://stackoverflow.com/questions/75116947/how-to-send-messages-to-telegram-using-python).

### Environment variables
Set the environment variables `TOKEN` and `CHAT_ID`.

Alternatively, save your token and chat ID in a file named ```.env``` within the same folder:

```
TOKEN={your bot TOKEN},
CHAT_ID={your chat id}
```

You may need to adjust the domain URL in ```main.py``` to match the corresponding prefecture and service.

## Run
```
python main.py
```
