from flask import Flask, render_template, request, jsonify
import sqlite3
import os
from datetime import datetime

app = Flask(__name__)
DATABASE = 'rekening_bank.db'

def get_db():
    db = sqlite3.connect(DATABASE)
    db.row_factory = sqlite3.Row
    return db

def init_db():
    if not os.path.exists(DATABASE):
        db = get_db()
        db.execute('''
            CREATE TABLE rekening (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nama_rekening TEXT NOT NULL,
                no_rekening TEXT NOT NULL UNIQUE,
                jenis_bank TEXT NOT NULL,
                status TEXT DEFAULT 'aktif',
                keterangan TEXT,
                tanggal_dibuat TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        db.commit()
        db.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/rekening', methods=['GET'])
def get_rekening():
    db = get_db()
    rekenings = db.execute('SELECT * FROM rekening ORDER BY tanggal_dibuat DESC').fetchall()
    db.close()
    return jsonify([dict(r) for r in rekenings])

@app.route('/api/rekening', methods=['POST'])
def add_rekening():
    data = request.json
    try:
        db = get_db()
        db.execute('''
            INSERT INTO rekening (nama_rekening, no_rekening, jenis_bank, status, keterangan)
            VALUES (?, ?, ?, ?, ?)
        ''', (data['nama_rekening'], data['no_rekening'], data['jenis_bank'], data.get('status', 'aktif'), data.get('keterangan', '')))
        db.commit()
        db.close()
        return jsonify({'success': True, 'message': 'Rekening berhasil ditambahkan'}), 201
    except sqlite3.IntegrityError:
        return jsonify({'success': False, 'message': 'Nomor rekening sudah ada!'}), 400
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 400

@app.route('/api/rekening/<int:id>', methods=['PUT'])
def update_rekening(id):
    data = request.json
    try:
        db = get_db()
        db.execute('''
            UPDATE rekening 
            SET nama_rekening=?, no_rekening=?, jenis_bank=?, status=?, keterangan=?
            WHERE id=?
        ''', (data['nama_rekening'], data['no_rekening'], data['jenis_bank'], data.get('status', 'aktif'), data.get('keterangan', ''), id))
        db.commit()
        db.close()
        return jsonify({'success': True, 'message': 'Rekening berhasil diperbarui'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 400

@app.route('/api/rekening/<int:id>', methods=['DELETE'])
def delete_rekening(id):
    try:
        db = get_db()
        db.execute('DELETE FROM rekening WHERE id=?', (id,))
        db.commit()
        db.close()
        return jsonify({'success': True, 'message': 'Rekening berhasil dihapus'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 400

   if __name__ == '__main__':
       init_db()
       import os
       port = int(os.environ.get('PORT', 5000))
       print(f"🏦 Server berjalan di http://0.0.0.0:{port}")
       print("Database: rekening_bank.db")
       app.run(debug=False, host='0.0.0.0', port=port)
