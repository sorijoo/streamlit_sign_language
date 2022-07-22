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
image = Image.open('images/korean_number.PNG')
st.image(image,)
callout([
  '안녕하세요! ✌ Sign팀입니다. 🙂',
  'Kaggle의 English Sign Language 데이터를 이용하여 CNN Project를 진행하였습니다.',
  'OpenCV를 이용하여 실시간으로 알파벳 수화를 예측할 수 있도록 만들었습니다.'
])
line_break()
