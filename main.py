import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import koreanize-matplotlib

# CSV 파일 불러오기
file_path = 'path_to_your_file/202406_202406_연령별인구현황_월간 (1).csv'
data = pd.read_csv(file_path, encoding='cp949')

# 숫자 형식 변환
data = data.replace(',', '', regex=True)
data.iloc[:, 1:] = data.iloc[:, 1:].astype(int)

# Streamlit 애플리케이션
st.title("중학생 인구 비율 원 그래프")
selected_region = st.selectbox("지역을 선택하세요:", data['행정구역'].unique())

# 선택한 지역의 데이터 추출
region_data = data[data['행정구역'] == selected_region]

# 중학생 연령 인구수 추출 및 비율 계산 (12세~14세)
middle_school_population = region_data.iloc[0][[f'2024년06월_계_{age}세' for age in range(12, 15)]].sum()
total_population = region_data.iloc[0]['2024년06월_계_총인구수']
other_population = total_population - middle_school_population

# 원 그래프 데이터 준비
labels = ['중학생 인구', '기타 인구']
sizes = [middle_school_population, other_population]
colors = ['#ff9999','#66b3ff']
explode = (0.1, 0)

# 원 그래프 생성
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

st.pyplot(fig1)
