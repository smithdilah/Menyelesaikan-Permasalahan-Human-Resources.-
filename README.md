# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Walaupun telah menjadi perusahaan yang cukup besar, **Jaya Jaya Maju** masih menghadapi tantangan serius dalam mengelola karyawan. Salah satu isu utama yang dihadapi adalah **tingginya tingkat attrition** atau tingkat keluar masuk karyawan (rasio jumlah karyawan yang keluar dengan total karyawan keseluruhan), yang saat ini telah melebihi **10%**. Tingginya attrition rate ini berdampak langsung terhadap:
- Meningkatnya biaya rekrutmen dan pelatihan karyawan baru.
- Turunnya produktivitas tim akibat kekosongan jabatan.
- Gangguan terhadap stabilitas operasional perusahaan.
- Penurunan semangat kerja tim karena fluktuasi anggota.

## Permasalahan Bisnis

- Belum adanya sistem prediksi untuk mendeteksi karyawan yang berisiko tinggi keluar dari perusahaan.
- Tidak tersedia insight yang cukup mengenai faktor-faktor penyebab attrition.
- Proses pengambilan keputusan oleh HRD masih berbasis asumsi dan pengalaman subjektif.
- Perlu adanya dashboard interaktif untuk visualisasi dan pengambilan keputusan secara real-time.

## Cakupan Proyek

- Melakukan eksplorasi dan pembersihan data (EDA & preprocessing).
- Membangun model prediktif menggunakan Logistic Regression dan Random Forest.
- Evaluasi performa model berdasarkan metrik klasifikasi.
- Membuat dashboard interaktif menggunakan Metabase (dijalankan di Docker).
- Menyimpan model yang terlatih untuk prediksi masa depan.

## Persiapan

**Sumber data:**  
Dataset karyawan internal perusahaan Jaya Jaya Maju yang mencakup atribut seperti usia, jabatan, divisi, pendidikan, gaji, status perkawinan, dan status attrition.

**Setup Environment - Anaconda**

```bash
conda create --name edutech-ds python=3.9
conda activate edutech-ds
pip install -r requirements.txt
```

**Setup Environment - Shell/Terminal**

```bash
pip install pipenv
pipenv install
pipenv shell
pip install -r requirements.txt
```

**Menjalankan File Prediksi**

```bash
python predict_attrition.py
```

**Menjalankan Metabase via Docker**

```bash
cd docker-compose
docker-compose up -d
```

## Business Dashboard

Dashboard dibuat menggunakan **Metabase** yang berjalan di atas Docker. Beberapa insight yang ditampilkan antara lain:
Untuk masuk ke metabase
Username: nurfadilahti21a2@gmail.com
Password: Nurfadilah123
- Distribusi karyawan berdasarkan status attrition.
- Hubungan antara fitur-fitur demografis dengan kemungkinan keluar.
- Jumlah karyawan keluar per departemen.
- Rata-rata gaji dan tingkat turnover per kelompok usia atau divisi.

📊 **Dashboard dapat diakses melalui:**  
[http://localhost:3000](http://localhost:3000) *(jika dijalankan secara lokal)*


## Model Evaluation

| Algoritma            | Akurasi |
|----------------------|---------|
| Logistic Regression  | 0.89    |
| Random Forest        | 0.89    |

Random Forest dan Logistic Regresion menunjukkan akurasi tertinggi dan dipilih sebagai model akhir untuk deployment.

## Conclusion

- Logistic Regression dan Random Forest menunjukkan akurasi yang baik (89%).
- Model masih kesulitan mengenali kelas minoritas karena ketidakseimbangan data.
- Sebagian besar karyawan yang keluar berasal dari divisi tertentu dengan tingkat lembur tinggi dan gaji di bawah rata-rata.
- Dashboard memudahkan tim HR dalam visualisasi, analisis, dan pengambilan keputusan berbasis data.

## Rekomendasi Action Items (Optional)

1. Lakukan balancing data menggunakan metode seperti SMOTE atau oversampling.
2. Terapkan strategi retensi pada divisi dengan turnover tinggi seperti mentoring atau program insentif.
3. Buat sistem peringatan dini menggunakan model prediksi.
4. Tambahkan fitur seperti lama bekerja, promosi terakhir, dan penilaian kinerja untuk akurasi lebih baik.
## Cara Menjalankan Skrip Prediksi Python (.py)

Untuk menjalankan skrip prediksi, pastikan Anda sudah berada di direktori proyek dan telah melakukan instalasi dependensi.

**Langkah Menjalankan Skrip:**
```bash
python prediksi_karyawan.py
```

Jika terdapat parameter tambahan yang harus dimasukkan (misalnya nama file atau model), contohnya:
```bash
python prediksi_karyawan.py --model random_forest.pkl --input data_uji.csv
```

## Setup Environment

Berikut tahapan untuk membuat virtual environment dan menginstal dependensi:

### Setup Environment - Anaconda
```bash
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt
```

### Setup Environment - Shell/Terminal
```bash
pip install pipenv
pipenv install
pipenv shell
pip install -r requirements.txt
```
