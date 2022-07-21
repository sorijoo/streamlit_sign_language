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
section('주제 선정')
callout([
    'Kaggle - Sign Language MNIST Dataset'
    '알파벳 문자 A-Z에 대한 일대일 맵으로 라벨(0-25)을 나타낸다. 단, 제스처 모션으로 인해 9(J)와 25(Z)의 경우는 제외한다.',
])
line_break()
