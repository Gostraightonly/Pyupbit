# 현재가 정보 가져오기

import pyupbit

price = pyupbit.get_current_price("KRW-BTC")
print(price)

"""
# 여러개 가져오기
tickers = ["KRW-BTC", "KRW-XRP"]
price = pyupbit.get_current_price(tickers)
print(price)
"""
