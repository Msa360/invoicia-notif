import logging
import sys
import requests

class DiscordHandler(logging.Handler):
    def __init__(self, webhook_url, level):
        super().__init__(level)
        self.webhook_url = webhook_url

    def emit(self, record):
        # Customize message based on log level
        if record.levelno >= logging.ERROR:
            embed = {
                "title": "❌ ERROR " + f"({record.filename}:{record.funcName}:{record.lineno})",
                "description": record.getMessage(),
                "color": 0xFF0000
            }
        elif record.levelno >= logging.WARNING:
            embed = {
                "title": "⚠️ WARNING " + f"({record.filename}:{record.funcName}:{record.lineno})",
                "description": record.getMessage(),
                "color": 0xFFA500
            }
        elif record.levelno == logging.INFO:
            embed = {
                "title": "ℹ️ INFO " + f"({record.filename}:{record.funcName}:{record.lineno})",
                "description": record.getMessage(),
                "color": 0x0084ff  # blue
            }
        else:  # DEBUG and below
            embed = {
                "title": "🐞 DEBUG " + f"({record.filename}:{record.funcName}:{record.lineno})",
                "description": record.getMessage(),
                "color": 0x2ECC40  # green
            }
        data = {"embeds": [embed]}
        try:
            requests.post(
                self.webhook_url,
                json=data,
            )
        except Exception as e:
            print(f"Failed to send log to Discord: {e}", file=sys.stderr)

