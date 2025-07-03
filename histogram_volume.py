import streamlit as st
import pandas as pd
import altair as alt

# Data
data = {
    "Tanggal": [
        "30/12/2022", "29/12/2022", "28/12/2022", "27/12/2022", "23/12/2022", "22/12/2022",
        "21/12/2022", "20/12/2022", "19/12/2022", "16/12/2022", "15/12/2022", "14/12/2022",
        "13/12/2022", "12/12/2022", "12/09/2022", "12/08/2022", "12/07/2022", "12/06/2022",
        "12/05/2022", "12/02/2022", "12/01/2022"
    ],
    "Volume": [
        10750000, 10599000, 11808000, 15962000, 10546000, 17577000,
        11018000, 19750000, 8609000, 12875000, 18532000, 14380000,
        23091000, 10778000, 15094000, 11627000, 15557000, 12786000,
        17982000, 18372000, 22615000
    ]
}

df = pd.DataFrame(data)
df["Tanggal"] = pd.to_datetime(df["Tanggal"], dayfirst=True)

# Judul
st.title("Grafik Histogram Volume Penjualan per Hari")

# Grafik
bar_chart = alt.Chart(df).mark_bar(color='skyblue').encode(
    x=alt.X('Tanggal:T', title='Tanggal'),
    y=alt.Y('Volume:Q', title='Volume'),
    tooltip=['Tanggal', 'Volume']
).properties(width=800, height=400).configure_axisX(labelAngle=45)

st.altair_chart(bar_chart, use_container_width=True)
