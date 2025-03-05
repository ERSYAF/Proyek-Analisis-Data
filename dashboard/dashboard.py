import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from datetime import datetime

sns.set(style='darkgrid')

# Load data
df = pd.read_csv("dashboard/dataclean_bikesharing.csv", parse_dates=['date'])

# Menentukan tanggal awal dan akhir
min_date = df['date'].min().date()
max_date = df['date'].max().date()

# Sidebar untuk pemilihan rentang tanggal
with st.sidebar:
    st.title("Bike Sharing Dashboard")
    st.image("https://storage.googleapis.com/kaggle-datasets-images/4165290/7200983/7ab427725cb0c7b59c5b4e450ede9c1a/dataset-card.png?t=2023-12-15-10-05-39", use_container_width=True)
    start_date = st.date_input("Pilih tanggal mulai", min_value=min_date, max_value=max_date, value=min_date)
    end_date = st.date_input("Pilih tanggal akhir", min_value=min_date, max_value=max_date, value=max_date)

# Filter data berdasarkan rentang tanggal
df_filtered = df[(df['date'] >= pd.to_datetime(start_date)) & (df['date'] <= pd.to_datetime(end_date))]

# Menambahkan kolom tahun untuk visualisasi per tahun
df_filtered['year'] = df_filtered['date'].dt.year

# Grafik Tren Peminjaman Harian per Tahun
st.subheader('Tren Peminjaman Sepeda Harian pada Tahun 2011 dan 2012')
fig, ax = plt.subplots(figsize=(14, 6))
sns.lineplot(data=df_filtered, x='date', y='count', hue='year', palette="coolwarm", alpha=0.5)
ax.set_xlabel('Tanggal')
ax.set_ylabel('Jumlah Peminjaman')
ax.set_title('Tren Peminjaman Sepeda Harian pada Tahun 2011 dan 2012')
st.pyplot(fig)

# Grafik Pengaruh Kondisi Cuaca terhadap Peminjaman Sepeda
st.subheader('Pengaruh Kondisi Cuaca terhadap Jumlah Peminjaman Sepeda')
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(data=df_filtered, x='weather_condition', y='count', palette="dark")
ax.set_xlabel('Kondisi Cuaca')
ax.set_ylabel('Jumlah Peminjaman')
ax.set_title('Pengaruh Kondisi Cuaca terhadap Jumlah Peminjaman Sepeda')
st.pyplot(fig)

st.caption('Copyright ©ersyafin 2025')
