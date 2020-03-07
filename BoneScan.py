from SSHComs import SSHComs
from getpass import getpass
"""
ip = input('Enter ip: ')
user = input('Enter username: ')
password = getpass()
"""

ip = '192.168.1.35'
user = 'lucas'
password = 'P@ssw0rd'
com = SSHComs(ip, user, password)
com.connect('dpkg --list')
print(com.out)
