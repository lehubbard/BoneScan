import datetime
import os

class report:
    def __init__ (self):
        self.vulnPresent = False
        self.date = datetime.datetime.now()
        self.create()


    def create(self):
        self.html = f"""<!doctype self.html>
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

        if self.vulnPresent:
            self.html = self.html + self.vuln

        if not self.vulnPresent:
            message = '<h3>Congratulations, no vulnerabilities were found!</h3>'
            self.html = self.html + message

        self.html = self.html + '</div>\n</body>'

    def vulnSoft(self, vuln):
        self.vuln = vuln
        if len(self.vuln) > 0:
            self.vulnPresent = True

        head = '<h3>{len(self.vuln)} potential vulnerabilities found</h3>\n'
        #format vulnerable software list
        for line in self.vuln:
            line[2] = line[2].replace('[', '')
            line[2] = line[2].replace(']', '')
            line[2] = line[2].replace('"', '')
            line[2] = line[2].replace("'", '')
            self.vuln = head + '\t\t<p>' + line[0] + ' ' + line[1] + ': ' + line[2] + '</p>\n'


    def write(self):
        self.filename = 'report-' + str(self.date)
        self.filename = self.filename.replace(' ', '-')
        self.filename = self.filename.replace('.', '-')
        self.filename = self.filename.replace(':', '-')
        self.filename = './report/' + self.filename + '.html'

        file = open(self.filename, 'a')
        file.write(self.html)
        file.close()

        print('\nReport written to ', os.getcwd(), '/report', self.filename, sep = '')
