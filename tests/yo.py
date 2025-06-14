import invoicia_notif

logger = invoicia_notif.configure_logger(__name__)

def log():
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
