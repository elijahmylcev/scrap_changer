import pandas as pd

# return id_currency array 
def get_intermediate_currencies(df_info, column_name, substring):
  df = df_info[~df_info[column_name].str.contains(substring)]
  return df['id_currency'].tolist()
