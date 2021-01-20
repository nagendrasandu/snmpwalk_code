""""
a funcion to diasplay device info using snmpwalk

"""
from pysnmp.hlapi import *


import sys


def walk(host, oid):

    for (errorIndication,
         errorStatus,
         errorIndex,
         varBinds) in nextCmd(SnmpEngine(),
                              CommunityData('public'),
                              UdpTransportTarget((host, 161)),
                              ContextData(),
                              ObjectType(ObjectIdentity(oid)),
                              lookupMib=False,
                              lexicographicMode=False):

        if errorIndication:
            print(errorIndication, file=sys.stderr)
            break

        elif errorStatus:
            print('%s at %s' % (errorStatus.prettyPrint(),
                                errorIndex and varBinds[int(errorIndex) - 1][0] or '?'), file=sys.stderr)
            break

        else:
            for varBind in varBinds:

                 # print(oid.prettyPrint(),'=',varBind.prettyPrint())
                 result='%s = %s' % varBind
                 return result
                 # print(varBind.prettyPrint())


walk('localhost', '1.3.6.1.2.1.1.1')



