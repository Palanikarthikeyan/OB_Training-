import logging

logging.basicConfig(level=logging.ERROR)

try:
    result = 10 / 0
except Exception:
    logging.exception("An Error Occurred")