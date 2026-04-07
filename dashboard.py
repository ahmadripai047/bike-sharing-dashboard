import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

df = pd.read_csv("Bike_sharing_dataset.csv")
df.columns = df.columns.str.strip()
df = df.drop_duplicates(subset=['dteday'], keep='first')
df['dteday'] = pd.to_datetime(df['dteday'])
df['season_label'] = df['season'].map({
    1: 'Springer', 2: 'Summer', 3: 'Fall', 4: 'Winter'
})

st.title('Dashboard Bike Sharing Dataset')
st.metric("Total sewa", value=df['cnt'].sum())

st.subheader('Bar Chart jumlah penyewaan sepeda berdasarkan musim')
season_counts = df.groupby('season_label')['cnt'].sum().reindex(
    ['Springer', 'Summer', 'Fall', 'Winter']
)
fig1, ax1 = plt.subplots()
season_counts.plot(kind='bar', ax=ax1,
    color=['#00b4d8','#00b4d8','#023e8a','#00b4d8'])
plt.xticks([0,1,2,3], ['Springer','Summer','Fall','Winter'], rotation=45)
plt.tight_layout()
st.pyplot(fig1)
plt.close(fig1)

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

st.subheader('Korelasi Spearman antar variabel')
corr = df[['temp','hum','windspeed','cnt']].corr(method='spearman')
fig3, ax3 = plt.subplots()
sns.heatmap(corr, annot=True, annot_kws={'size':16}, cmap='Blues', ax=ax3)
plt.title("Korelasi Spearman")
plt.tight_layout()
st.pyplot(fig3)
plt.close(fig3)

st.caption('Copyright (c) Muhammad Rifai 2024')