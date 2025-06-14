# Invoicia internal library for logs & notifications to Discord

### Usage
Required environment variables:
```bash
LOG_LEVEL="DEBUG" # stdout
DISCORD_LOG_LEVEL="WARNING" # discord webhook
DISCORD_WEBHOOK="" # webhook url
```
```py
import invoicia_notif

logger = invoicia_notif.configure_logger(__name__)
logger.debug("Debug!")
```