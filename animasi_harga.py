import streamlit as st
import pandas as pd
import altair as alt
import time

# Data
data = {
    "Tanggal": [
        "2022-12-30", "2022-12-29", "2022-12-28", "2022-12-27", "2022-12-23", "2022-12-22",
        "2022-12-21", "2022-12-20", "2022-12-19", "2022-12-16", "2022-12-15", "2022-12-14",
        "2022-12-13", "2022-12-12", "2022-09-12", "2022-08-12", "2022-07-12", "2022-06-12",
        "2022-05-12", "2022-02-12", "2022-01-12"
    ],
    "Harga": [
        1.8262, 1.826, 1.8158, 1.8231, 1.8042, 1.7953,
        1.8254, 1.8254, 1.7977, 1.8002, 1.7878, 1.8187,
        1.8255, 1.7923, 1.8107, 1.8015, 1.798, 1.7824,
        1.7813, 1.8096, 1.8152
    ]
}

df = pd.DataFrame(data)
df["Tanggal"] = pd.to_datetime(df["Tanggal"])

# Judul
st.title("Animasi Grafik Perubahan Harga per Tanggal")

# Plot animasi
placeholder = st.empty()
x = []
y = []

for i in range(0, len(df), 5):  # interval 5
    x.append(df["Tanggal"].iloc[i])
    y.append(df["Harga"].iloc[i])

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(x, y, marker='o', linestyle='-', color='green')
    ax.set_xlabel("Tanggal")
    ax.set_ylabel("Harga")
    ax.set_title("Perubahan Harga")
    ax.tick_params(axis='x', rotation=45)
    placeholder.pyplot(fig)
    time.sleep(0.5)
