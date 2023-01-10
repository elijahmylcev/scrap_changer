import requests
import json
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import re

def find_price(string):
  match = re.search(r'\d+\.\d+', string)
  if match:
    number = match.group()
    return number

def broke_round(base_url, obj_round):
  result = {}
  for key in obj_round:
    res = requests.get(base_url+obj_round[key])
    soup = BeautifulSoup(res.text, 'html.parser')
    table_rates = soup.find('div', {'id': 'rates_block'}).find_all('tr')
    price_out = table_rates[1].findAll('td', class_='bi')[0].text
    price_income = table_rates[1].findAll('td', class_='bi')[1].text
    if key=='buy':
      result[key] = find_price(price_out)
    elif key=='sale':
      result[key] = find_price(price_income)
  if all(result.values()):
    return round(float(result['sale']) / float(result['buy']), 2)
  else:
    return None

if __name__ == "__main__":
  load_dotenv()
  BASE_URL = os.getenv('BASE_URL')
  data_obj = os.getenv('ROUNDS') # Строка
  ROUNDS = json.loads(data_obj)
  print(broke_round(BASE_URL, ROUNDS))
  