import logging as lg
from logging.handlers import RotatingFileHandler


def create_logger():
    logger = lg.getLogger()
    logger.setLevel(lg.DEBUG)

    formatter = lg.Formatter('%(asctime)s :: %(levelname)s :: %(message)s')

    file_handler = RotatingFileHandler('activity.log', 'a', 1000000, 1)
    file_handler.setLevel(lg.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger
