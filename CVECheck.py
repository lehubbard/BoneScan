import json
import requests

class CVECheck:
    def __init__(self, name, ver):
        self.name = name
        self.ver = ver
        url = f'https://services.nvd.nist.gov/rest/json/cves/1.0?cpeMatchString=cpe:2.3:*:*:{self.name}:{self.ver}'
        r = requests.get(url)
        data = r.json()
        self.totalResults = int(json.dumps(data['totalResults']))
        self.IDList = []
        if self.totalResults > 0 and self.totalResults < 21:
            self.url = f'https://services.nvd.nist.gov/rest/json/cves/1.0?cpeMatchString=cpe:2.3:*:*:{self.name}:{self.ver}&resultsPerPage={self.totalResults}'
            r = requests.get(url)
            data = r.json()
            for i in range(self.totalResults):
                self.IDList.append(json.dumps(data['result']['CVE_Items'][i]['cve']['CVE_data_meta']['ID']))
