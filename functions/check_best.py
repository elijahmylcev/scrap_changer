from .target_function import target_function

def check_best(df, initial_currency, final_currency, intermediate_currencies):
  start = None
  end=None
  best_intermediate_currency = None
  best_result = 0
  for intermediate_currency in intermediate_currencies:
    start_price = target_function(df, initial_currency, intermediate_currency)
    end_price = target_function(df, intermediate_currency, final_currency, out=False)
    if start_price and end_price:
      result = end_price / start_price
    else:
      result = 0
    if result > best_result:
      start = start_price
      end = end_price
      best_result = result
      best_intermediate_currency = intermediate_currency
  return {
    'start' :start,
    'end': end,
    'best_intermediate': best_intermediate_currency,
    'best_result': best_result
  }
