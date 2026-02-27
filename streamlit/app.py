import streamlit as st
import numpy as np
import pandas as pd

# 제목 설정
st.title("🚀 나의 첫 실시간 발표 도구")

# 1. 사이드바에 조절 바 만들기
st.sidebar.header("설정 변경")
freq = st.sidebar.slider("주파수(Frequency) 조절", 1, 100, 20)
power = st.sidebar.slider("진폭(Amplitude) 조절", 1, 10, 5)

# 2. 로직 구현 (파이썬 연산)
x = np.linspace(0, 10, 500)
y = power * np.sin(x * freq / 10)
data = pd.DataFrame({'x': x, 'y': y})

# 3. 시각화 출력
st.subheader(f"현재 결과: 주파수 {freq}, 진폭 {power}")
st.line_chart(data.set_index('x'))

st.write("왼쪽 사이드바의 슬라이더를 움직이면 로직이 실시간으로 계산됩니다!")
