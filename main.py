import requests
import json
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv()
BASE_URL = os.getenv('BASE_URL')
data_arr = os.getenv('ROUNDS')
ROUNDS = json.loads(data_arr)

print(ROUNDS)

res = requests.get(BASE_URL+ROUNDS[0])

print(res)