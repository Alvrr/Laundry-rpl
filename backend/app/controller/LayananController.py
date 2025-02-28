from app import db    
from app.model.layanan import Layanan    
from app import response    
from flask import request    
  
# Fungsi untuk menampilkan semua layanan    
def index_layanan():    
    try:    
        layanan = Layanan.query.all()    
        data = format_layanan(layanan)    
        return response.success(data, "Data layanan berhasil diambil")    
    except Exception as e:    
        print(e)    
        return response.badRequest([], 'Terjadi kesalahan saat mengambil data layanan')    
  
# Fungsi untuk menambahkan layanan    
def add_layanan():  
    try:  
        data = request.get_json()  # Ambil data JSON dari request  
        nama_layanan = data.get('nama_layanan')  
        harga_per_kg = data.get('harga_per_kg')  
        deskripsi = data.get('deskripsi')  
  
        layanan = Layanan(nama_layanan=nama_layanan, harga_per_kg=harga_per_kg, deskripsi=deskripsi)  
        db.session.add(layanan)  
        db.session.commit()  
  
        return response.success('', 'Berhasil menambah data layanan')  
    except Exception as e:  
        print(e)  
        return response.badRequest([], 'Terjadi kesalahan saat menambah layanan')
    
# Fungsi untuk mengedit layanan    
def edit_layanan(id):    
    try:    
        layanan = Layanan.query.get(id)    
        if not layanan:    
            return response.badRequest([], 'Layanan tidak ditemukan')    
  
        data = request.json  # Mengambil data JSON  
        layanan.nama_layanan = data.get('nama_layanan', layanan.nama_layanan)    
        layanan.harga_per_kg = data.get('harga_per_kg', layanan.harga_per_kg)    
        layanan.deskripsi = data.get('deskripsi', layanan.deskripsi)    
  
        db.session.commit()    
        return response.success('', 'Berhasil mengedit data layanan')    
    except Exception as e:    
        print(e)    
        return response.badRequest([], 'Terjadi kesalahan saat mengedit layanan')    
  
# Fungsi untuk menghapus layanan    
def delete_layanan(id):    
    try:    
        layanan = Layanan.query.get(id)    
        if not layanan:    
            return response.badRequest([], 'Layanan tidak ditemukan')    
  
        db.session.delete(layanan)    
        db.session.commit()    
        return response.success('', 'Berhasil menghapus layanan')    
    except Exception as e:    
        print(e)    
        return response.badRequest([], 'Terjadi kesalahan saat menghapus layanan')    
  
# Fungsi untuk format layanan    
def format_layanan(datas):    
    array = []    
    for i in datas:    
        array.append({    
            'id': i.id,    
            'nama_layanan': i.nama_layanan,  # Pastikan ini sesuai  
            'harga_per_kg': float(i.harga_per_kg),    
            'deskripsi': i.deskripsi    
        })    
    return array    
