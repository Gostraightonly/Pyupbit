import pyupbit_2

tickers = pyupbit_2.get_tickers(fiat="BTC")  # get_tickers : fiat 정보를 이용해서 필요한 부분만 이용
print(tickers)
print(len(tickers))
