# 지정가 매수/매도주문
import pyupbit
import pprint

#매수
f = open("upbit.txt")
lines = f.readlines()
access = lines[0].strip()
secret = lines[1].strip()
f.close()

upbit = pyupbit.Upbit(access,secret)
resp = upbit.buy_limit_order("KRW-XRP",535,10)
pprint.pprint(resp)

#매도 : sell_limit_ordr(티커, 주문가격, 주문량)함수 이용. get_balance이용해서 본인이 가지고 있는 만큼 매도 가능
