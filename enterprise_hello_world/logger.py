import logging
import sys

def get_logger(name: str) -> logging.Logger:
    # Setting up a logger for enterprise-level compliance
    logger = logging.getLogger(name)
    if not logger.hasHandlers():  # Prevent adding multiple handlers if already configured
        logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        
        file_handler = logging.FileHandler("enterprise_hello_world.log")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        
        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)
    
    return logger