from SSHComs import SSHComs
from CVECheck import CVECheck
from report import report
from mdnsDiscover import mdnsDiscover
import argparse
from distutils.util import strtobool

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

def parser():
    parser = argparse.ArgumentParser(description='Scan for potential vulnerabilities on a BeagleBoard')
    parser.add_argument('-i', action = 'store', help = 'IP address of machine to be scanned', dest = 'ip')
    parser.add_argument('-u', action = 'store', help = 'Account Username', dest = 'user')
    args = parser.parse_args()

    return args.user

def checkForVulnSoft(software):
    software = ParseSoft(software)
    vulnSoft = []

    for i in range(3):
        print ('Scanning', software[i][0], software[i][1])
        cve = CVECheck(software[i][0], software[i][1])
        if len(cve.IDList) > 0:
            vulnSoft.append([software[i][0], software[i][1], str(cve.IDList)])
    # for line in software:
    #     print ('Scanning', line[0], line[1])
    #     cve = CVECheck(line[0], line[1])
    #     if len(cve.IDList) > 0:
    #         vulnSoft.append([line[0], line[1], str(cve.IDList)])

    re = report()
    re.vulnSoft(vulnSoft)
    re.write()

def main():
    user = parser()
    try:
        discover = mdnsDiscover()
        ipLst = discover.getIPAddr()
    except:
        choice = input('No BeagleBoards were found. \nWould you like to enter an IP address manually? (yes or no) ')
        choice = strtobool(choice)
        if choice:
            ipLst = input('Enter the IP addresses of the devices you would like scanned seperated by a space. ')
            ipLst = ipLst.split()
        else:
            quit()

    for i in range(len(ipLst)):
        ip = ipLst[i]
        com = SSHComs(ip, user)
        if com.passEnabled:
            pass
        software = com.In('dpkg --list')
        print('Scanning device', (i+1), 'of', len(ipLst), '\n')






        checkForVulnSoft(software)

if __name__ == '__main__':
    main()




















#
