# ⚔️ Sambung Kata — Predator Mode

Game sambung kata berbasis KBBI dengan strategi huruf langka. Dibangun dengan Streamlit.

## 🎮 Cara Main

1. Ketik awalan kata di kolom pencarian
2. Pilih kata dari daftar yang muncul
3. Kata berikutnya harus dimulai dari **huruf terakhir** kata yang dipilih
4. Strategi: pilih kata yang berakhiran **huruf predator** untuk menyulitkan lawan!

## 🔥 Huruf Predator

| Huruf | Keterangan |
|-------|------------|
| **Q** | Sangat langka |
| **X** | Sangat langka |
| **Z** | Langka |
| **V** | Langka |
| **F** | Langka |

Kata yang berakhiran huruf ini ditandai **merah** — sulit dilanjutkan lawan!

## 🗄️ Database

72.000+ kata dari KBBI (Kamus Besar Bahasa Indonesia)

## 🚀 Jalankan Lokal

```bash
pip install streamlit
streamlit run app.py
```

## 🌐 Deploy

Live di Streamlit Cloud: [sambung-kata.streamlit.app](https://sambung-kata.streamlit.app)

---

© 2026 yuambubulabu
