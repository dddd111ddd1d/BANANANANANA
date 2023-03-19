import requests
from bs4 import BeautifulSoup

URL = "https://www.olx.ua/d/uk/obyavlenie/groviy-pk-i5-gtx660-12gb-ram-ssd-hdd-IDRmIKz.html"

res = requests.get(URL)

if res.status_code == 200:
  soup = BeautifulSoup(res.text, features="html.parser")
  product_name = soup.find_all("h1", {"class":"css-1soizd2 er34gjf0"})
  product_price = soup.find_all("h3", {"class":"css-ddweki er34gjf0"})
  price = product_price[0].getText()
  productName = product_name[0].getText()
  print(productName, "-", price)

 
  
  

