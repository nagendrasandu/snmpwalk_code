"""
a function to display device info using snmpwalk
"""

from easysnmp import Session

session=Session(hostname='localhost',community='public',version=1)
system_items = session.walk('system')

# Each returned item can be used normally as its related type (str or int)
# but also has several extended attributes with SNMP-specific information
for item in system_items:
    result='{oid}.{oid_index} {snmp_type} = {value}'.format(
        oid=item.oid,
        oid_index=item.oid_index,
        snmp_type=item.snmp_type,
        value=item.value
    )
    print(result)
