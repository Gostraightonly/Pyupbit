# 시장가 매도/매수 주문
import pyupbit
import pprint

# 매수
f = open("upbit.txt")
lines = f.readlines()
access = lines[0].strip()
secret = lines[1].strip()
f.close()

upbit = pyupbit.Upbit(access,secret)
resp = upbit.buy_market_order("KRW-XRP",10)
pprint.pprint(resp)

#매도 : sell_market_order(티커, 주문량)함수 이용
