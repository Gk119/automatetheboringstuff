import requests
from requests.models import HTTPError
import bs4
link = input("Enter the link: ")

res = requests.get(link)

bs = bs4.BeautifulSoup(res.text,'html.parser')
for elem in bs.select('a[href]'):
    inlink = elem["href"]
    if(inlink.startswith('http')):
        inlinkpage = requests.get(inlink)
        if inlinkpage.status_code == 404:
            print(inlink)
        

#if res.status_code == 404:
#    print("Error 404: Link not Found!")
