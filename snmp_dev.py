"""
This simulates a SNMP device which sends information through UDP port 162
"""

import sys
import socket
from time import sleep


#local module
import snmp_walker
import logger

log=logger.snmp_logger('snmp_dev')



MESSAGE=snmp_walker.walk('localhost', '1.3.6.1.2.1.1.1') #fatching system info through snmpwalk from snmp_waker module
# log.info(MESSAGE)




UDP_IP = "localhost"
UDP_PORT = 5678





clt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    try:
        clt.sendto(bytes(str(MESSAGE),"utf-8"),(UDP_IP,UDP_PORT))
        log.info("message sent is %s: " %(MESSAGE))
        sleep(10)
    except KeyboardInterrupt:
        clt.sendto(bytes("quit","utf-8"),(UDP_IP,UDP_PORT))
        clt.close()
        exit()