import requests
import json
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup

def broke_round(base_url, obj_round):
  for key in obj_round:
    res = requests.get(base_url+obj_round[key])
    soup = BeautifulSoup(res.text, 'html.parser')
    table_rates = soup.find('div', {'id': 'rates_block'}).find_all('tr')
    price_out = table_rates[1].findAll('td', class_='bi')[0].text
    price_income = table_rates[1].findAll('td', class_='bi')[1].text
    print(price_out)
    print(price_income)

if __name__ == "__main__":
  load_dotenv()
  BASE_URL = os.getenv('BASE_URL')
  data_obj = os.getenv('ROUNDS')
  ROUNDS = json.loads(data_obj)
  broke_round(BASE_URL, ROUNDS)
  