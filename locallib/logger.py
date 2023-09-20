import sys
import logging

def setup_logging(logger_name: str, debug_enabled: bool = False) -> logging.Logger:
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%d-%b-%y %H:%M:%S'
    )

    logger: logging.Logger = logging.getLogger(logger_name)
    
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)

    logger.addHandler(console_handler)

    logger.setLevel(logging.INFO)
    if debug_enabled:
        logger.setLevel(logging.DEBUG)

    return logger