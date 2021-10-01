import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.in/Samsung-Galaxy-Ocean-128GB-Storage/dp/B07HGGYWL6'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find(id='productTitle').get_text()

price = soup.find(id='priceblock_ourprice').get_text()

converted_price = float(price[2:4])

print(title.strip())

print(price)

print(converted_price)


# i have no idea what this is supposed to do, duh... need some iprovisation.. will do in 2 weeks
