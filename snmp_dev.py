"""
This simulates a SNMP device which sends information through UDP port 162
"""
import sys
import socket
from time import sleep

#local module
import snmp_walker

MESSAGE=snmp_walker.walk('localhost', '1.3.6.1.2.1.1.1') #fatching system info through snmpwalk from snmp_waker module
print(MESSAGE)




UDP_IP = "localhost"
UDP_PORT = 5678
# MESSAGE = "SNMP SNMP SNMP"




clt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    try:
        clt.sendto(bytes(str(MESSAGE),"utf-8"),(UDP_IP,UDP_PORT))
        print("message sent is:  ",MESSAGE)
        sleep(10)
    except KeyboardInterrupt:
        clt.sendto(bytes("quit","utf-8"),(UDP_IP,UDP_PORT))
        clt.close()
        exit()