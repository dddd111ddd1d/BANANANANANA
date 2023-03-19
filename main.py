import requests 
from bs4 import BeautifulSoup

URL = "https://www.python.org/"

res = requests.get(URL)

print(res.text)

if res.status_code == 200:
  soup = BeautifulSoup(res.text, feauture=)
  