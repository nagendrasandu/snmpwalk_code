"""
Descrption:This is a Kafka Consumer basic code to receive data from
            Kafka Producer
author:     sandu nagendra.<nagendra.s@tessrac.com>
"""
import re

import pymysql
import logger
from kafka import KafkaConsumer

log=logger.snmp_logger('snmp_consumer')

consumer = KafkaConsumer('first_topic',
                         bootstrap_servers=['localhost:9092'],
                         auto_offset_reset='latest',enable_auto_commit=True)


def save_info(device_oid, hostname, device_OS, OS_type, OS_bit_version):
    '''description:establishing database connection
                    and saving pasre function results into db.
        parameters:device_oid,hostname,device_OS,OS_type,OS_bit_version takes from parse function result
        author:nagendra sandu <nagendra.s@tessrac.com>'''
    try:

        db = pymysql.connect(host="localhost",
                             user="root",
                             password="",
                             database="snmp_db")

        cursor = db.cursor()
    except Exception as e:
        print('connection error',e)
    try:
        #  SQL query to INSERT a record into the database.
        cursor.execute("INSERT INTO device_info(device_oid,hostname,device_os,os_type,os_bit_version)"
                       "VALUES(%s,%s,%s,%s,%s)",(device_oid,hostname,device_OS,OS_type,OS_bit_version))



        # Commit your changes in the database
        db.commit()
        log.info('successfully saved')
    except:
        # Rollback in case there is any error
        db.rollback()

        # disconnect from server
        db.close()

#parsing function to extract device info

def parse(message):
    '''    description:applying parsing logic to extract reqired info
            parameter:takes message parameter from kafka consumer result.
           author:sandu nagendra<nagendra.s@tessrac.com>     '''
    try:
        if message is not None :

            device_oid = re.search('value=b(.*?) = ', message).group(1)
            hostname = re.search('Linux (.*?) 5.4.0', message).group(1)
            device_OS = re.search('= (.*?) user', message).group(1)

            OS_type = re.search('#72~18.04.1-(.*?) SMP', message).group(1)

            OS_bit_version = re.search('2021 (.*?),', message).group(1)

            save_info(device_oid,hostname,device_OS,OS_type,OS_bit_version) #calling save_info function with params
        else:
            log.info('message is empty')
    except Exception as e:
        log.info(e)
try:
    for message in consumer:
        if message.value == b"quit":
            print("Message Transfer Completed")
            exit()
        # log.info(message)
        parse(str(message))
except KeyboardInterrupt:
    exit()