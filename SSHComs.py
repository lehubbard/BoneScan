import socket
from ssh2.session import Session

class SSHComs:

    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password

    def connect(self, command):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((self.host, 22))

        session = Session()
        session.handshake(sock)
        session.userauth_password(self.user, self.password)

        channel = session.open_session()
        channel.execute(command)
        size, data = channel.read()
        while size > 0:
            print(data.decode())
            size, data = channel.read()
        channel.close()
        print("Exit Status: {0}".format(channel.get_exit_status()))

host = input('Enter IP: ')
user = input('Enter username: ')
password = input('Enter password: ')

com = SSHComs(host, user, password)
com.connect('dpkg --list')
