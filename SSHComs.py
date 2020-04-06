import socket
from ssh2.session import Session
from getpass import getpass
from pathlib import Path
import spur
import spur.ssh

class SSHComs:

    def __init__(self, ip, user):
        self.ip = ip
        self.user = user

    def In(self, command, opt):
        print('Establishing connection to ', self.user, '@', self.ip, sep='')
        # sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # sock.connect((self.ip, 22))
        #
        # session = Session()
        # session.handshake(sock)
        # path = str(Path.home()) + '/.ssh/id_ed25519.pub'
        # f = open(path, 'r')
        # print(f)
        # # pKey = open(path, 'rb')
        # # pKeyBytes = pKey.read()
        # session.userauth_publickey_fromfile(self.user, path)
        #
        #
        #
        # #session.userauth_password(self.user, self.password)
        #
        # channel = session.open_session()
        # channel.execute(command)
        # size, data = channel.read()
        # self.Out = ''
        # while size > 0:
        #     self.Out += data.decode()
        #     size, data = channel.read()
        #
        # channel.close()
        # print("Exiting with Status: {0}".format(channel.get_exit_status()))
        # print()
        path = str(Path.home()) + '/.ssh/id_ed25519.pub'
        shell = spur.SshShell(hostname = self.ip, username = self.user, private_key_file = path)

        result = shell.run([command, opt])
        self.out = result.output
        shell.close()
