import requests
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
BASE_URL = os.getenv('BASE_URL')
print(BASE_URL)

# res = requests.get(URL)