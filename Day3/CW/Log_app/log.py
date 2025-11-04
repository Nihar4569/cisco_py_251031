import logging

logging.basic(
    filename = 'app.log',
    level = logging.INFO,
    format = '%(asctime)s [%(levelname)s] %(message)s'
)