# CANDLE 조회
import pyupbit

df = pyupbit.get_ohlcv("KRW-BTC", 'minute1') # minute자리를 day, week, month로 바꾸면 일봉, 주봉, 월봉 데이터 가져옴/ 3번째 인자는 개수, default는 200개.
print(df)

# 월봉은 거래량이 매우 많아지기 때문에 이를 간단히 표현하기 위해 pandas 이용 -> pandas.options.display.float_format = "{:.1f}".format 추가
#to_excel 함수로 excel파일 만들 수 있음.

"""
n분봉 만들기 : pandas의 resample() 함수를 사용

df['open'].resample('nT').first() : 시가
df['high'].resample('nT').max() : 고가
df['low'].resample('nT').min() : 저가
df['close'].resample('nT'}.last() : 종가
df['volume'].resample('nT').sum() : 거래량
"""