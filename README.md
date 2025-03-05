# Proyek Analisis Data - Bike Sharing  

## **Deskripsi**  
Proyek ini bertujuan untuk melakukan analisis dan visualisasi data dari **Bike Sharing Dataset**, yang mencakup informasi tentang pola penggunaan sepeda dari tahun 2011 hingga 2012.

## **Dataset**  
Dataset yang digunakan adalah **Bike Sharing Dataset**, yang berisi data tentang jumlah peminjaman sepeda, kondisi cuaca, serta faktor waktu (hari, bulan, musim, dll.).

## **Direktori Proyek**  
Struktur folder dalam proyek ini adalah sebagai berikut:

- **`submission/`**  
  - **`dashboard/`** → Berisi file dashboard untuk visualisasi data  
    - `dataclean_bikesharing` → Dataset yang digunakan dalam dashboard  
    - `dahsboard_bike.py` → File Python untuk menjalankan dashboard  
  - **`data/`** → Berisi dataset utama untuk analisis  
    - `day.csv`  
    - `hour.csv`  
  - `Proyek Analisis Data (bike-sharing-dataset).ipynb` → Notebook Jupyter untuk eksplorasi dan analisis data  
  - `README.md` → Dokumentasi proyek  
  - `requirements.txt` → Daftar library yang digunakan dalam proyek  
  - `url.txt` → Berisi link atau referensi terkait proyek  

## **Cara Menjalankan Proyek**  
1. **Clone repository**  
   ```sh
   git clone https://github.com/ERSYAF/Proyek-Analisis-Data-BikeSharing.git
   cd Proyek-Analisis-Data-BikeSharing

2. **Instal library yang dibutuhkan**
   ```sh
   pip install -r requirements.txt

3. **Menjalankan dashboard Streamlit**
   ```sh
   cd dashboard
   streamlit run dahsboard_bike.py

