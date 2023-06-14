import streamlit as st
from PIL import Image
import pandas as pd
import altair as alt

st.set_page_config(
    page_title="Potensi Kopi Indonesia di Pasar Global",
    layout="wide"
)

with st.sidebar:
    st.write("Tahun 2017-2022")


image = Image.open('buah-kopi.png')

st.title("Analisis Perkembangan Kopi Indonesia di Pasar Global")
st.caption("oleh : Irvant Ismail")

'''Kopi adalah minuman hasil seduhan biji kopi yang telah disangrai dan dihaluskan menjadi bubuk. Kopi merupakan
salah satu komoditas di dunia yang dibudidayakan lebih dari 50 negara. Kopi digolongkan kedalam famili Rubiacea dengan genus Coffee.
 Secara umum kopi hanya memiliki dua spesies yaitu Coffee Arabica dan Coffee Robusta.'''
st.image(
    image,
    caption="Buah Kopi"
)
'''Indonesia merupakan negara terbesar keempat yang memproduksi biji kopi setelah Brazil, Vietnam, dan Kolombia.
Hal ini membuat produk kita memiliki keunggulan dalam volume produksi dibandingkan negara lainnya.
Lalu Bagaimana Pekembangan Kopi kita di Pasar Global?'''


df = pd.read_excel('data/brasil-rajai-produksi-kopi-pada-2020-indonesia-urutan-berapa.xlsx')
st.header ("TOP 9 Negara Produksi Kopi di Dunia")
st.bar_chart(data=df,  x='nama_data', y='value')
'''Untuk data diatas pada tahun 2020 dapat dilihat bahwa Brazil berada pada tingkat Produksi Terbesar
didunia yaitu 63,4, diikuti oleh Vietnam, Kolombia, dan Indonesia'''
df

data = pd.read_excel('data/produksi-kopi-indonesia-meningkat-capai-794-ribu-ton-pada-2022.xlsx')
st.header ("Produksi Kopi Negara Indonesia dari tahun 2017-2022")
'''Untuk tahun 2017 - 2022 produksi kopi Indonesia mengalami kenaikan, dilansir dari detik.com bahwa mengalami kenaikan karena pandemi
juga telah berakhir '''
st.line_chart(data=data, x='Tahun', y='Jumlah(ribu ton)', width=0, height=0, use_container_width=True)


data1 = pd.read_excel('data/kinerja-ekspor-kopi-indonesia-meningkat-pada-2021.xlsx')
st.header ("Rata-rata volume eksport kopi di Indonesia Periode 2011-2021")
st.line_chart(data=data1, x='date', y='Volume')
'''Pada grafik diatas kita bisa lihat Volume eksport kopi indonesia pada 2017 ke 2018 mengalami penurunan
namun 2018-2022 ekspor kita terus mengalami kenaikan yang signifikan bahkan di Era pandemi sekalipun'''
st.header ("Nilai Eksport Kopi Indonesia Periode 2011-2021")
st.bar_chart(data=data1, x='date', y= 'Nilai')
''' Nilai Eksport kopi Indonesia juga selaras dengan volume produksinya'''

data2 = pd.read_excel('data/dari-as-sampai-rusia-ini-negara-tujuan-ekspor-kopi-indonesia-pada-2022 (1).xlsx')
st.header("Negara-negara tujuan ekspor Indonesia")
st.bar_chart(data=data2,  x='Negara', y='Nilai')


st.header("Kesimpulan")
'''Negara Indonesia dengan produktivitas kopinya dapat berkembang di pasar global bahkan di era pandemi
sekaligus, namun naik atau turun nya nilai ekspor tidak terlalu di pengaruhi oleh tingkat produksi ekspor tersebut'''

