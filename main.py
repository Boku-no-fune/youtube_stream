import streamlit as st
import time


st.title('streamlit 超入門')
st.write('DataFrame')

st.write('プログレスバーの表示')
'Start!'

latest_iteration =st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.05)

'Done!'
left_column, right_column = st.columns(2)

button= left_column.button('右カラムに文字を表示')
if button:
    right_column.button('ここは右カラム')

expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')

color = st.color_picker('色を選んで')


    #content = st.text_input('あなたの趣味を教えてください')

    #option = st.selectbox(
    #    'あなたが好きな数字を教えてください',
    #     list(range(1,11))
    #)

    #'あなたの趣味',content 
    #'あなたの好きな数字は', option , 'です'


    #スライダ
    #condition = st.slider('あなたの今の調子は', 0, 1000, 500)
    #'あなたの調子', condition



