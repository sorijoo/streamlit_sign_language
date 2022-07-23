import streamlit as st 
import tensorflow as tf
import numpy as np
from PIL import Image
from html_module import line_break, section, callout, title

st.set_page_config(
    page_title="Korean Sign Language Prediction",
    page_icon="📸",
    initial_sidebar_state="expanded", 
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

title('Korean Sign Language Prediction')
image = Image.open('images/korean_sign_lang.png')
st.image(image,)
line_break()

section('Image Upload')
callout([
    '위의 수화 이미지를 참고하여 사진을 찍은 후 업로드 해보세요!'
])
line_break()

# Image Upload
filename = st.file_uploader("Choose a file")

model = tf.keras.models.load_model('model/model_kor_num_no_augmentation.h5')

convertDict = {0: "1",
 1: "10",
 2: "10",
 3: "2",
 4: "3",
 5: "4",
 6: "5",
 7: "6",
 8: "7",
 9: "8",
 10: "9"}

@st.cache
def convert_letter(result):
    classLabels = {idx:c for idx, c in zip(idx, alpha)}
    try:
        res = int(result)
        return classLabels[res]
    except:
        return "err"


if filename is not None:
    img = Image.open(filename)
    img = img.convert('L')
    img = img.resize((300, 300)) 
    img = np.array(img)
    pred = np.argmax(model.predict(img.reshape(1, 300, 300, 1)))
    # text = []
    st.image(img, use_column_width=False)
    st.text('혹시.. 당신이 원하는 숫자가')
    st.title(convertDict[pred])
    st.text('인가요?')
