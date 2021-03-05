# 원화시장 현재가만 가져오기

import pyupbit

krw_tickers = pyupbit.get_tickers(fiat = "KRW")
prices = pyupbit.get_current_price(krw_tickers)

for k, v in prices.items():
    print(k, v)
