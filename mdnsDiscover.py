import socket
import signal

class mdnsDiscover:
    def __init__(self):
        self.domain = 'beaglebone'
        self.tld = '.local'
    def timeout(signum, frame):
        pass

    signal.signal(signal.SIGALRM, timeout)
    signal.alarm(1)

    def getIPAddr(self):
        ipAddr = []
        #find ip address of first BeagleBoard
        try:
            ip = socket.gethostbyname(str(self.domain + self.tld))
            ipAddr.append(ip)
        except OSError:
            raise Exception('No Beagleboards found')

        #find ip address if BeagleBoards with suffix is present
        count = 2
        while True:
            try:
                searchName = self.domain + '-' + str(count)
                count = count + 1
                ip = socket.gethostbyname(str(searchName + self.tld))
                ipAddr.append(ip)
            except OSError:
                return(ipAddr)
