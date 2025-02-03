import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("https://raw.githubusercontent.com/tirtasm/analisis-data-python-dicoding/refs/heads/main/dashboard/hour_cleaned.csv")

def plot_weather_impact(data):
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.boxplot(x='weather', y='count', data=data, palette="Set2", ax=ax)
    ax.set_title('Pengaruh Cuaca terhadap Penyewaan Sepeda')
    ax.set_xlabel('Cuaca')
    ax.set_ylabel('Jumlah Penyewaan')
    return fig

def plot_rental_by_hour(data):
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.lineplot(x='hour', y='count', data=data, color='r', marker='o', ax=ax)
    ax.set_title('Jumlah Penyewaan Sepeda Berdasarkan Jam dalam Sehari')
    ax.set_xlabel('Jam')
    ax.set_ylabel('Jumlah Penyewaan')
    ax.set_xticks(range(0, 24))
    ax.grid()
    return fig

st.set_page_config(page_title="Bike Sharing Dashboard", page_icon="🚲", layout="wide")
st.title("Bike Sharing Dashboard")

st.sidebar.title("Navigasi")
st.sidebar.markdown("Pilih visualisasi yang ingin ditampilkan:")
show_weather = st.sidebar.checkbox("Pengaruh cuaca terhadap penyewaan", True)
show_hourly = st.sidebar.checkbox("Jumlah penyewaan berdasarkan jam", True)

st.sidebar.header("Filter Data")
selected_season = st.sidebar.multiselect(
    "Pilih musim:", options=df['season'].unique(), default=df['season'].unique()
)
selected_weather = st.sidebar.multiselect(
    "Pilih cuaca:", options=df['weather'].unique(), default=df['weather'].unique()
)

filtered_data = df[(df['season'].isin(selected_season)) & (df['weather'].isin(selected_weather))]

st.sidebar.markdown("Dataset ini berisi informasi penyewaan sepeda berdasarkan cuaca dan jam")

st.header(" Pertanyaan Bisnis")
st.markdown("1. Apakah cuaca mempengaruhi jumlah penyewaan sepeda?")
st.markdown("2. Kapan waktu penyewaan sepeda paling banyak dalam sehari?")

kol1, kol2 = st.columns(2)

if show_weather:
    with kol1:
        st.subheader("Pengaruh cuaca terhadap penyewaan sepeda")
        st.pyplot(plot_weather_impact(filtered_data))

if show_hourly:
    with kol2:
        st.subheader("Jumlah penyewaan sepeda berdasarkan jam dalam sehari")
        st.pyplot(plot_rental_by_hour(filtered_data))

st.header("Kesimpulan")
st.subheader("Apakah cuaca memengaruhi jumlah penyewaan sepeda?")
st.markdown("Berdasarkan visualisasi, penyewaan sepeda cenderung lebih banyak pada cuaca cerah dibanding cuaca buruk. Hal ini masuk akal karena kondisi cuaca buruk seperti hujan dapat mengurangi kenyamanan pengguna sepeda dan bahkan meningkatkan risiko kecelakaan. Dengan demikian, cuaca yang cerah menjadi faktor yang pilihan dari tingginya jumlah penyewaan sepeda.")
st.subheader("Kapan waktu penyewaan sepeda paling banyak dalam sehari?")
st.markdown("Penyewaan sepeda paling banyak terjadi pada pukul 17.00 dan 18.00. Karena kemungkinan besar waktu tersebut bertepatan dengan jam pulang kerja atau aktivitas sore hari, di mana mereka lebih cenderung menggunakan sepeda untuk pulang dari kantor. Sebaliknya, penyewaan sepeda paling sedikit terjadi pada pukul 04.00, karena waktu tersebut masih pagi hari, sehingga aktivitas pengguna cenderung sangat sedikit.")

st.success("Dashboard Analisis data penyewaan sepeda tersedia di atas.")
