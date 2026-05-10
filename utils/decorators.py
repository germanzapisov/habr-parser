from .config import logger

def logger_decorator(func):
    def wrapper(*args, **kwargs):
        logger.debug('func started')

        result = func(*args, **kwargs)

        logger.debug('func ended')

        return result
    return wrapper