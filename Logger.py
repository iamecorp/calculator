import logging

class Logger:
    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger("ComplexCalculator")

    def log(self, message):
        self.logger.info(message)
