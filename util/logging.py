import logging

logger_format = '%(asctime)s - %(levelname)s - %(message)s'
logger_output_file = './running.log'
logging.basicConfig(filename=logger_output_file, format=logger_format)
logger = logging.getLogger('service')
logger.setLevel(logging.INFO)
