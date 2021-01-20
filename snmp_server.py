"""
This server reveives the snmp trap data through TCP port
8768 to be sent to Kafka Server
"""
import socket
from time import sleep
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers =['localhost:9092'])

TCP_IP = "localhost"
TCP_PORT = 8768

serv_tcpsock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serv_tcpsock.bind((TCP_IP,TCP_PORT))
serv_tcpsock.listen(5)
conn,addr = serv_tcpsock.accept()
data = conn.recv(1024)
producer.send('first_topic', data)
producer.flush()
while True:
    try:

        if (data == b"quit"):
            producer.send('first_topic',data)
            producer.flush()
            serv_tcpsock.close()
            exit()
        if (data == b"") or (b'empty' in data):
            continue
        print(data)


    except KeyboardInterrupt:
        serv_tcpsock.close()
        exit()

