import streamlit as st
import pandas as pd
import numpy as np
from html_module import line_break, section, callout, title
from PIL import Image

# 전체 페이지 설정
st.set_page_config(
    page_title="Progress",
    page_icon="💡",
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
line_break()

# 구성도 section
section('구성도')
image = Image.open('images/content.PNG')
st.image(image,)
line_break()
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
line_break()

# 문제점 section
section('Problem')
st.subheader("OpenCV Real Time")
callout([
    '모델의 성능 자체는 높게 나타났지만, OpenCV를 이용 수화를 예측할 경우 대부분을 다르게 예측하는 문제가 발생한다.'
       ])
line_break()

col1, col2 = st.columns(2)
with col1:
    st.markdown('1. **A**를 **I** 라고 잘못 예측한 경우')
    image = Image.open('images/fail1.jpg')
    st.image(image,)
    line_break()

with col2:   
    st.markdown('2. **W**를 **B**라고 잘못 예측한 경우')
    image2 = Image.open('images/fail2.jpg')
    st.image(image2,)
    line_break()
    
line_break()

# 해결 section
section('Solve')
tab1, tab2 = st.tabs(["Detection", "Image Train"])

with tab1:
    st.subheader("Detection")
    callout([
        '수화를 제대로 인식하지 못 하는 문제점의 원인이 무엇일까?',
        '',
        '1. 모델 자체의 성능 문제',
        '2. 전체적인 손 모양과 손가락의 마디들을 제대로 인식하지 못 하는 문제',
        '',
        '=> 결론적으로 모델의 성능 보다는 손 모양을 잘 인식할 수 있도록 개선이 필요하다고 생각'
    ])
    line_break()
    
    image = Image.open('images/mediapip.PNG')
    st.image(image,)
    callout([
        'Hand Detection 방법을 이용하여 손가락 마디, 관절 등을 인식할 수 있도록 한다.',
    ])
    
with tab2:
    st.subheader("Image Train")
    callout([
        'Hand Detection을 이용한 이미지로 모델을 학습 시키기 위해 직접 데이터를 수집하였다.',
        '직접 모션을 취한 뒤 이미지를 저장하여 데이터를 수집하고, 학습시킨 후 테스트를 해보니 성능이 눈에 띄게 좋아졌다.'
    ])
    line_break()
    
    image = Image.open('images/detection1.png')
    st.image(image,)
    image2 = Image.open('images/detection2.png')
    st.image(image2,)   
    image3 = Image.open('images/detection3.png')
    st.image(image3,)
    st.caption('직접 수집한 데이터 사진의 일부입니다.')
    
line_break()
