import requests
import re

url = 'http://ccinfo.wdcm.org/search/basic/'
myobj = {'query': 'CLIP'}

x = requests.post(url, data = myobj)

m = re.findall(r'Total ([0-9]+) results.', x.text)
print(int(m[0]))
