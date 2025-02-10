# 🚀 Project_Data_Science_Drug_Classification_Streamlit

## 📌 1. Business Understanding

### 1.1 Menentukan Masalah
Proyek ini bertujuan untuk mengembangkan sistem klasifikasi yang dapat mengidentifikasi tipe obat (drug) dalam tubuh pasien berdasarkan berbagai fitur kesehatan pasien.

### 1.2 Menentukan Tugas Analytics
Pendekatan yang digunakan dalam proyek ini adalah **klasifikasi**, di mana model akan menerima input berupa variabel-variabel pasien dan memprediksi jenis obat/drug yang dikonsumsi.

### 1.3 Menentukan Data yang Diperlukan
Data yang digunakan dalam proyek ini meliputi:
- **Usia**
- **Jenis Kelamin**
- **Level Tekanan Darah**
- **Tingkat Kolesterol dalam Darah**
- **Sodium to Potassium Ratio**
- **Label (Jenis Drug)**

Data dalam bentuk **CSV** dengan total **200 records**.

## 🔎 2. Exploratory Data Analysis (EDA) dan Fakta Penting
1. **Dataset termasuk kecil**, hanya memiliki 200 records.
2. **Ketidakseimbangan data** pada kolom **Drug**, di mana kelas **DrugY** dan **DrugX** mendominasi.
3. **Metrik evaluasi utama adalah Precision**, karena:
   - Precision mengukur akurasi model dalam mengidentifikasi jenis obat yang benar saat memberikan label positif.
   - Kesalahan dalam klasifikasi obat dapat berdampak serius pada perlakuan dan penanganan pasien.
4. **Model yang dipilih** untuk klasifikasi adalah:
   - **Logistic Regression**
   - **Support Vector Machine (SVM)**
   - **Decision Tree**
   
   Model-model ini dipilih karena ketahanan mereka terhadap **imbalanced data**.

5. **Hasil Pemodelan**:
   - Model **SVM** menghasilkan **weighted average precision** tertinggi sebesar **0.91**.
   - **Weighted avg precision** digunakan sebagai metrik utama karena dataset tidak seimbang, sehingga hasil lebih representatif.

## 🛠 3. Teknologi yang Digunakan
- **Python** (Pandas, Scikit-learn, NumPy, Matplotlib)
- **Machine Learning (SVM, Logistic Regression, Decision Tree)**
- **Streamlit** (Untuk membuat aplikasi web interaktif)
