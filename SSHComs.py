import socket
from ssh2.session import Session
from getpass import getpass


class SSHComs:

    def __init__(self, ip, user, password):
        self.ip = ip
        self.user = user
        self.password = password

    def connect(self, command):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((self.ip, 22))

        session = Session()
        session.handshake(sock)
        session.userauth_password(self.user, self.password)

        channel = session.open_session()
        channel.execute(command)
        size, data = channel.read()
        self.out = ''
        while size > 0:
            self.out += data.decode()
            size, data = channel.read()
        
        channel.close()
        print("Exit Status: {0}".format(channel.get_exit_status()))

ip = '192.168.1.35'
user = 'lucas'
password = 'P@ssw0rd'

com = SSHComs(ip, user, password)
com.connect('dpkg --list')
