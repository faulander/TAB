import functools
from loguru import logger

# This decorator can be applied to
def with_logging(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger.info('LOG: Running job "%s"' % func.__name__)
        result = func(*args, **kwargs)
        logger.info('LOG: Job "%s" completed' % func.__name__)
        return result
    return wrapper
