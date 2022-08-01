import requests
from bs4 import BeautifulSoup
import re

filt = re.compile('Digitama.+\.jpg')
filt_2 = re.compile('(?<=_).+?(?=\.jpg)')

url = 'https://wikimon.net/Digitama'
req = requests.get(url)
bs = BeautifulSoup(req.text,'lxml')

data = bs.find('table',attrs={'border':1})
data = bs.find_all('img',attrs={'alt':filt})
print(len(data))
for d in data:
    d = 'https://wikimon.net' + d['src']
    c = filt_2.search(d).group()
    
    image_res = requests.get(d)
    image_res.raise_for_status()
    
    with open(r'C:\Users\a\Desktop\제비\asset\{}.jpg'.format(c), 'wb') as f:
        f.write(image_res.content)