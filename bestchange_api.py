import requests
import zipfile
import io
import os
import pandas as pd
import numpy as np
from dotenv import load_dotenv
import csv


load_dotenv()
URL_API = os.getenv('URL_API')

def getData(URL):
  result = requests.get(URL, stream=True)
  z = zipfile.ZipFile(io.BytesIO(result.content))
  z.extractall("./currency")
  
def create_info_table(path):
  columns = {0: 'id_currency', 2: 'name_currency', 3:'short_name'}

  df = pd.read_csv(path, delimiter=';', encoding='windows-1251', header=None)
  df = df[df.columns[[0, 2, 3]]]
  df = df.rename(columns=columns)
  df.to_csv('csv.csv')


def create_df(path):
  columns=['ID отдаваемой валюты', 'ID получаемой валюты', 'ID обменного пункта', 'Курс обмена (отдать)', 'Курс обмена (получить)', 'Резерв получаемой валюты', 'Отзывы', 'Не используется', 'Минимальная сумма обмена', 'Максимальная сумма обмена', 'ID города (для направлений с наличными)']
  df = pd.read_csv(path, delimiter=';', encoding='cp1251', names=columns)


if __name__ == '__main__':
  # getData(URL_API)
  # create_df('./currency/bm_rates.dat')
  create_info_table('./currency/bm_cy.dat')
  
  
