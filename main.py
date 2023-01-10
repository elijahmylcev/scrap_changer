import requests
import json
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup

load_dotenv()
BASE_URL = os.getenv('BASE_URL')
data_arr = os.getenv('ROUNDS')
ROUNDS = json.loads(data_arr)

res = requests.get(BASE_URL+ROUNDS[0])
soup = BeautifulSoup(res.text, 'html.parser')
table_rates = soup.find('div', {'id': 'rates_block'}).find_all('tr')
price_out = table_rates[1].findAll('td', class_='bi')[0].text
price_income = table_rates[1].findAll('td', class_='bi')[1].text
print(price_out)
print(price_income)
