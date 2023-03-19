import requests
from bs4 import BeautifulSoup

URL = "https://coinmarketcap.com/"

res = requests.get(URL)

if res.status_code == 200:
  soup = BeautifulSoup(res.text, features="html.parser")
  info = soup.find_all("a", {"href":"/currencies/ethereum/markets/"})
  price = info[0].getText()
  print("ethereum -", price)
  info2 = soup.find_all("a", {"href":"/currencies/bitcoin/markets/"})
  price = info2[0].getText()
  print("bitcoin -", price)
  info3 = soup.find_all("a", {"href":"/currencies/tether/markets/"})
  price = info3[0].getText()
  print("tether -", price)
  info4 = soup.find_all("a", {"href":"/currencies/bnb/markets/"})
  price = info4[0].getText()
  print("bnb -", price)
 
  
  

