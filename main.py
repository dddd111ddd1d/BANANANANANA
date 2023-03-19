import requests
from bs4 import BeautifulSoup

URL = "https://www.amazon.com/Razer-Huntsman-Mini-Gaming-Keyboard/dp/B08B3MHYPC/ref=sr_1_16?crid=2CP4WCWO2D6PC&keywords=gaming+keyboard&qid=1679213039&sprefix=gaming+ceyboard%2Caps%2C238&sr=8-16"

res = requests.get(URL)

if res.status_code == 200:
  soup = BeautifulSoup(res.text, features="html.parser")
  info = soup.find_all("span", {"class":"a-price a-text-price a-size-medium apexPriceToPay"})
  price = info[0].getText()
  print("klava -", price)
 
  
  

