def target_function(df, initial_currency, final_currency, out=True):
  initial = df[(df['ID отдаваемой валюты'] == initial_currency) & (df['ID получаемой валюты'] == final_currency)]
  if initial.empty:
    rate = 0
  else:
    if out:
      rate = min(initial['Курс обмена (отдать)'])
    else:
      rate = max(initial['Курс обмена (получить)'])

  return rate
