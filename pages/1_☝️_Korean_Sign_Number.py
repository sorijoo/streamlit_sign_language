import streamlit as st
import pandas as pd
import numpy as np
from html_module import line_break, section, callout, title
from PIL import Image

# 전체 페이지 설정
st.set_page_config(
    page_title="Korean Sign Number",
    page_icon="☝️",  # 아이콘
    initial_sidebar_state="expanded", 
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

title('Korean Sign Number CNN Project')

# 개요 section
section('Summary')
image = Image.open('images/korean_sign.jpg')
st.image(image,)
callout([
  '안녕하세요! ✌ Sign팀입니다. 🙂',
  'Kaggle의 Korean Sign Number Language 데이터를 이용하여 CNN Project를 진행하였습니다.',
  '이미지를 업로드하면 해당 수화 이미지가 어느 숫자를 의미히는지 예측해줍니다..'
])
line_break()

# 데이터 출처 section
section('Dataset')
link = 'https://www.kaggle.com/datasets/nahyunpark/korean-sign-languageksl-numbers'
st.markdown(link, unsafe_allow_html=True)
st.caption('데이터 출처 사이트로 이동하기')
line_break()

# Sign Team Notion section
section('Notion')
link = 'https://www.notion.so/likelion-aischool/English-Sign-Language-759acc98547a4e259367a63625ba2158'
st.markdown(link, unsafe_allow_html=True)
st.caption('팀 노션 페이지로 이동하기')
line_break()
