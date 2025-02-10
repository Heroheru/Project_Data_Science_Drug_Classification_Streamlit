<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>README - Drug Classification</title>
    <style>
        body { font-family: Arial, sans-serif; line-height: 1.6; margin: 40px; }
        h1, h2, h3 { color: #333; }
        code { background: #f4f4f4; padding: 3px; border-radius: 5px; }
        pre { background: #eee; padding: 10px; border-radius: 5px; }
    </style>
</head>
<body>
    <h1>🚀 Project_Data_Science_Drug_Classification_Streamlit</h1>
    
    <h2>📌 1. Business Understanding</h2>
    <h3>1.1 Menentukan Masalah</h3>
    <p>Proyek ini bertujuan untuk mengembangkan sistem klasifikasi yang dapat mengidentifikasi tipe obat (drug) dalam tubuh pasien berdasarkan berbagai fitur kesehatan pasien.</p>
    
    <h3>1.2 Menentukan Tugas Analytics</h3>
    <p>Pendekatan yang digunakan dalam proyek ini adalah <b>klasifikasi</b>, di mana model akan menerima input berupa variabel-variabel pasien dan memprediksi jenis obat/drug yang dikonsumsi.</p>
    
    <h3>1.3 Menentukan Data yang Diperlukan</h3>
    <ul>
        <li>Usia</li>
        <li>Jenis Kelamin</li>
        <li>Level Tekanan Darah</li>
        <li>Tingkat Kolesterol dalam Darah</li>
        <li>Sodium to Potassium Ratio</li>
        <li>Label (Jenis Drug)</li>
    </ul>

    <h2>🔎 2. Exploratory Data Analysis (EDA) dan Fakta Penting</h2>
    <ul>
        <li>Dataset kecil, hanya memiliki 200 records.</li>
        <li>Ketidakseimbangan data pada kolom Drug, di mana kelas DrugY dan DrugX mendominasi.</li>
        <li>Metrik evaluasi utama adalah <b>Precision</b>, karena kesalahan klasifikasi dapat berdampak serius.</li>
        <li>Model yang dipilih untuk klasifikasi: Logistic Regression, Support Vector Machine (SVM), dan Decision Tree.</li>
        <li>Hasil terbaik diperoleh dari model <b>SVM</b> dengan weighted average precision sebesar <b>0.91</b>.</li>
    </ul>

    <h2>🛠 3. Teknologi yang Digunakan</h2>
    <ul>
        <li>Python (Pandas, Scikit-learn, NumPy, Matplotlib)</li>
        <li>Machine Learning (SVM, Logistic Regression, Decision Tree)</li>
        <li>Streamlit (Untuk membuat aplikasi web interaktif)</li>
    </ul>

    
