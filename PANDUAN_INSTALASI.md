# 📖 PANDUAN INSTALASI LENGKAP - Aplikasi Manajemen Data Rekening Bank

## 🎯 Tujuan
Membuat sistem manajemen data rekening bank berbasis localhost dengan database lokal yang aman dan mudah digunakan.

---

## 📋 PERSIAPAN

### Yang Anda Butuhkan:
1. **Python** versi 3.7 atau lebih tinggi
2. **pip** (biasanya sudah included dengan Python)
3. **Browser** (Chrome, Firefox, Edge, Safari, dll)
4. **Folder** untuk menyimpan aplikasi

### Cek Instalasi Python

**Untuk Windows:**
```
Tekan: Windows + R
Ketik: cmd
Tekan: Enter

Lalu ketik:
python --version
```

**Untuk Mac/Linux:**
```
Buka Terminal
Ketik: python3 --version
```

Jika muncul versi Python, berarti Python sudah terinstall ✓

---

## 🚀 LANGKAH INSTALASI

### LANGKAH 1: Download/Ekstrak File

1. Ekstrak semua file aplikasi ke folder di komputer Anda
   - Contoh: `C:\Bank_App` (Windows)
   - Contoh: `~/bank_app` (Mac/Linux)

2. Folder harus berisi:
   ```
   bank_app/
   ├── bank_app.py
   ├── requirements.txt
   ├── README.md
   ├── QUICK_START.txt
   ├── export_to_csv.py
   ├── templates/
   │   └── index.html
   └── static/
       ├── css/style.css
       └── js/script.js
   ```

### LANGKAH 2: Install Dependencies

**Untuk Windows:**
```
1. Buka Command Prompt (Windows + R → cmd → Enter)
2. Masuk ke folder aplikasi:
   cd C:\Users\YourName\Desktop\bank_app

3. Install Flask:
   pip install -r requirements.txt
```

**Untuk Mac:**
```
1. Buka Terminal
2. Masuk ke folder aplikasi:
   cd ~/bank_app

3. Install Flask:
   pip install -r requirements.txt
```

**Untuk Linux:**
```
1. Buka Terminal
2. Masuk ke folder aplikasi:
   cd ~/bank_app

3. Install Flask:
   pip install -r requirements.txt
```

✅ Tunggu proses instalasi selesai (biasanya 1-2 menit)

### LANGKAH 3: Jalankan Aplikasi

**Untuk Windows:**
```
Masih di Command Prompt yang sama, ketik:
python bank_app.py
```

**Untuk Mac/Linux:**
```
Masih di Terminal yang sama, ketik:
python3 bank_app.py
```

Jika berhasil, Anda akan melihat:
```
🏦 Server berjalan di http://localhost:5000
Database: rekening_bank.db
```

### LANGKAH 4: Akses Aplikasi

1. Buka browser favorit Anda (Chrome, Firefox, dll)
2. Ketik di address bar:
   ```
   http://localhost:5000
   ```
3. Tekan Enter

✅ Aplikasi siap digunakan!

---

## 💻 MENGGUNAKAN APLIKASI

### Menambah Rekening Baru

1. Scroll ke bagian "Tambah Rekening Baru"
2. Isi form dengan data:
   - **Nama Rekening**: Contoh: "Rekening Operasional BCA"
   - **Nomor Rekening**: Contoh: "1234567890123456" (16 digit)
   - **Jenis Bank**: Pilih dari dropdown
   - **Status Bank** ✨: Pilih:
     - "✓ Bank Aktif" - untuk rekening yang sedang digunakan
     - "✗ Bank Tidak Aktif" - untuk rekening yang tidak digunakan
   - **Keterangan**: Opsional, contoh: "Untuk transaksi harian"
3. Klik tombol "Simpan Rekening" berwarna ungu

### Melihat Daftar Rekening

Di bagian "Daftar Rekening" akan muncul tabel dengan semua rekening yang sudah ditambahkan.

Tabel menampilkan:
- No (urutan)
- Nama Rekening
- Nomor Rekening (bold)
- Jenis Bank
- **Status** ✨ (Aktif/Tidak Aktif dengan warna badge):
  - 🟢 Hijau untuk "✓ Bank Aktif"
  - 🔴 Merah untuk "✗ Bank Tidak Aktif"
- Keterangan
- Tombol Aksi (Edit/Hapus)

### Mengedit Rekening

1. Cari rekening di tabel yang ingin diubah
2. Klik tombol "Edit" (hijau)
3. Modal akan muncul dengan data yang sudah terisi:
   - Nama Rekening
   - Nomor Rekening
   - Jenis Bank
   - **Status Bank** ✨ (dropdown)
   - Keterangan
4. Lakukan perubahan yang diperlukan
5. Anda bisa mengubah status dari "Aktif" menjadi "Tidak Aktif" atau sebaliknya
6. Klik "Perbarui Rekening"

### Menghapus Rekening

1. Cari rekening di tabel yang ingin dihapus
2. Klik tombol "Hapus" (merah)
3. Sistem akan meminta konfirmasi: "Apakah Anda yakin ingin menghapus rekening ini?"
4. Klik "OK" untuk mengkonfirmasi
5. Rekening akan dihapus

---

## 💾 BACKUP DATA

### Menggunakan Script Export

**Export ke CSV (Backup):**
```
1. Buka Command Prompt/Terminal
2. Masuk ke folder aplikasi
3. Ketik: python export_to_csv.py

Hasil: File CSV akan dibuat dengan nama seperti:
       rekening_bank_backup_20240315_143022.csv
```

**Import dari CSV:**
```
1. Buka Command Prompt/Terminal
2. Masuk ke folder aplikasi
3. Ketik: python export_to_csv.py --import nama_file.csv

Contoh: python export_to_csv.py --import data_lama.csv
```

### Backup Manual

Untuk backup data secara manual:
1. Cari file `rekening_bank.db` di folder aplikasi
2. Copy file tersebut ke folder lain/storage eksternal
3. Simpan dengan nama: `rekening_bank_backup_[tanggal].db`

---

## 🛑 MENGHENTIKAN APLIKASI

**Untuk menghentikan server:**
```
Di Command Prompt/Terminal, tekan: CTRL + C

Anda akan melihat pesan untuk konfirmasi shutdown
```

Setelah itu:
- Aplikasi akan berhenti
- Anda tetap bisa akses file database
- Untuk menjalankan lagi, ulang LANGKAH 3

---

## 🔧 TROUBLESHOOTING

### ❌ "Kesalahan: Python tidak ditemukan"
**Solusi:**
1. Install Python dari https://www.python.org/downloads/
2. Saat install, pastikan centang: "Add Python to PATH"
3. Restart Command Prompt/Terminal

### ❌ "Kesalahan: Port 5000 sudah digunakan"
**Solusi:**
1. Buka file `bank_app.py` dengan text editor
2. Cari baris paling akhir: `app.run(debug=True, port=5000)`
3. Ubah port ke port lain: `app.run(debug=True, port=5001)`
4. Jalankan aplikasi lagi
5. Akses di browser: http://localhost:5001

### ❌ "ModuleNotFoundError: No module named 'flask'"
**Solusi:**
1. Install ulang dependencies:
   ```
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

### ❌ "Database error" saat menjalankan
**Solusi:**
1. Hapus file `rekening_bank.db` (jika ada)
2. Jalankan aplikasi lagi
3. Database akan dibuat otomatis

### ❌ "Cannot access localhost:5000"
**Solusi:**
1. Pastikan aplikasi sedang berjalan (lihat Command Prompt/Terminal)
2. Refresh browser (F5 atau Ctrl+R)
3. Coba URL: http://127.0.0.1:5000 (sama dengan localhost)

---

## 📱 STRUKTUR DATABASE

Aplikasi menggunakan SQLite dengan tabel berikut:

```
TABEL: rekening

Kolom:
┌──────────────────┬───────────────────┬──────────────┐
│ Nama Kolom       │ Tipe Data         │ Deskripsi    │
├──────────────────┼───────────────────┼──────────────┤
│ id               │ INTEGER PRIMARY   │ ID unik      │
│                  │ KEY AUTOINCREMENT │              │
├──────────────────┼───────────────────┼──────────────┤
│ nama_rekening    │ TEXT NOT NULL     │ Nama rek.    │
├──────────────────┼───────────────────┼──────────────┤
│ no_rekening      │ TEXT NOT NULL     │ No rek unik  │
│                  │ UNIQUE            │              │
├──────────────────┼───────────────────┼──────────────┤
│ jenis_bank       │ TEXT NOT NULL     │ Bank type    │
├──────────────────┼───────────────────┼──────────────┤
│ keterangan       │ TEXT              │ Catatan      │
├──────────────────┼───────────────────┼──────────────┤
│ tanggal_dibuat   │ TIMESTAMP         │ Created at   │
└──────────────────┴───────────────────┴──────────────┘
```

---

## 🌐 INTEGRASI DENGAN BOT TELEGRAM

Jika Anda ingin mengintegrasikan dengan bot Telegram:

```python
# Contoh kode untuk ambil data dari database
import sqlite3

db = sqlite3.connect('rekening_bank.db')
cursor = db.execute('SELECT * FROM rekening')
rekenings = cursor.fetchall()

for rek in rekenings:
    print(f"Rekening: {rek[1]} ({rek[3]})")
```

---

## 🔒 KEAMANAN

### Catatan Penting:
✓ Database disimpan lokal di komputer Anda - AMAN
✓ Tidak ada data yang terkirim ke internet
✓ Nomor rekening tidak boleh duplikat (validasi otomatis)
✓ Backup data secara berkala

### Tips Keamanan:
1. Backup data minimal 1x seminggu
2. Jangan bagikan file `rekening_bank.db`
3. Gunakan password yang kuat untuk komputer Anda
4. Simpan backup di lokasi aman (cloud, USB eksternal, dll)

---

## 📞 DUKUNGAN

Jika ada pertanyaan atau masalah:
1. Baca file `README.md`
2. Cek bagian TROUBLESHOOTING di atas
3. Pastikan semua file sudah berada di folder yang benar

---

## ✅ CHECKLIST SETELAH INSTALASI

- [ ] Python terinstall dan versi ≥ 3.7
- [ ] Dependencies sudah di-install (pip install -r requirements.txt)
- [ ] Aplikasi berjalan tanpa error (python bank_app.py)
- [ ] Browser bisa akses http://localhost:5000
- [ ] Bisa menambah rekening baru
- [ ] Bisa melihat daftar rekening
- [ ] Database `rekening_bank.db` sudah dibuat

---

## 🎉 SELESAI!

Aplikasi Anda sudah siap digunakan untuk manajemen data rekening bank!

Nikmati kemudahan pengelolaan data dengan sistem yang aman dan terpercaya. 🚀
