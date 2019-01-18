from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup
import random
url = "https://quotes.yourdictionary.com/theme/marriage/"
response = urlopen(url).read()
soup = BeautifulSoup(response)


quotes = soup.findAll("div", attrs={"class": "QuotesAndNotes"})
list_of_quotes = []

for p in quotes:
    quotes1 = p.find("p").string
    list_of_quotes.append(quotes1)

print random.sample(list_of_quotes, 5)




