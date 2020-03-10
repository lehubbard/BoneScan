import datetime

class reportGen:
    def __init__ (self, vuln):
        self.date = datetime.datetime.now()
        self.vuln = vuln

    def write(self):
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

          <div class="results">
            <h3>{len(self.vuln)} potential vulnerabilities found</h3>\n"""

        for line in self.vuln:
            line[2] = line[2].replace('[', '')
            line[2] = line[2].replace(']', '')
            line[2] = line[2].replace('"', '')
            line[2] = line[2].replace("'", '')
            self.html = self.html + '\t\t<p>' + line[0] + ' ' + line[1] + ': ' + line[2] + '</p>\n'

        self.html = self.html + """  </div>
        </body>
        </self.html>
                """
        self.filename = 'report-' + str(self.date)
        self.filename = self.filename.replace(' ', '-')
        self.filename = self.filename.replace('.', '-')
        self.filename = self.filename.replace(':', '-')
        self.filename = './report/' + self.filename + '.html'

        file = open(self.filename, 'a')
        file.write(self.html)
        file.close()
