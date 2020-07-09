import logging
from logging.handlers import TimedRotatingFileHandler
def logger():
    try:
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        handler = TimedRotatingFileHandler('log2.log', when="s", interval=5, encoding='utf8')
        handler.suffix = "%Y-%m-%d"
        handler.setFormatter(formatter)
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        logger.addHandler(handler)
        logger.debug('debug message')
        logger.info('info message')
        logger.warning('warn message')
        logger.error('error message')
        logger.critical('critical message')
        return logging
    except Exception as e:
        return False

