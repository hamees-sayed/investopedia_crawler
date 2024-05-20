import requests
from bs4 import BeautifulSoup

url = "https://www.investopedia.com/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
url = {}
print(soup.find_all("ul", class_="header-nav__list"))

