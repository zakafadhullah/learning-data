import pandas as pd
import random
from datetime import datetime, timedelta

# Buat data dummy
lokasi_list = ['Jakarta', 'Bandung', 'Surabaya', 'Yogyakarta', 'Bali']
tipe_list = ['Rumah', 'Apartemen']
luas_bangunan_rumah_list = ['21', '36', '45', '54', '60']

data = []
for i in range(100):  # Buat 100 data properti
    lokasi = random.choice(lokasi_list)
    tipe = random.choice(tipe_list)
    luas_bangunan = random.choice(luas_bangunan_rumah_list) if tipe == 'Rumah' else random.randint(20, 40)  # Luas bangunan dalam m²
    # menentukan luas tanah berdasarkan luas bangunan
    if tipe == 'Apartemen':
        luas_tanah = '0'
    elif luas_bangunan == '21':
        luas_tanah = random.choice(['60', '72'])
    elif luas_bangunan == '36':
        luas_tanah = random.choice(['72', '90'])
    elif luas_bangunan == '45':
        luas_tanah = random.choice(['90', '105'])
    elif luas_bangunan == '54':
        luas_tanah = random.choice(['90', '120'])
    elif luas_bangunan == '60':
        luas_tanah = random.choice(['120', '150'])
    
    if lokasi == 'Jakarta':
        harga_per_meter = 5000000
    elif lokasi == 'Bandung':
        harga_per_meter = 3500000
    elif lokasi == 'Surabaya':
        harga_per_meter = 3000000
    elif lokasi == 'Yogyakarta':
        harga_per_meter = 2500000
    elif lokasi == 'Bali':
        harga_per_meter = 4000000
    elif tipe == 'Apartemen':
        harga_per_meter = round(random.randint(25000000, 60000000))
    harga = ((int(luas_bangunan) * harga_per_meter) + (int(luas_tanah) * harga_per_meter))

    status_transaksi = random.choice(['Terjual', 'Belum Terjual'])
    tanggal_transaksi = (datetime.now() - timedelta(days=random.randint(1, 365))).strftime('%Y-%m-%d') if status_transaksi == 'Terjual' else None

    data.append([i+1, lokasi, tipe, luas_bangunan, luas_tanah, harga_per_meter, harga, status_transaksi, tanggal_transaksi])

# Buat DataFrame
df = pd.DataFrame(data, columns=['id_property', 'lokasi', 'tipe_properti', 'luas_bangunan', 'luas_tanah', 'harga_per_meter', 'harga', 'status_transaksi', 'tanggal_transaksi'])

# Simpan sebagai CSV
df.to_csv('dataset_dummy_properti.csv', index=False)

print("Dataset dummy properti berhasil dibuat!")
