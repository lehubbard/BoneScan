import socket
from ssh2.session import Session
from getpass import getpass


class SSHComs:

    def __init__(self, ip, user, password):
        self.ip = ip
        self.user = user
        self.password = password

    def In(self, command):
        print('Establishing connection to ', self.user, '@', self.ip, sep='')
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((self.ip, 22))

        session = Session()
        session.handshake(sock)
        session.userauth_password(self.user, self.password)

        channel = session.open_session()
        channel.execute(command)
        size, data = channel.read()
        self.Out = ''
        while size > 0:
            self.Out += data.decode()
            size, data = channel.read()

        channel.close()
        print("Exiting with Status: {0}".format(channel.get_exit_status()))
        print()
