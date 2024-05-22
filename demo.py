import streamlit as st
from PIL import Image
st.title("お小遣い２００円もらった！！")

image = Image.open('スクリーンショット 2024-05-22 11.07.15.png')
st.image(image, width=200)

st.text("アーニャがお菓子を選んでくれるらしい!!")

names = ['蒲焼さん', 'クッピーラムネ', 'タラタラしてんじゃねーよ', 'うまい棒', 'ヤングドーナツ', 'カルパス', 'ガブリチュウ', 'パチパチパニック', 'ポテチ', 'チョコマシュマロ', 'ベビースター', 'グミ', 'キットカット', 'ブタメン', 'チロルチョコ', 'キャベツ太郎', 'ハッピーターン', 'きな粉棒']
prices = [15, 30, 40, 11, 40, 13, 40, 35, 100, 10, 40, 10, 30, 70, 35, 30, 60, 40]

en = 200
a = 0
while en > 0:
    import random
    num = random.randrange(17)
    print(names[num], prices[num])
    st.text(f'{names[num]} {prices[num]}円')
    en -= prices[num]
    a += prices[num]

b = a-200

if b == 0:
    st.text("ちょうど!!まいどぉ!")
else:
    st.text(f"😭{a-200}円足りない😭")
    okasi = st.text_input('何のお菓子をやめる？↓')

c = names.index(okasi)
d = prices[c]
e = d-b

if e > 0:
    st.text(f"おつり{e}円だよ")
elif e == 0:
    st.text("ちょうど!!まいどぉ!!")
else:
    st.text(f"まだ{b-d}円足りない!")
