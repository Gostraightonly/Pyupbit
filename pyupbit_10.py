# 변동성 돌파전략 구현
import pyupbit
import time
import datetime

# 목표가 설정함수
def cal_target(ticker):
    df = pyupbit.get_ohlcv(ticker,"day")
    yesterday = df.iloc[-2]     #행의 끝에서 두 번째
    today = df.iloc[-1]     #행의 끝에서 첫 번째
    yesterday_range = yesterday['high']-yesterday['low']
    target = today['open'] + yesterday_range * 0.5
    return target

# 로그인 정보
f = open("upbit.txt")
lines = f.readlines()
access = lines[0].strip()
secret = lines[1].strip()
f.close()
upbit = pyupbit.Upbit(access,secret)

target = cal_target("KRW-BTC")
op_mode = False     # 매수 가능여부
hold = False    # 코인 보유여부

while True:
   now = datetime.datetime.now()   # 현재시간 출력

   # 매도 시도
   if now.hour == 8 and now.minute == 59 and 50 <= now.second <= 59:
       if op_mode is True and hold is True:
           btc_balance = upbit.get_balance("KRW-BTC")
           upbit.sell_market_order("KRW-BTC",btc_balance)
           hold = False

       op_mode = False
       time.sleep(10)

   # 9시 목표가 갱신
   if now.hour == 9 and now.minute == 0 and 20 <= now.second <= 30:
       target = cal_target("KRW-BTC")
       op_mode = True

   price = pyupbit.get_current_price("KRW-BTC")    # 현재가 호출

   # 매수 시도
   if op_mode is True and hold is False and price is not None and price >= target:
       #매수
       krw_balance = upbit.get_balance("KRW")
       upbit.buy_market_order("KRW-BTC", krw_balance)
       hold = True

   print(f"현재시간: {now} 목표가: {target} 현재가: {price} 보유상태: {hold} 동작상태: {op_mode}")

   time.sleep(1)

