import streamlit as st
import pandas as pd
import numpy as np
from html_module import line_break, section, callout, title
from PIL import Image

# 전체 페이지 설정
st.set_page_config(
    page_title="Progress",
    page_icon="🧐",
    initial_sidebar_state="expanded", 
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

# Progress section
section('Progress')
image = Image.open('images/progress.PNG')
st.image(image,)
line_break()

# 주제 선정 section
section('Subject')
callout([
    '[데이터]',
    'Kaggle - Sign Language MNIST Dataset',
    '알파벳 문자 A-Z에 대한 일대일 맵으로 Label(0-25)을 나타낸다. 단, 제스처 모션으로 인해 9(J)와 25(Z)의 경우는 제외한다.',
    '',
    '[필요성]',
    '청각 장애인과 청각 장애인이 컴퓨터 비전 애플리케이션을 사용하여 더 나은 의사 소통을 할 수 있도록 실용적으로 도움이 되기를 바란다.'
])
line_break()

# 문제점 section
section('Problem')
tab1, tab2, tab3 = st.tabs(["Problem1", "Problem2", "Problem3"])

with tab1:
    st.subheader("OpenCV Real Time")
    callout([
    '모델의 성능 자체는 높게 나타났지만, OpenCV Real Time으로 수화를 예측할 경우 대부분을 다르게 예측하는 문제 발생'
    ])
    line_break()
    
    st.markdown('1. **A**를 **I** 라고 잘못 예측한 경우')
    image = Image.open('images/fail1.jpg')
    st.image(image,)
    line_break()
    
    st.markdown('2. **W**를 **B**라고 잘못 예측한 경우')
    image2 = Image.open('images/fail2.jpg')
    st.image(image2,)
    
with tab2:
    st.subheader("An owl")

line_break()

# 해결 section
section('Solve')
