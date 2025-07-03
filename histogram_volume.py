import streamlit as st
import pandas as pd
import altair as alt

# Data
data = {
    "Tanggal": [
        "2022-12-30", "2022-12-29", "2022-12-28", "2022-12-27", "2022-12-23", "2022-12-22",
        "2022-12-21", "2022-12-20", "2022-12-19", "2022-12-16", "2022-12-15", "2022-12-14",
        "2022-12-13", "2022-12-12", "2022-09-12", "2022-08-12", "2022-07-12", "2022-06-12",
        "2022-05-12", "2022-02-12", "2022-01-12"
    ],
    "Volume": [
        10750000, 10599000, 11808000, 15962000, 10546000, 17577000,
        11018000, 19750000, 8609000, 12875000, 18532000, 14380000,
        23091000, 10778000, 15094000, 11627000, 15557000, 12786000,
        17982000, 18372000, 22615000
    ]
}

df = pd.DataFrame(data)
df["Tanggal"] = pd.to_datetime(df["Tanggal"])

# Judul
st.title("Grafik Volume Penjualan per Hari (Altair Chart)")

# Altair bar chart
chart = alt.Chart(df).mark_bar().encode(
    x=alt.X('Tanggal:T', title='Tanggal'),
    y=alt.Y('Volume:Q', title='Volume'),
    tooltip=['Tanggal', 'Volume']
).properties(width=800, height=400)

st.altair_chart(chart, use_container_width=True)
