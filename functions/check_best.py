from .target_function import target_function

def check_best(df, initial_currency, final_currency, intermediate_currencies):
  best_intermediate_currency = None
  best_result = 0
  for intermediate_currency in intermediate_currencies:
    result = target_function(df, initial_currency, intermediate_currency) * target_function(df, intermediate_currency, final_currency)
    if result > best_result:
      best_result = result
      best_intermediate_currency = intermediate_currency
