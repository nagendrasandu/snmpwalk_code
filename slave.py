"""
This receives from snmp device the data on udp port 162
and sends to server on tcp port 8768
"""
import sys
import socket
from time import sleep

UDP_IP = "localhost"
UDP_PORT = 5678

TCP_IP = "localhost"
TCP_PORT = 8768

clt_tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clt_tcpsock.connect((TCP_IP, TCP_PORT))

serv_udpsock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
serv_udpsock.bind((UDP_IP,UDP_PORT))

while True:
    try:
        data,addr = serv_udpsock.recvfrom(1024)
        if (data == b"quit"):
            clt_tcpsock.send(data)
            serv_udpsock.close()
            clt_tcpsock.close()
            exit()
        if (data == b"") or (b'empty' in data):
            continue
        print("Received message:  ",data)

        clt_tcpsock.send(data)

    except KeyboardInterrupt:
        serv_udpsock.close()
        clt_tcpsock.close()
        exit()


