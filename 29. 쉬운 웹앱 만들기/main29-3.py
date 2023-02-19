# 선택한 날짜의 비트코인 시세를 그래프로 출력해주는 웹앱 코드

import streamlit as st 
import datetime
import pyupbit

d = st.date_input(
    "날짜를 선택하세요",
    datetime.date.today()
)

st.write('비트코인 1일 차트')

ticker = 'KRW-BTC'
interval = 'minute60'
to = str(d+datetime.timedelta(days=1))
count = 24
price_now = pyupbit.get_ohlcv(ticker=ticker, interval=interval, to=to, count=count)

st.line_chart(price_now.close)