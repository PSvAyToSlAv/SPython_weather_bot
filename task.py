import requests
from bs4 import BeautifulSoup

pog = 'https://world-weather.ru/pogoda/russia/saransk/'

r = requests.get(pog)

soup = BeautifulSoup(r.text, 'html.parser')

for temp in soup.find_all('div', id = 'weather-now-number'):
    temp = temp.text

for obl in soup.find_all('span', id = 'weather-now-icon'):
    obl = obl.get('title')

for timew in soup.find_all('div', class_ = 'weather-now-info'):
    timew = timew.text[6:-3]

for dr in soup.find_all('div', id= 'weather-now-description'):
    line = dr.text

    last_index=0

    itog = []

    for i, char in enumerate(line[1:-9]):
        if char.istitle() or i== len(line[1:-10]): 
            itog.append(line[last_index: i + 1])
            last_index=1+1 
    itog.append(line[-10:-4])
    itog.append(line[-4:])
    dr.join(itog[:-5])

print("погода в саранске:" +  '\n' + temp + ' ' + obl + '\n' + dr + '\n', 'данные на', timew)

