import sys, os
import logging
from dotenv import load_dotenv

from invoicia_notif.discord import DiscordHandler

load_dotenv()

def get_log_level_env(env_var: str, default: str = "INFO") -> str:
    """
    Get the log level from an environment variable, with a default value.
    It will raise ValueError if the log level is not valid.
    """
    log_level = os.environ.get(env_var, default)
    try:
        logging._nameToLevel[log_level]
    except KeyError:
        raise ValueError(f"Invalid log level: {log_level} from {env_var}. Must be one of: {list(logging._nameToLevel.keys())}")
    return log_level


LOG_LEVEL = get_log_level_env("LOG_LEVEL")

DISCORD_LOG_LEVEL = get_log_level_env("DISCORD_LOG_LEVEL", LOG_LEVEL)

DISCORD_WEBHOOK = os.environ["DISCORD_WEBHOOK"]


# Remove default Lambda handlers
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

logger = logging.getLogger(__name__)
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(logging.Formatter('[%(levelname)s] [%(name)s.%(funcName)s:%(lineno)d] %(message)s'))
logger.addHandler(handler)
logger.setLevel(getattr(logging, LOG_LEVEL))

# Add DiscordHandler to logger
discord_handler = DiscordHandler(DISCORD_WEBHOOK, DISCORD_LOG_LEVEL)
logger.addHandler(discord_handler)
