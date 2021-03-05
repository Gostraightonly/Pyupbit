# 주문취소
import pyupbit
import pprint

f = open("upbit.txt")
lines = f.readlines()
access = lines[0].strip()
secret = lines[1].strip()
f.close()

upbit = pyupbit.Upbit(access,secret)
#resp = upbit.buy_limit_order("KRW-XRP",520,10)
#print(resp[0]['uuid'])

uuid = ""
resp = upbit.cancel_order(uuid)
pprint.pprint(resp)
