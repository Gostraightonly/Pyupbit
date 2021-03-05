# 잔고조회
import pyupbit
import pprint

f = open("upbit.txt")
lines = f.readlines()
access = lines[0].strip()
secret = lines[1].strip()
f.close()

upbit = pyupbit.Upbit(access,secret)
balances = upbit.get_balances()
pprint.pprint(balances[0])  # balaces에서 가져오는 데이터는 튜플 그리고 0번째가 잔고 데이터
