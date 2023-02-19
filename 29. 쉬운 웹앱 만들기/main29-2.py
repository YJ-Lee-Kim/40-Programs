# 달력에서 날짜 선택하는 코드

import streamlit as st 
import datetime

d = st.date_input(
    "날짜를 선택하세요",
    datetime.date.today()
)

st.write('선택한 날짜:',d)

# import datetime
# import streamlit as st

# d = st.date_input(
#     "When\'s your birthday",
#     datetime.date(2019, 7, 6))
# st.write('Your birthday is:', d)