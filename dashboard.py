import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Load Data
df = pd.read_csv("Bike_sharing_dataset.csv")
df['dteday'] = pd.to_datetime(df['dteday'])

# Header
st.title('Dashboard Bike Sharing Dataset')
total = df['cnt'].sum()
st.metric("Total sewa", value=total)

# ── Visualisasi 1: Bar Chart per Musim ───────────────────────────
st.subheader('Bar Chart jumlah penyewaan sepeda berdasarkan musim')

season_counts = df.groupby(by=df.season).cnt.sum()

fig1, ax1 = plt.subplots()
season_counts.plot(
    kind='bar',
    xlabel='Musim',
    ylabel='Jumlah Penyewaan',
    title='Jumlah Penyewaan Sepeda Berdasarkan Musim',
    color=['#00b4d8','#00b4d8','#023e8a','#00b4d8'],
    ax=ax1
)
plt.xticks([0, 1, 2, 3], ['Springer','Summer', 'Fall', 'Winter'], rotation=45)
plt.tight_layout()
st.pyplot(fig1)
plt.close(fig1)

# ── Visualisasi 2: Pola Casual vs Registered ─────────────────────
st.subheader('Pola Data berdasarkan jenis pelanggan')

fig2, ax2 = plt.subplots(figsize=(12, 5))
ax2.plot(df['dteday'], df['casual'], label='casual', color='red')
ax2.plot(df['dteday'], df['registered'], label='registered', color='blue')
ax2.set_xlabel('date', size=15)
ax2.set_ylabel('Jumlah Pengunaan', size=15)
ax2.legend()
plt.tight_layout()
st.pyplot(fig2)
plt.close(fig2)

# ── Visualisasi 3: Korelasi Spearman ─────────────────────────────
st.subheader('Korelasi Spearman antar variabel')

correlation_matrix = df[['temp','hum','windspeed','cnt']].corr(method='spearman')

fig3, ax3 = plt.subplots()
sns.heatmap(
    data=correlation_matrix,
    annot=True,
    annot_kws={'size': 16},
    cmap='Blues',
    ax=ax3
)
plt.title("Korelasi Spearman")
plt.tight_layout()
st.pyplot(fig3)
plt.close(fig3)

st.caption('Copyright (c) Muhammad Rifai 2024')