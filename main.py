import requests
import json
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup

load_dotenv()
BASE_URL = os.getenv('BASE_URL')
data_arr = os.getenv('ROUNDS')
ROUNDS = json.loads(data_arr)

res = requests.get(BASE_URL+ROUNDS[1])
soup = BeautifulSoup(res.text, 'html.parser')
table_rates = soup.find('div', {'id': 'rates_block'}).find_all('tr')
price = table_rates[1].find('td', class_='bi').find('div', class_='fs').text
# print(table_rates[0])
print(price)
