#!usr/bin/evn python
#Integrating nmap

import nmap
import optparse

# defining nmap scan function with arguments
# TargetHost will hold the host value and TargetHost will hold the port value
def nmapScan(TargetHost, TargetHost):
    nmscan = nmap.PortScanner()
    nmscan.scan(TargetHost, TargetPort)
    state = nmscan[TargetHost]['tcp'][int(TargetPort)]['state']
    print(" [*] " + TargetHost + " tcp/"+ TargetPort + " "+state)

def main():
    # printing Help to inform How to use this script
    parser = optparse.OptionParser('Script Usage:'+'-H <target host> -p <target port>')
    
    parser.add_option('-H', dest='TargetHost', type='string', 
    help='specify target host')

    parser.add_option('-P', dest='TargetPort', type='string', 
    help='specify target port[s] separated by comma')

    (options,args) = parser.parse_args()
    TargetHost = options.TargetHost
    TargetPort = str(options.TargetPort)
    
    print(TargetPort)
    
    if (TargetHost == None) | (TargetPort[0] == None):
        print(parser.usage)
        exit(0)
        
    ports = TargetPort.strip("'").split(',')
    
    for TargetPort in ports:
        print(TargetHost+ " " + TargetPort)
        nmapScan(TargetHost, TargetPort)

if __name__ == '__main__':
        main()