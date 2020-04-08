from getpass import getpass
import spur
import spur.ssh
from distutils.util import strtobool
import traceback

class SSHComs:

    def __init__(self, ip, user):
        self.ip = ip
        self.user = user
        self.passEnabled = False
        self.defPass = self.isPassDefault()
        print('Establishing connection to ', self.user, '@', self.ip, sep='')
        self.login('key')

    def login(self, opt):
        if opt == 'key':
            self.shell = spur.SshShell(hostname = self.ip, username = self.user)
        elif opt == 'pass':
            self.password = getpass("\nEnter your BeagleBoard's password: ")
            self.shell = spur.SshShell(hostname = self.ip, username = self.user, password = self.password)
            self.passEnabled = True
        else:
             raise Exception('Bad input')

    def isPassDefault(self):
        self.shell = spur.SshShell(hostname = self.ip, username = self.user, password = 'temppwd')
        if self.checkConnection():
            return True
            self.endSession()
        else:
            return False

    def checkConnection(self):
        try:
            connected = self.shell.run(['pwd'])
            return True
        except:
            #traceback.print_exc()
            return False

    def choose(self, message):
        choice = input(message)
        choice = strtobool(choice)
        if choice:
            return choice
        else:
            quit()

    def In(self, command):
        connected = self.checkConnection()
        while not connected:
            choice = self.choose('Login failed. \nWould you like to enter a password? (yes or no) ')
            self.login('pass')
            connected = self.checkConnection()


        #parse and run command
        command = command.split()
        if len(command) > 1:
            result = self.shell.run([command[0], command[1]])
        else:
            result = self.shell.run([command[0]])

        return str(result.output)

    def endSession(self):
        self.shell.close()
