# 호가 정보 가져오기

import pyupbit
import pprint   # 복잡한 딕셔너리 보기 좋게 표현해줌

orderbooks = pyupbit.get_orderbook("KRW-BTC")
pprint.pprint(orderbooks)