# © @devforgekush. All rights reserved.
# Audiofy Bot

import time
import requests

# Replace with your Railway bot URL
BOT_URL = "https://your-railway-bot-url.up.railway.app/"
PING_INTERVAL = 12 * 60  # 12 minutes in seconds

while True:
    try:
        response = requests.get(BOT_URL)
        print(f"Pinged {BOT_URL} - Status code: {response.status_code}")
    except Exception as e:
        print(f"Error pinging {BOT_URL}: {e}")
    time.sleep(PING_INTERVAL)
