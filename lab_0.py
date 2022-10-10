'''
CIS41B
Lab 0 drafting
'''

from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
from collections import defaultdict
import numpy as np

url = 'https://en.wikipedia.org/wiki/List_of_countries_by_carbon_dioxide_emissions_per_capita'
html = urlopen(url)
soup = BeautifulSoup(html, 'html.parser')
#print(soup)

rows = []
data = []
table = soup.select('table')[1]
# print(table)
for tbody in table.find_all('tbody'):
    # print(tbody)
    for tr in tbody.find_all('tr'):
        row = str(tr.text.strip())
        rows.append(row)
    #print(rows)
    # for tr in tbody.find_all('tr'):
        # row = list(str(tbody.find_all('tr').text.strip()))
    #print(row)

    for td in table.find_all('td'):
        #print(str(td))
        text = str(td.text.strip())
        data.append(text)
    # print(data)
    elem15 = [data[x:x+15] for x in range(0, len(data), 15)]
    # print(elem15)

# print(emissions)
    
    #td = tbody.find_all('td')[0].text.strip()
    #print(td)

# print(elem15[0][0])

def defaultDict():
    dd = defaultdict(list)
    #dd[elem15[0][0]].append(elem15[0][1])
    #dd[elem15[0][0]].append(elem15[0][14])

    for i in range(len(elem15)):
        #print(i)
        try:
            dd[elem15[i][0]].append(float(elem15[i][1]))
            dd[elem15[i][0]].append(float(elem15[i][14]))
        except:
            if elem15[i][1] == '..':
                dd[elem15[i][0]].append(float(0))
            else:
                dd[elem15[i][0]].append(float(elem15[i][1]))
            if elem15[i][14] == '..':
                dd[elem15[i][0]].append(float(0))
            else:
                dd[elem15[i][0]].append(float(elem15[i][14]))
        for k,v in dd.items():
            #print(k,v)
            emissionDiff = float('{:.1f}'.format(v[1]-v[0]))
            #print(emissionDiff)

        dd[elem15[i][0]].append(emissionDiff)
    
   # print(list(dd[0]))
    #for i in range(len(dd)):
        #print(dd[i])
   
        ddSorted = sorted(dd.items(), key =lambda k_v: k_v[1][1], reverse = True)
    #print(ddSorted)
        ddSorted10 = list(ddSorted[:10])
    print(ddSorted10)
    
                               
        #emissionDiff = '{:.1f}'.format((ddSorted10[i][1][1]) - (ddSorted10[i][1][0]))
        #print(emissionDiff)
        #print(list(ddSorted10[i]))
        #asList = list(ddSorted10[i]).append(emissionDiff)
    #print(asList)
    #print(dd)    
    
                                
defaultDict()        
    
