import pandas as pd
import joblib

# === 1. Load model, scaler, dan daftar fitur yang digunakan saat training ===
model = joblib.load('model/model.pkl')
scaler = joblib.load('model/scaler.pkl')
feature_names = joblib.load('model/feature_names.pkl')  # Harus sudah disimpan saat training

# === 2. Load data baru untuk prediksi ===
new_data = pd.read_csv('data_baru.csv')  # Pastikan file ini ada di folder yang sama

# === 3. Hapus kolom yang tidak digunakan jika masih ada ===
drop_columns = ['GenderBusinessTravel', 'Attrition']
new_data = new_data.drop(columns=[col for col in drop_columns if col in new_data.columns])

# === 4. Pastikan kolom data baru sesuai dengan urutan dan nama fitur saat training ===
missing_cols = [col for col in feature_names if col not in new_data.columns]
if missing_cols:
    raise ValueError(f"Kolom berikut tidak ditemukan dalam data baru: {missing_cols}")

# Urutkan kolom agar sesuai dengan training
new_data = new_data[feature_names]

# === 5. Lakukan standarisasi dengan scaler ===
new_data_scaled = scaler.transform(new_data)

# === 6. Lakukan prediksi dengan model yang sudah dilatih ===
predictions = model.predict(new_data_scaled)

# === 7. Tampilkan hasil prediksi ===
print("Hasil Prediksi (0 = Tidak Resign, 1 = Resign):")
print(predictions.astype(int))  # Menampilkan sebagai integer agar lebih jelas
