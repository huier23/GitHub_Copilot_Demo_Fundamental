- Add loggging to the code below
[]: # - Use the logging module
[]: # - Use the logging.info() method to log a message
import logging
logging.basicConfig(level=logging.INFO)
def add(a, b):
    logging.info(f"Adding {a} and {b}")
    return a + b
[]: # - Use the logging.warning() method to log a warning message
def divide(a, b):
    if b == 0:
        logging.warning("Attempted to divide by zero")
        return None
    logging.info(f"Dividing {a} by {b}")
    return a / b
[]: # - Use the logging.error() method to log an error message    