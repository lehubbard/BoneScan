from SSHComs import SSHComs
from getpass import getpass
from CVECheck import CVECheck
import re
"""
ip = input('Enter ip: ')
user = input('Enter username: ')
password = getpass()
cve = CVECheck('windows_10', '1511')
"""
ip = '192.168.1.35'
user = 'lucas'
password = 'P@ssw0rd'
com = SSHComs(ip, user, password)
com.In('dpkg --list')

software = com.Out
pattern = re.compile(r'\b')
matches = pattern.finditer(software)
for match in matches:
    print(match)
