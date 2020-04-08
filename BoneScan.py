from SSHComs import SSHComs
from CVECheck import CVECheck
from report import report
from mdnsDiscover import mdnsDiscover
import argparse
from distutils.util import strtobool

def parser():
    parser = argparse.ArgumentParser(description='Scan for potential vulnerabilities on a BeagleBoard')
    parser.add_argument('-i', action = 'store', help = 'IP address of machine to be scanned', dest = 'ip')
    parser.add_argument('-u', action = 'store', help = 'Account Username', dest = 'user')
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

def getIP():
    ipLst = input('Enter the IP addresses of the devices you would like scanned seperated by a space. ')
    ipLst = ipLst.split()
    return ipLst

def parser():
    parser = argparse.ArgumentParser(description='Scan for potential vulnerabilities on a BeagleBoard')
    parser.add_argument('-i', action = 'store', help = 'IP address of machine to be scanned', dest = 'ip')
    parser.add_argument('-u', action = 'store', help = 'Account Username', dest = 'user')
    parser.add_argument('--cve', action="store_true", help = 'Scans installed software for known vulnerabilities')
    parser.add_argument('--ip', action="store_true", help = 'Enter an IP address manually')
    return parser

def checkForVulnSoft(software):
    software = ParseSoft(software)
    vulnSoft = []

    # !!!!!!!!!!!!!! remove this before submission !!!!!!!!!!
    # for i in range(3):
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

    for i in range(len(ipLst)):
        ip = ipLst[i]
        com = SSHComs(ip, user)
        re = report(ipLst)

        if com.defPass:
            pass
        if com.passEnabled:
            pass
        software = com.In('dpkg --list')
        print('Scanning device', (i+1), 'of', len(ipLst), '\n')

        if args.cve:
            vulnSoft = checkForVulnSoft(software)
            re.vulnSoft(vulnSoft)

        re.write()
if __name__ == '__main__':
    main()




















#
