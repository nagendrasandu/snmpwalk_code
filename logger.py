import logging
import os

def snmp_logger(name):
    logger=logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    # add formatter to ch
    ch.setFormatter(formatter)

    # add ch to logger
    logger.addHandler(ch)

    file_handler=logging.FileHandler('log/snmp_log.txt')  #writing log activity to a file
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)





    return logger

