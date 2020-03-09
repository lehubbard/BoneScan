from SSHComs import SSHComs
from getpass import getpass
from CVECheck import CVECheck
from report import reportGen
import argparse

#parse software info
def ParseSoft (raw):
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

    return args.ip, args.user

def main():
    ip, user = parser()
    password = getpass("Enter your BeagleBoard's password: ")

    com = SSHComs(ip, user, password)
    com.In('dpkg --list')

    software = com.Out
    software = ParseSoft(software)
    vulnSoft = []

    for line in software:
        print ('Scanning', line[0], line[1])
        cve = CVECheck(line[0], line[1])
        if len(cve.IDList) > 0:
            vulnSoft.append([line[0], line[1], str(cve.IDList)])

    re = reportGen(vulnSoft)
    re.write()

if __name__ == '__main__':
    main()




















#
