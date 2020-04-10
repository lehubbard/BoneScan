import datetime
import os

class report:
    def __init__ (self, ip):
        self.ip = ip
        self.vulnPresent = False
        self.servicesPresent = False
        self.defPass = False
        self.passEnabled = False
        self.listeningPortsPresent = False
        self.date = datetime.datetime.now()
        self.head = f"""<!doctype self.html>
        <self.html lang="en">
        <head>
          <meta charset="utf-8">
          <title>Bone Scan Report</title>
          <link rel="stylesheet" href="./style.css">
        </head>

        <body>
          <div class="header">
            <img id="logo" src="logo.png">

            <div class="htext">
              <h1>Bonescan Report</h1>
              <h2>({self.date})</h2>
            </div>
          </div>

          <div class="results"> """
        self.foot = '<a href="https://beagleboard.org/ai/aws">For more information on securing your BeagleBoard, click here</a>\n</div>\n</body>'

    def makeBody(self):
        self.body = '\n<h2> BeagleBoard at ' + self.ip + '</h2>\n'

        if self.defPass:
            self.body = self.body + '<h3>The default password is enabled</h3>\n'

        if self.passEnabled:
            self.body = self.body + '<h3>Password login over SSH is enabled</h3>\n'

        if self.servicesPresent:
            self.body = self.body + self.services

        if self.listeningPortsPresent:
            self.body = self.body + self.portsOut

        if self.vulnPresent:
            self.body = self.body + self.vulnOut

        if not self.vulnPresent and not self.defPass and not self.servicesPresent and not self.passEnabled:
            message = '<h3>Congratulations, no vulnerabilities were found!</h3>'
            self.body = self.body + message

    def vulnSoft(self, vuln):
        self.vuln = vuln
        if len(self.vuln) > 0:
            self.vulnPresent = True

        self.vulnOut = '<h3>' + str(len(self.vuln)) + ' potential vulnerabilities found</h3>\n<ul>'
        #format vulnerable software list
        for line in self.vuln:
            line[2] = line[2].replace('[', '')
            line[2] = line[2].replace(']', '')
            line[2] = line[2].replace('"', '')
            line[2] = line[2].replace("'", '')
            print(line[2])
            self.vulnOut = self.vulnOut + '\t\t<li>' + line[0] + ' ' + line[1] + ': ' + line[2] + '</li>\n'
        self.vulnOut = self.vulnOut + '</ul>'


    def disServices(self, services):
        if len(services) > 1:
            self.servicesPresent = True
        self.services = '<h3>If unused, the following services should be disabled:</h3> \n<ul>'
        for i in range(len(services)):
            self.services = self.services + '<li>' + services[i] + '</li>' + '\n'
        self.services = self.services + '</ul>'

    def isPassDef(self):
        self.defPass = True

    def isPassEnabled(self):
        self.passEnabled = True

    def listeningPorts(self, listening):
        self.listeningPortsPresent = True
        self.portsOut = '<h3>The following ports are in a listening state</h3>\n<ul>'
        for i in range(len(listening)):
            port = str(listening[i])
            port = port.replace('[', '')
            port = port.replace(']', '')
            port = port.replace('"', '')
            port = port.replace("'", '')
            port = port.replace(",", ':')
            self.portsOut = self.portsOut + f'<li>{port}</li>\n'
        self.portsOut = self.portsOut + '</ul>'


    def getFileName(self):
        self.filename = 'report-' + str(self.date)
        self.filename = self.filename.replace(' ', '-')
        self.filename = self.filename.replace('.', '-')
        self.filename = self.filename.replace(':', '-')
        self.filename = './report/' + self.filename + '.html'
        return self.filename
