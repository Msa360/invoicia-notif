import requests
import os
from dotenv import load_dotenv

load_dotenv()
DISCORD_WEBHOOK = os.environ.get("DISCORD_WEBHOOK")

def warning_discord(message: str, description: str = ""):
    webhook_url = DISCORD_WEBHOOK
    embed = {
        "title": "⚠️ " + message,
        "description": description,
        "color": 0xFFA500
    }
    data = {
        "embeds": [embed]
    }
    requests.post(webhook_url, json=data)

def error_discord(message: str, description: str = ""):
    webhook_url = DISCORD_WEBHOOK
    embed = {
        "title": "❌ " + message,
        "description": description,
        "color": 0xFF0000
    }
    data = {
        "embeds": [embed]
    }
    requests.post(webhook_url, json=data)