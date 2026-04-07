## 🔗 Live Dashboard
👉 [Klik di sini untuk melihat Dashboard](https://bike-sharing-dashboard-proyek-bangkit.streamlit.app/)

# 🚲 Bike Sharing Dashboard

## 📋 Deskripsi Proyek
Proyek analisis data ini bertujuan untuk mengeksplorasi dataset **Bike Sharing** guna menjawab pertanyaan bisnis terkait pola penyewaan sepeda berdasarkan musim dan jenis pelanggan. Dashboard interaktif dibangun menggunakan **Streamlit**.

- **Nama:** Muhammad Rifai
- **Email:** ahmadripai.wijaya04@gmail.com
- **ID Dicoding:** 7729510

---

## ❓ Pertanyaan Bisnis
1. Pada musim apa jumlah penyewaan sepeda paling tinggi?
2. Bagaimana pola penggunaan sepeda antara pelanggan **casual** dan **registered** dari waktu ke waktu?

---

## 📁 Struktur Direktori
```
submission/
├── dashboard/
│   ├── dashboard.py
│   └── Bike_sharing_dataset.csv
├── Proyek_Bangkit.ipynb
├── requirements.txt
└── README.md
```

---

## 🛠️ Library yang Digunakan
- **pandas** — manipulasi dan analisis data
- **matplotlib** — visualisasi data
- **seaborn** — visualisasi statistik
- **streamlit** — membuat dashboard interaktif

---

## ⚙️ Cara Menjalankan Dashboard

### 1. Clone Repository
```bash
git clone https://github.com/ahmadripai047/bike-sharing-dashboard.git
cd bike-sharing-dashboard
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Jalankan Dashboard
```bash
cd dashboard
streamlit run dashboard.py
```

### 4. Buka Browser
Akses dashboard di: `http://localhost:8501`

---

## 📊 Hasil Analisis

### Pertanyaan 1: Penyewaan per Musim
Musim **Fall (Gugur)** memiliki jumlah penyewaan tertinggi dengan total **1.061.129** penyewaan, diikuti Summer, Winter, dan Springer. Hal ini menunjukkan bahwa cuaca yang tidak terlalu panas maupun dingin mendorong lebih banyak orang untuk menyewa sepeda.

| Musim | Jumlah Penyewaan |
|-------|-----------------|
| Springer | 471.348 |
| Summer | 918.589 |
| **Fall** | **1.061.129** |
| Winter | 841.613 |

### Pertanyaan 2: Pola Casual vs Registered
Pelanggan **registered** secara konsisten mendominasi penggunaan sepeda dibanding **casual** di sepanjang waktu. Pelanggan casual cenderung meningkat pada musim tertentu (puncak di musim panas), sementara registered lebih stabil, mengindikasikan penggunaan rutin seperti commuting.

---

## 📝 Kesimpulan
- Musim **Fall** adalah waktu terbaik untuk promosi penyewaan sepeda karena permintaan tertinggi.
- Strategi pemasaran untuk pelanggan **casual** dapat difokuskan pada musim panas, sedangkan layanan untuk **registered** perlu konsisten sepanjang tahun.

---

## 📄 Requirements
```
pandas
matplotlib
seaborn
streamlit
```

---

*Copyright © Muhammad Rifai 2024*
