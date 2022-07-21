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

# 주제 선정 section
section('주제 선정')
st.markdown('##### **프로젝트 소개**')
