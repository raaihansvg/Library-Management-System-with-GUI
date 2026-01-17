# 📚 Library Management System with GUI

Library Management System adalah aplikasi berbasis **Python** dengan **Graphical User Interface (GUI)** yang dibuat menggunakan **CustomTkinter**.  
Aplikasi ini mensimulasikan sistem manajemen perpustakaan sederhana seperti peminjaman buku, pengembalian, reservasi, dan pelacakan status buku.

---

## ✨ Features

- 📖 Peminjaman buku
- 🔄 Pengembalian buku
- ⏳ Cek batas waktu peminjaman
- 📝 Reservasi buku (antrian peminjam)
- 🔁 Perpanjangan masa pinjam (maksimal 2 kali)
- 📚 Daftar buku dan status ketersediaan
- 📜 Riwayat peminjaman
- 🔍 Pelacakan status buku secara real-time

---

## 🛠️ Tech Stack

- **Python**
- **CustomTkinter**
- **Tkinter**
- **Datetime**

---

## 🧠 System Logic Overview

- Data buku disimpan dalam struktur **dictionary**
- Setiap buku memiliki:
  - status (tersedia / tidak tersedia)
  - peminjam
  - tanggal pinjam
  - jumlah perpanjangan
  - antrian reservasi
- Riwayat peminjaman dicatat berdasarkan nama peminjam

---

## ▶️ How to Run

1. Pastikan Python sudah terinstall
2. Install dependency:
   ```bash
   pip install customtkinter
   ```
3. Jalankan Program:
   ```bash
   python Perpus.py
   ```
