import customtkinter as ctk
from datetime import datetime, timedelta
from tkinter import messagebox

# Daftar Buku di Perpustakaan
buku_perpustakaan = {
    "Buku A": {"kategori": "Fiksi", "status": "tersedia", "peminjam": None, "antrian": [], "tanggal_pinjam": None, "perpanjangan": 0},
    "Buku B": {"kategori": "Non-Fiksi", "status": "tersedia", "peminjam": None, "antrian": [], "tanggal_pinjam": None, "perpanjangan": 0},
    "Buku C": {"kategori": "Ilmu Pengetahuan", "status": "tersedia", "peminjam": None, "antrian": [], "tanggal_pinjam": None, "perpanjangan": 0},
    "Buku D": {"kategori": "Fiksi", "status": "tersedia", "peminjam": None, "antrian": [], "tanggal_pinjam": None, "perpanjangan": 0},
    "Buku E": {"kategori": "Sejarah", "status": "tersedia", "peminjam": None, "antrian": [], "tanggal_pinjam": None, "perpanjangan": 0},
    "Buku F": {"kategori": "Teknologi", "status": "tersedia", "peminjam": None, "antrian": [], "tanggal_pinjam": None, "perpanjangan": 0},
}

riwayat_peminjaman = {}
DURASI_PEMINJAMAN = 7

# Setup GUI CustomTkinter
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Sistem Manajemen Perpustakaan")
app.geometry("600x600")

# Function untuk membersihkan frame
def clear_frame():
    for widget in app.winfo_children():
        widget.pack_forget()

# Fungsi untuk membuat entry fields
def create_entry_fields():
    nama_label = ctk.CTkLabel(app, text="Nama Peminjam:")
    nama_label.pack(pady=5)
    nama_entry = ctk.CTkEntry(app)
    nama_entry.pack(pady=5)
    
    buku_label = ctk.CTkLabel(app, text="Judul Buku:")
    buku_label.pack(pady=5)
    buku_entry = ctk.CTkEntry(app)
    buku_entry.pack(pady=5)

    return nama_entry, buku_entry

# Fungsi untuk kembali ke halaman utama
def home_button():
    ctk.CTkButton(app, text="Kembali ke Halaman Utama", command=home_page).pack(pady=10)

# Fungsi halaman utama
def home_page():
    clear_frame()
    welcome_label = ctk.CTkLabel(app, text="📚 Selamat Datang di Perpustakaan", font=("Arial", 16, "bold"))
    welcome_label.pack(pady=20)

    buttons = [
        ("📖 Pinjam Buku", go_to_pinjam_buku),
        ("🔄 Kembalikan Buku", go_to_kembalikan_buku),
        ("⏳ Cek Batas Waktu", go_to_cek_batas_waktu),
        ("📝 Reservasi Buku", go_to_reservasi_buku),
        ("🔄 Perpanjang Peminjaman", go_to_perpanjang_peminjaman),
        ("📚 Tampilkan Daftar Buku", go_to_tampilkan_daftar_buku),
        ("📜 Lihat Riwayat Peminjaman", go_to_riwayat),
        ("🔍 Lacak Status Buku", go_to_lacak_status_buku)
    ]
    
    for text, command in buttons:
        button = ctk.CTkButton(app, text=text, command=command)
        button.pack(pady=5)
    
    # Tambahkan tombol Exit
    ctk.CTkButton(app, text="Keluar", command=app.quit).pack(pady=20)

# Fungsi untuk Pinjam Buku
def go_to_pinjam_buku():
    clear_frame()
    title_label = ctk.CTkLabel(app, text="📖 Pinjam Buku", font=("Arial", 14, "bold"))
    title_label.pack(pady=10)
    nama_entry, buku_entry = create_entry_fields()
    
    def pinjam_buku_action():
        nama_peminjam = nama_entry.get().strip()
        buku = buku_entry.get().strip()
        if not nama_peminjam or not buku:
            messagebox.showerror("Gagal", "Nama peminjam dan judul buku tidak boleh kosong.")
            return
        
        if buku in buku_perpustakaan and buku_perpustakaan[buku]["status"] == "tersedia":
            buku_perpustakaan[buku]["status"] = "tidak tersedia"
            buku_perpustakaan[buku]["peminjam"] = nama_peminjam
            buku_perpustakaan[buku]["tanggal_pinjam"] = datetime.now()
            riwayat_peminjaman.setdefault(nama_peminjam, []).append({"buku": buku, "tanggal_pinjam": datetime.now()})
            messagebox.showinfo("Sukses", "Berhasil Meminjam Buku")
        else:
            messagebox.showerror("Gagal", "Buku tidak tersedia atau tidak ditemukan.")
    
    ctk.CTkButton(app, text="Pinjam Buku", command=pinjam_buku_action).pack(pady=10)
    home_button()

# Fungsi untuk Kembalikan Buku
def go_to_kembalikan_buku():
    clear_frame()
    title_label = ctk.CTkLabel(app, text="🔄 Kembalikan Buku", font=("Arial", 14, "bold"))
    title_label.pack(pady=10)
    nama_entry, buku_entry = create_entry_fields()

    def kembalikan_buku_action():
        nama_peminjam = nama_entry.get().strip()
        buku = buku_entry.get().strip()
        if not nama_peminjam or not buku:
            messagebox.showerror("Gagal", "Nama peminjam dan judul buku tidak boleh kosong.")
            return
        
        if buku in buku_perpustakaan and buku_perpustakaan[buku]["peminjam"] == nama_peminjam:
            buku_perpustakaan[buku]["status"] = "tersedia"
            buku_perpustakaan[buku]["peminjam"] = None
            buku_perpustakaan[buku]["tanggal_pinjam"] = None
            buku_perpustakaan[buku]["perpanjangan"] = 0
            messagebox.showinfo("Sukses", "Buku Berhasil Dikembalikan")
        else:
            messagebox.showerror("Gagal", "Buku tidak ditemukan atau tidak sedang dipinjam.")
    
    ctk.CTkButton(app, text="Kembalikan Buku", command=kembalikan_buku_action).pack(pady=10)
    home_button()

# Fungsi untuk Cek Batas Waktu
def go_to_cek_batas_waktu():
    clear_frame()
    title_label = ctk.CTkLabel(app, text="⏳ Cek Batas Waktu", font=("Arial", 14, "bold"))
    title_label.pack(pady=10)
    nama_entry, buku_entry = create_entry_fields()
    
    def cek_batas_waktu_action():
        nama_peminjam = nama_entry.get().strip()
        buku = buku_entry.get().strip()
        if not nama_peminjam or not buku:
            messagebox.showerror("Gagal", "Nama peminjam dan judul buku tidak boleh kosong.")
            return
        
        if buku in buku_perpustakaan and buku_perpustakaan[buku]["peminjam"] == nama_peminjam:
            tanggal_pinjam = buku_perpustakaan[buku]["tanggal_pinjam"]
            batas_waktu = tanggal_pinjam + timedelta(days=DURASI_PEMINJAMAN)
            hari_tersisa = (batas_waktu - datetime.now()).days
            if hari_tersisa >= 0:
                messagebox.showinfo("Batas Waktu", f"Sisa waktu peminjaman: {hari_tersisa} hari.")
            else:
                messagebox.showwarning("Terlambat", f"Buku '{buku}' terlambat dikembalikan selama {-hari_tersisa} hari.")
        else:
            messagebox.showerror("Gagal", f"{nama_peminjam} tidak meminjam buku '{buku}'.")

    ctk.CTkButton(app, text="Cek Batas Waktu", command=cek_batas_waktu_action).pack(pady=10)
    home_button()

# Fungsi untuk Reservasi Buku
def go_to_reservasi_buku():
    clear_frame()
    title_label = ctk.CTkLabel(app, text="📝 Reservasi Buku", font=("Arial", 14, "bold"))
    title_label.pack(pady=10)
    nama_entry, buku_entry = create_entry_fields()
    
    def reservasi_buku_action():
        nama_peminjam = nama_entry.get().strip()
        buku = buku_entry.get().strip()
        if not nama_peminjam or not buku:
            messagebox.showerror("Gagal", "Nama peminjam dan judul buku tidak boleh kosong.")
            return
        
        if buku in buku_perpustakaan:
            if buku_perpustakaan[buku]["status"] == "tersedia":
                messagebox.showinfo("Tersedia", "Buku tersedia untuk dipinjam langsung.")
            else:
                buku_perpustakaan[buku]["antrian"].append(nama_peminjam)
                messagebox.showinfo("Reservasi Berhasil", f"{nama_peminjam} telah ditambahkan ke dalam antrian untuk buku '{buku}'.")
        else:
            messagebox.showerror("Gagal", "Buku tidak ditemukan.")

    ctk.CTkButton(app, text="Reservasi Buku", command=reservasi_buku_action).pack(pady=10)
    home_button()

# Fungsi Perpanjang Peminjaman
def go_to_perpanjang_peminjaman():
    clear_frame()
    title_label = ctk.CTkLabel(app, text="🔄 Perpanjang Peminjaman", font=("Arial", 14, "bold"))
    title_label.pack(pady=10)
    nama_entry, buku_entry = create_entry_fields()

    def perpanjang_peminjaman_action():
        nama_peminjam = nama_entry.get().strip()
        buku = buku_entry.get().strip()
        if not nama_peminjam or not buku:
            messagebox.showerror("Gagal", "Nama peminjam dan judul buku tidak boleh kosong.")
            return

        if buku in buku_perpustakaan and buku_perpustakaan[buku]["peminjam"] == nama_peminjam:
            if buku_perpustakaan[buku]["perpanjangan"] < 2:
                buku_perpustakaan[buku]["tanggal_pinjam"] = datetime.now()
                buku_perpustakaan[buku]["perpanjangan"] += 1
                messagebox.showinfo("Berhasil", f"Peminjaman untuk buku '{buku}' berhasil diperpanjang.")
            else:
                messagebox.showerror("Gagal", "Buku telah diperpanjang 2 kali dan tidak bisa diperpanjang lagi.")
        else:
            messagebox.showerror("Gagal", "Buku tidak ditemukan atau tidak sedang dipinjam.")

    ctk.CTkButton(app, text="Perpanjang Peminjaman", command=perpanjang_peminjaman_action).pack(pady=10)
    home_button()

# Fungsi Tampilkan Daftar Buku
def go_to_tampilkan_daftar_buku():
    clear_frame()
    title_label = ctk.CTkLabel(app, text="📚 Daftar Buku", font=("Arial", 14, "bold"))
    title_label.pack(pady=10)
    
    for buku, data in buku_perpustakaan.items():
        info = f"{buku} ({data['kategori']}) - {data['status']}"
        ctk.CTkLabel(app, text=info).pack(pady=2)

    home_button()

# Fungsi Lihat Riwayat
def go_to_riwayat():
    clear_frame()
    title_label = ctk.CTkLabel(app, text="📜 Riwayat Peminjaman", font=("Arial", 14, "bold"))
    title_label.pack(pady=10)
    
    for peminjam, riwayat in riwayat_peminjaman.items():
        for item in riwayat:
            buku_info = f"{peminjam} meminjam '{item['buku']}' pada {item['tanggal_pinjam'].strftime('%Y-%m-%d')}"
            ctk.CTkLabel(app, text=buku_info).pack(pady=2)

    home_button()

# Fungsi Lacak Status Buku
def go_to_lacak_status_buku():
    clear_frame()
    title_label = ctk.CTkLabel(app, text="🔍 Lacak Status Buku", font=("Arial", 14, "bold"))
    title_label.pack(pady=10)
    buku_entry = ctk.CTkEntry(app)
    buku_entry.pack(pady=5)
    buku_entry.insert(0, "Masukkan judul buku")

    def lacak_status_action():
        buku = buku_entry.get().strip()
        if buku in buku_perpustakaan:
            status = buku_perpustakaan[buku]["status"]
            peminjam = buku_perpustakaan[buku]["peminjam"]
            info = f"Status buku: {status}."
            if peminjam:
                info += f" Saat ini dipinjam oleh {peminjam}."
            if buku_perpustakaan[buku]["antrian"]:
                info += f" Antrian: {', '.join(buku_perpustakaan[buku]['antrian'])}."
            messagebox.showinfo("Status Buku", info)
        else:
            messagebox.showerror("Gagal", "Buku tidak ditemukan.")

    ctk.CTkButton(app, text="Lacak Status Buku", command=lacak_status_action).pack(pady=10)
    home_button()

# Tampilkan Halaman Utama
home_page()
app.mainloop()
