from SSHComs import SSHComs
from CVECheck import CVECheck
from report import report
from mdnsDiscover import mdnsDiscover
import argparse
from distutils.util import strtobool
import os

def parser():
    parser = argparse.ArgumentParser(description='Scan for potential vulnerabilities on a BeagleBoard')
    parser.add_argument('-u', action = 'store', help = 'Username, Deafult = debian', dest = 'user', default = 'debian')
    parser.add_argument('--cve', action="store_true", help = 'Scans installed software for known vulnerabilities')
    parser.add_argument('--ip', action="store_true", help = 'Enter an IP address manually')
    return parser

#parse software info
def ParseSoft (raw):
    raw = raw.replace("\\n", '\n')
    raw = raw.replace('~', "-")
    raw = raw.replace(':', "-")
    raw = raw.replace('+', "-")
    rawLst = raw.split('\n')
    for i in range(len(rawLst)):
        if '===' in rawLst[i]:
            rawLst = rawLst[(i+1):]
            break
    soft = []
    for line in rawLst:
        line = line.split()
        line = line[1:3]
        soft.append(line)
    soft = soft[:-1]
    return soft

def netstatParse(raw):
    raw = raw.replace("\\n", '\n')
    portLst = raw.split('\n')
    portLst = portLst[2:-1]
    listening = []
    for i in range(len(portLst)):
        portLst[i] = portLst[i].split()
    for port in portLst:
        port[3] = port[3].replace('0.0.0.0:', '')
        port[3] = port[3].replace(':::', '')
        listening.append([port[0], port[3]])
    return listening



def checkForVulnSoft(software):
    software = ParseSoft(software)
    vulnSoft = []

    # #!!!!!!!!!!!!!! remove this before submission !!!!!!!!!!
    # for i in range(15):
    #     print ('Scanning', software[i][0], software[i][1])
    #     cve = CVECheck(software[i][0], software[i][1])
    #     if len(cve.IDList) > 0:
    #         vulnSoft.append([software[i][0], software[i][1], str(cve.IDList)])
    for line in software:
        print ('Scanning', line[0], line[1])
        cve = CVECheck(line[0], line[1])
        if len(cve.IDList) > 0:
            vulnSoft.append([line[0], line[1], str(cve.IDList)])
    return vulnSoft

def writeReport(reports):
    report = reports[0].head
    for i in range(len(reports)):
        reports[i].makeBody()
        report = report + reports[i].body
    report = report + reports[0].foot

    file = open(reports[0].getFileName(), 'a')
    file.write(report)
    file.close()

    print('\nReport written to ', os.getcwd(), '/report', reports[0].getFileName(), sep = '')

def main():
    parsed = parser()
    args = parsed.parse_args()
    user = args.user

    if args.ip:
        ipLst = getIP()
    else:
        try:
            discover = mdnsDiscover()
            ipLst = discover.getIPAddr()
        except:
            choice = input('No BeagleBoards were found. \nWould you like to enter an IP address manually? (yes or no) ')
            choice = strtobool(choice)
            if choice:
                ipLst = getIP()
            else:
                quit()

    reports = []
    for i in range(len(ipLst)):
        ip = ipLst[i]
        com = SSHComs(ip, user)
        re = report(ipLst[i])
        reports.append(re)
        print('Scanning device', (i+1), 'of', len(ipLst), '\n')

        if com.defPass:
            reports[i].isPassDef()
        if com.passEnabled:
            reports[i].isPassEnabled()
        software = com.In('dpkg --list')

        services = ['nginx', 'cloud9.socket', 'nodered.socket', 'bonescript.socket', 'bonescript-autorun', 'hostapd', 'bb-bbai-tether']
        enabledServices = []
        for serv in services:
            service = com.In(f'systemctl is-enabled {serv}')
            if service.find('enabled') > -1:
                enabledServices.append(serv)
                reports[i].disServices(enabledServices)

        netstatData = com.In('netstat -lntu')
        listening = netstatParse(netstatData)
        if len(listening) > 0:
            reports[i].listeningPorts(listening)

        if args.cve:
            vulnSoft = checkForVulnSoft(software)
            reports[i].vulnSoft(vulnSoft)

        com.endSession()
    writeReport(reports)
if __name__ == '__main__':
    main()




















#
