#!/usr/bin/env python3
"""
Script untuk export data rekening dari database ke file CSV
Gunakan ketika Anda ingin backup data dalam format spreadsheet
"""

import sqlite3
import csv
from datetime import datetime
import os

DATABASE = 'rekening_bank.db'

def export_to_csv():
    """Export data rekening ke CSV file"""
    
    if not os.path.exists(DATABASE):
        print("❌ Database tidak ditemukan!")
        print(f"   Pastikan file '{DATABASE}' ada di folder yang sama")
        return
    
    try:
        # Connect ke database
        db = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
        
        # Query data
        cursor = db.execute('SELECT * FROM rekening ORDER BY tanggal_dibuat DESC')
        rekenings = cursor.fetchall()
        
        if not rekenings:
            print("⚠️  Tidak ada data rekening untuk di-export")
            db.close()
            return
        
        # Buat filename dengan timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"rekening_bank_backup_{timestamp}.csv"
        
        # Write ke CSV
        with open(filename, 'w', newline='', encoding='utf-8-sig') as csvfile:
            fieldnames = ['ID', 'Nama Rekening', 'No Rekening', 'Jenis Bank', 'Status', 'Keterangan', 'Tanggal Dibuat']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            for row in rekenings:
                writer.writerow({
                    'ID': row['id'],
                    'Nama Rekening': row['nama_rekening'],
                    'No Rekening': row['no_rekening'],
                    'Jenis Bank': row['jenis_bank'],
                    'Status': row['status'],
                    'Keterangan': row['keterangan'] or '',
                    'Tanggal Dibuat': row['tanggal_dibuat']
                })
        
        db.close()
        
        # Hasil
        print("\n✅ Export berhasil!")
        print(f"📁 File: {filename}")
        print(f"📊 Total data: {len(rekenings)} rekening")
        print(f"📍 Lokasi: {os.path.abspath(filename)}")
        
    except sqlite3.Error as e:
        print(f"❌ Error database: {e}")
    except Exception as e:
        print(f"❌ Error: {e}")

def import_from_csv(filename):
    """Import data rekening dari CSV file"""
    
    if not os.path.exists(filename):
        print(f"❌ File '{filename}' tidak ditemukan!")
        return
    
    try:
        db = sqlite3.connect(DATABASE)
        
        # Buat tabel jika belum ada
        db.execute('''
            CREATE TABLE IF NOT EXISTS rekening (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nama_rekening TEXT NOT NULL,
                no_rekening TEXT NOT NULL UNIQUE,
                jenis_bank TEXT NOT NULL,
                status TEXT DEFAULT 'aktif',
                keterangan TEXT,
                tanggal_dibuat TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        count = 0
        skip_count = 0
        
        with open(filename, 'r', encoding='utf-8-sig') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    db.execute('''
                        INSERT INTO rekening (nama_rekening, no_rekening, jenis_bank, status, keterangan)
                        VALUES (?, ?, ?, ?, ?)
                    ''', (row['Nama Rekening'], row['No Rekening'], row['Jenis Bank'], row.get('Status', 'aktif'), row.get('Keterangan', '')))
                    count += 1
                except sqlite3.IntegrityError:
                    skip_count += 1
        
        db.commit()
        db.close()
        
        print("\n✅ Import berhasil!")
        print(f"➕ Data ditambahkan: {count} rekening")
        print(f"⏭️  Data dilewati (duplikat): {skip_count} rekening")
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == '__main__':
    import sys
    
    print("=" * 50)
    print("🏦 Export/Import Data Rekening Bank")
    print("=" * 50)
    print()
    
    if len(sys.argv) > 1 and sys.argv[1] == '--import':
        if len(sys.argv) > 2:
            import_from_csv(sys.argv[2])
        else:
            print("Usage: python export_to_csv.py --import <filename.csv>")
    else:
        export_to_csv()
