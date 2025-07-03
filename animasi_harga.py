import streamlit as st
import pandas as pd
import altair as alt
import time

# Data
data = {
    "Tanggal": [
        "30/12/2022", "29/12/2022", "28/12/2022", "27/12/2022", "23/12/2022", "22/12/2022",
        "21/12/2022", "20/12/2022", "19/12/2022", "16/12/2022", "15/12/2022", "14/12/2022",
        "13/12/2022", "12/12/2022", "12/09/2022", "12/08/2022", "12/07/2022", "12/06/2022",
        "12/05/2022", "12/02/2022", "12/01/2022"
    ],
    "Harga": [
        "Rp18.262", "Rp1.826", "Rp18.158", "Rp18.231", "Rp18.042", "Rp17.953",
        "Rp18.254", "Rp18.254", "Rp17.977", "Rp18.002", "Rp17.878", "Rp18.187",
        "Rp18.255", "Rp17.923", "Rp18.107", "Rp18.015", "Rp1.798", "Rp17.824",
        "Rp17.813", "Rp18.096", "Rp18.152"
    ],
    "Volume": [
        10750000, 10599000, 11808000, 15962000, 10546000, 17577000,
        11018000, 19750000, 8609000, 12875000, 18532000, 14380000,
        23091000, 10778000, 15094000, 11627000, 15557000, 12786000,
        17982000, 18372000, 22615000
    ]
}

# Format data
df = pd.DataFrame(data)
df["Tanggal"] = pd.to_datetime(df["Tanggal"], dayfirst=True)
df["Harga"] = df["Harga"].str.replace("Rp", "").str.replace(".", "").astype(float) / 1000

# Judul dan animasi
st.title("📈 Animasi Grafik Harga per Tanggal (Interval 5)")

placeholder = st.empty()
x = []
y = []

for i in range(0, len(df), 5):
    x.append(df["Tanggal"].iloc[i])
    y.append(df["Harga"].iloc[i])
    
    anim_df = pd.DataFrame({"Tanggal": x, "Harga": y})
    line_chart = alt.Chart(anim_df).mark_line(point=True).encode(
        x='Tanggal:T',
        y='Harga:Q',
        tooltip=['Tanggal', 'Harga']
    ).properties(width=800, height=400)
    
    placeholder.altair_chart(line_chart, use_container_width=True)
    time.sleep(0.5)
