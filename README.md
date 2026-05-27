# Sistem Pemesanan Tiket Bioskop (UKPL Project)

Proyek ini dibuat untuk memenuhi **Tugas 4 mata kuliah Uji Kualitas Perangkat Lunak (UKPL)**. Proyek ini mengimplementasikan aplikasi pemesanan tiket bioskop dalam dua versi untuk menunjukkan perbedaan implementasi antarmuka namun dengan logika pengujian yang sama.

---

## 🎯 Identitas Tugas
- **Mata Kuliah:** Uji Kualitas Perangkat Lunak (UKPL)
- **Tugas:** Tugas 4 - Blackbox Testing
- **Topik:** Aplikasi Pemesanan Tiket Bioskop Berbasis Python

## 📂 Struktur Repositori
- `test.py`: Versi *Command Line Interface* (CLI) untuk pengujian logika dasar.
- `app.py`: Versi *Web-based* menggunakan **Streamlit** untuk antarmuka yang lebih menarik.

## 🛠️ Metodologi Pengujian
Aplikasi ini diuji menggunakan dua teknik pengujian standar untuk memastikan kualitas perangkat lunak:

1. **Boundary Value Analysis (BVA):**
   - Validasi batasan input jumlah tiket (1–10).
   - Memastikan aplikasi menangani nilai batas bawah (0) dan batas atas (11) dengan pesan kesalahan yang tepat.

2. **State Transition Testing (STT):**
   - Memverifikasi perpindahan status sistem (*Login → Pemesanan → Pembayaran → Struk*).
   - Memastikan sistem memiliki *error handling* (tidak *crash*) saat diberikan input tidak valid di setiap *state*.

## 🚀 Cara Menjalankan

### Persiapan
Pastikan Python sudah terinstal di perangkat Anda.

### 1. Menjalankan Versi CLI
```bash
python code.py
```
### 2. Menjalankan Versi Streamlit (Web)
Install dependensi yang diperlukan:
```bash
pip install streamlit
```
Jalankan aplikasi:
```bash
streamlit run app.py
```

## 📊 Hasil Pengujian
Proyek ini telah melalui tahap pengujian fungsionalitas dengan hasil Pass. Dokumentasi lengkap mengenai tabel skenario pengujian dan State Transition Diagram tersedia di dalam laporan tugas.
