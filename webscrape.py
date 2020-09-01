from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.daft.ie/ireland/residential-property-for-rent/?ad_type=rental&advanced=1&s%5Bmxp%5D=1700&s%5Bmxb%5D=2&s%5Badvanced%5D=1&s%5Bfurn%5D=1&searchSource=rental'
#opening connection, grabbing the page
uclient = ureq(my_url)
page_html = uclient.read()
uclient.close()
#html parsing
page_soup = soup(page_html, "html.parser")
page_soup.body.span

containers = page_soup.findAll("div",{"class":"PropertyImage__mainImageContainer"})
len(containers)

#building the scraper
contain = containers[0]
container = containers[0]
container.text

#create csv
filename = "rent.csv"
f = open(filename, "w")

headers = "address, price\n"

f.write(headers)

for container in containers: 
    address = container.div.div.div.a.text
    
    price = container.findAll("div",{"class":"PropertyInformationCommonStyles__costAmountCopySmall"})
    apt_price = price[0].text
    
    print("address: " + address)
    print("apt_price: " + apt_price)

    f.write(address.replace(",", "-") + "," + apt_price.replace(",", "-") + "\n")

f.close()
