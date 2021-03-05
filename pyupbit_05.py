# 업비트 로그인
import pyupbit

f= open("upbit.txt")
lines = f.readlines()
access = lines[0].strip()
secret = lines[1].strip()
f.close()

upbit = pyupbit.Upbit(access,secret)
balance = upbit.get_balance("KRW")  # 한 가지 잔고정보만 제공, but get_balances()를 사용하면 모든 잔고정보 제공(튜플형태)
print(balance)
