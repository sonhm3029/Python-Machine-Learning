import logging

logger = logging.getLogger(__name__)
logger.propagate = False


# Create handler
stream_h = logging.StreamHandler()
file_h = logging.FileHandler('file.log')


# level and format
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

logger.addHandler(stream_h)
logger.addHandler(file_h)

logger.warning("This is an warning")
logger.info("This is an error")