import streamlit as st
from PIL import Image
import random
import re


st.title("お小遣い２００円もらった！！")

image = Image.open('スクリーンショット 2024-05-22 11.07.15.png')
st.image(image, width=200)

st.text("アーニャがランダムでお菓子を選んでくれたよ!!")

names = ['蒲焼さん', 'クッピーラムネ', 'タラタラしてんじゃねーよ', 'うまい棒', 'ヤングドーナツ', 'カルパス', 'ガブリチュウ', 'パチパチパニック', 'ポテチ', 'チョコマシュマロ', 'ベビースター', 'グミ', 'キットカット', 'ブタメン', 'チロルチョコ', 'キャベツ太郎', 'ハッピーターン', 'きな粉棒']
prices = [15, 30, 40, 11, 40, 13, 40, 35, 100, 10, 40, 10, 30, 70, 35, 30, 60, 40]

en = 200
a = 0

first = False

if 'anya' not in st.session_state:
    st.session_state.anya = list()
    first = True

if first:
    while en > 0:
        num = random.randrange(17)
        st.session_state.anya.append(f'{names[num]} {prices[num]}円')
        print(names[num], prices[num])
        en -= prices[num]
        a += prices[num]
        st.session_state.a = a

for item in st.session_state.anya:
   st.text(item)

b = st.session_state.a-200

if b == 0:
    st.text("ちょうど!!まいどぉ!")
else:
    st.text(f"😭{st.session_state.a-200}円足りない😭")
    okasi = st.text_input('何のお菓子をやめる？↓')
    if okasi == "":
        st.text("")
    else:
        c = names.index(okasi)
        d = prices[c]
        e = d-b
        if e > 0:
            st.text(f"おつり{e}円だよ〜")
        elif e == 0:
            st.text(f"ちょうどまいど！！")
        else:
            st.text(f"まだ{b-d}円足りない!")
            tarinai = b-d
            okasi2 = st.text_input('もう一つお菓子をやめよう😢↓')
            if okasi2 == "":
                st.text("")
            else:
                zyun = names.index(okasi2)
                zyun2 = prices[zyun]
                g = zyun2 - tarinai 
                if g > 0:
                    st.text(f"おつり{g}円だよ")
                elif g == 0:
                    st.text("ちょうど！！まいど！！")
                else:
                    st.text("まだ足りねぇよ！計算できひんのか！！💢")

