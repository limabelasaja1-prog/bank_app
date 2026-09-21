# 🏦 Aplikasi Manajemen Data Rekening Bank

Aplikasi berbasis localhost untuk mengelola data rekening bank Anda dengan antarmuka web yang user-friendly.

## 📋 Fitur

- ✅ Tambah rekening bank baru
- ✅ Edit data rekening
- ✅ Hapus rekening
- ✅ Lihat daftar semua rekening
- ✅ **Status Bank** - Tandai rekening sebagai Aktif atau Tidak Aktif
- ✅ **Visual Badge** - Status ditampilkan dengan warna untuk kemudahan identifikasi
- ✅ Database lokal (SQLite) - disimpan di komputer Anda
- ✅ Interface web yang responsif dan modern
- ✅ Tidak perlu koneksi internet
- ✅ Export/Import data ke CSV

## 📦 Persyaratan

- Python 3.7 atau lebih tinggi
- pip (Package manager Python)

## 🚀 Cara Menggunakan

### 1. Setup Initial

**Langkah 1:** Install dependencies
```bash
pip install -r requirements.txt
```

**Langkah 2:** Jalankan aplikasi
```bash
python bank_app.py
```

Anda akan melihat output:
```
🏦 Server berjalan di http://localhost:5000
Database: rekening_bank.db
```

**Langkah 3:** Buka browser dan akses:
```
http://localhost:5000
```

### 2. Menggunakan Aplikasi

#### Tambah Rekening Baru
1. Isi form "Tambah Rekening Baru" dengan data:
   - **Nama Rekening**: Nama/identitas rekening (contoh: "Rekening Operasional")
   - **Nomor Rekening**: Nomor rekening 16-20 digit
   - **Jenis Bank**: Pilih dari dropdown (BRI, BCA, Mandiri, dll)
   - **Keterangan**: Catatan tambahan (opsional)
2. Klik tombol "Simpan Rekening"

#### Edit Rekening
1. Klik tombol "Edit" pada baris rekening yang ingin diubah
2. Modal akan terbuka dengan data yang sudah terisi
3. Lakukan perubahan yang diperlukan
4. Klik "Perbarui Rekening"

#### Hapus Rekening
1. Klik tombol "Hapus" pada baris rekening
2. Konfirmasi penghapusan
3. Data akan dihapus dari database

## 📁 Struktur File

```
├── bank_app.py              # File utama aplikasi Flask
├── requirements.txt         # Dependencies Python
├── rekening_bank.db         # Database SQLite (otomatis dibuat)
├── templates/
│   └── index.html          # Template HTML
└── static/
    ├── css/
    │   └── style.css       # Styling CSS
    └── js/
        └── script.js       # JavaScript untuk interaksi
```

## 💾 Lokasi Database

Database file `rekening_bank.db` akan disimpan di folder yang sama dengan `bank_app.py`.

Untuk melihat lokasi database:
- **Windows**: Cek di folder project Anda (misalnya `C:\Users\YourName\Desktop\bank_app`)
- **Mac/Linux**: Cek di folder project Anda (misalnya `~/bank_app`)

## 🔧 Menghentikan Aplikasi

Tekan `Ctrl + C` di terminal untuk menghentikan server.

## 📊 Struktur Database

Tabel `rekening`:
```
- id (Primary Key)
- nama_rekening (Text) - Nama/identitas rekening
- no_rekening (Text, Unique) - Nomor rekening (tidak boleh duplikat)
- jenis_bank (Text) - Jenis bank (BRI, BCA, Mandiri, dll)
- status (Text) - Status: 'aktif' atau 'tidak_aktif'
- keterangan (Text) - Catatan/keterangan tambahan
- tanggal_dibuat (Timestamp) - Waktu rekening dibuat
```

**Status Values:**
- `aktif` - Rekening sedang aktif/digunakan (badge hijau ✓)
- `tidak_aktif` - Rekening tidak aktif/tidak digunakan (badge merah ✗)

## 🌐 API Endpoints

Jika ingin mengintegrasikan dengan aplikasi lain:

```
GET  /api/rekening              # Dapatkan semua rekening
POST /api/rekening              # Tambah rekening
PUT  /api/rekening/<id>         # Update rekening
DELETE /api/rekening/<id>       # Hapus rekening
```

## 🔒 Keamanan

- Database disimpan lokal di komputer Anda
- Tidak ada data yang dikirim ke server eksternal
- Nomor rekening memiliki validasi unique (tidak boleh duplikat)

## 🐛 Troubleshooting

**Masalah: Port 5000 sudah digunakan**
- Edit file `bank_app.py` baris terakhir: `app.run(debug=True, port=5001)`

**Masalah: Module Flask tidak ditemukan**
- Install ulang: `pip install -r requirements.txt`

**Masalah: Database tidak terlihat**
- Database akan otomatis dibuat saat aplikasi pertama kali dijalankan

## 📝 Catatan

- Aplikasi ini menyimpan semua data di database lokal
- Database tidak akan hilang sampai Anda menghapusnya
- Anda dapat membackup file `rekening_bank.db` untuk keamanan data

---

**Dibuat untuk memudahkan pengelolaan data rekening bank Anda!** 🎉
