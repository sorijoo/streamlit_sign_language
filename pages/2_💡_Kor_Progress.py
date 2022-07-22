import streamlit as st
import pandas as pd
import numpy as np
from html_module import line_break, section, callout, title
from PIL import Image

# 전체 페이지 설정
st.set_page_config(
    page_title="Korean Sign Number Progress",
    page_icon="☝️",
    initial_sidebar_state="expanded", 
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

title('Kor Sign Progress')

# Progress section
section('Progress')
image = Image.open('images/progress.PNG')
st.image(image,)
line_break()
line_break()

# 구성도 section
section('구성도')

line_break()
line_break()
    
