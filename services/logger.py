import logging
import logging.handlers

# --- Setting up Logger ---
LOG_FILE_NAME = 'status.log'
def init_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logger_file_handler = logging.handlers.RotatingFileHandler(
        LOG_FILE_NAME,
        maxBytes = 1024 * 1024,
        backupCount = 2,
        encoding = "utf8",
    )
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    logger_file_handler.setFormatter(formatter)
    logger.addHandler(logger_file_handler)
    return logger
# --- ---