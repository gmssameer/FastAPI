import logging
import sys


#Get Logger
logger = logging.getLogger()

# create Logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

#create handlers
stream_handler = logging.StreamHandler(sys.stdout)
file_handler = logging.FileHandler('app.log')

#Set formater  
stream_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# add handlers to logger
logger.handlers = [stream_handler, file_handler]

# Set Log Level
logger.setLevel(logging.INFO)
