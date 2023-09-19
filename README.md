# Check Appointment Availability

We all know that extending one's residency permit in France is a pain in the ass. And booking an appointment in the prefecture is even a bigger pain in the ass. 

This repository is designed to automate the process of checking for newly released appointments and notifying you via Telegram.


## Environment setup

Install packages with
```
pip install selenium
pip install requests
```

The message sending process requires you to set up your own Telegram bot. You can follow the process [here](https://stackoverflow.com/questions/75116947/how-to-send-messages-to-telegram-using-python).

Save your token and chat ID in a file named ```config.json``` within the same folder:

```
{
    "TOKEN": {your bot TOKEN},
    "chat_id": {your chat id}
}
```

You may need to adjust the domain URL in ```main.py``` to match the corresponding prefecture and service.

## Run
```
python main.py
```