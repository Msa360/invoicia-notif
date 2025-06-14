import logging
import invoicia_notif
import yo

logger = invoicia_notif.configure_logger(__name__)

logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")
yo.log()