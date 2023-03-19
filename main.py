import requests
from bs4 import BeautifulSoup

URL = "https://www.amazon.com/Autom-Trinket-Tray-Banana-Shaped/dp/B08DVCLKFK/ref=sr_1_2?crid=CL7H2UL2Q9IS&keywords=banana+trinket&qid=1679212807&sr=8-2"

res = requests.get(URL)

if res.status_code == 200:
  soup = BeautifulSoup(res.text, features="html.parser")
  info = soup.find_all("a", {"href":"/currencies/bitcoin/markets/"})
  price = info[0].getText()
  print("bitcoin -", price)
 
  
  

