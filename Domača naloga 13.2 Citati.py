from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup

url = "https://quotes.yourdictionary.com/theme/marriage/"
response = urlopen(url).read()
soup = BeautifulSoup(response)

for p in soup.find("p"):
    quotes1 = soup.find("p", attrs={"id": "85960"}).string
    quotes2 = soup.find("p", attrs={"id": "616667"}).string
    quotes3 = soup.find("p", attrs={"id": "612269"}).string
    quotes4 = soup.find("p", attrs={"id": "624813"}).string
    quotes5 = soup.find("p", attrs={"id": "617875"}).string
    print quotes1
    print quotes2
    print quotes3
    print quotes4
    print quotes5