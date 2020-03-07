import json
import requests

class CVECheck:
    def __init__(self, name, ver):
        self.name = name
        self.ver = ver
    def lookup(self):
        url = f'https://services.nvd.nist.gov/rest/json/cves/1.0?cpeMatchString=cpe:2.3:*:*:{self.name}:{self.ver}'
        print(url)
        r = requests.get(url)
        data = r.json()

        data = json.dumps(data['totalResults'], indent=2)
        return data

cve = CVECheck('Java', '1.6.2')
#cve = CVECheck('windows_10', '1511')
print (cve.lookup())
