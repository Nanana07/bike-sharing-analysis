import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Memuat dataset
df = pd.read_csv('C:/Users/hp/Documents/Nanda/day.csv')

# Menampilkan Judul
st.title('Dashboard Analisis Bike Sharing')

# Menampilkan Tabel Data
st.write("Tabel Data", df.head())

# Visualisasi Distribusi Suhu
st.subheader('Distribusi Suhu')
sns.histplot(df['temp'])
plt.title('Distribusi Suhu')
st.pyplot()

# Visualisasi Penggunaan Sepeda Berdasarkan Jam
hourly_usage = df.groupby('hr')['cnt'].sum()
st.subheader('Penggunaan Sepeda Berdasarkan Jam')
st.bar_chart(hourly_usage)
