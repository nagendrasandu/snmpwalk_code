"""
This is a Kafka Consumer basic code to receive data from
Kafka Producer
"""
import re

import pymysql
from kafka import KafkaConsumer

consumer = KafkaConsumer('first_topic',
                         bootstrap_servers=['localhost:9092'],
                         enable_auto_commit=True)


def save_info(device_oid, hostname, device_OS, OS_type, OS_bit_version):
    # Open database connection
    db = pymysql.connect(host="localhost",
                         user="root",
                         password="",
                         database="snmp_db")

    cursor = db.cursor()
    try:


        # Prepare SQL query to INSERT a record into the database.
        cursor.execute("INSERT INTO device_info(device_oid,hostname,device_os,os_type,os_bit_version)"
                       "VALUES(%s,%s,%s,%s,%s)",(device_oid,hostname,device_OS,OS_type,OS_bit_version))



        # Commit your changes in the database
        db.commit()
        print('successfully saved')
    except:
        # Rollback in case there is any error
        db.rollback()

        # disconnect from server
        db.close()


def parse(message):
    # if message==message
    device_oid = re.search('value=b(.*?) = ', message).group(1)
    # print(device_oid)
    hostname = re.search('Linux (.*?) 4.15.0', message).group(1)
    # print(hostname)
    device_OS = re.search('= (.*?) ldap.example.com ', message).group(1)
    # print(device_OS)
    OS_type = re.search('#134-(.*?) SMP', message).group(1)
    # print(OS_type)
    OS_bit_version = re.search('2021 (.*?),', message).group(1)
    # print(OS_bit_version)
    save_info(device_oid,hostname,device_OS,OS_type,OS_bit_version)



try:
    for message in consumer:
        if message.value == b"quit":
            print("Message Transfer Completed")
            exit()
        parse(str(message))
except KeyboardInterrupt:
    exit()