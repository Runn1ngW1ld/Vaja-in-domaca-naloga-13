from BeautifulSoup import BeautifulSoup
from urllib2 import urlopen


#csv_file = open("email_list.csv", "w")


url = 'https://scrapebook22.appspot.com/'
response = urlopen(url).read()
soup = BeautifulSoup(response)

print soup.html.head.title.string


csv_file = open("email_list.csv", "w")

for link in soup.findAll("a"):
    if link.string == "See full profile":
        persons_url = 'https://scrapebook22.appspot.com/' + link["href"]
        persons_html = urlopen(persons_url).read()
        persons_soup = BeautifulSoup(persons_html)
        email = persons_soup.find("span", attrs={"class": "email"}).string
        name = persons_soup.find("div", attrs={"class": "col-md-8"}).find("h1").string
        city = persons_soup.find("span", attrs={"data-city": True}).string
        print name
        print email
        print city
        csv_file.write(name + "," + email + "," + city + "\n")
csv_file.close()

