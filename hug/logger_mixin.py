import logging

class LoggerMixin:
    def __init__(self, logger_name="hug"):
        self._logger = logging.getLogger(logger_name)
        if not self._logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            self._logger.addHandler(handler)
            self._logger.setLevel(logging.DEBUG)