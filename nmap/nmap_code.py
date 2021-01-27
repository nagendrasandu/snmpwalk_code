import nmap

nmScan = nmap.PortScanner()

nmScan.scan('127.0.0.1', '21-1024')

print(nmScan.command_line())

for host in nmScan.all_hosts():
    print('Host :%s (%s)' %(host,nmScan[host].hostname()))

    print('State :%s' %nmScan[host].state())

    for proto in nmScan[host].all_protocols():
        print('----------')
        print('Protocol : %s' %proto)

        lport = nmScan[host][proto].keys()
        # lport.sort()

        for port in lport:
            print('port : %s\tstate : %s' % (port, nmScan[host][proto][port]['state']))

