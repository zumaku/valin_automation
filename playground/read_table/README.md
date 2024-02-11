# Readtbl.py

Readtbl.py adalah sebuah program Python sederhana yang memungkinkan pengguna untuk membaca, menampilkan, dan mengedit tabel dari file Excel melalui terminal.
Program ini ditujukan untuk mempermudah para Mahasiswa Magang di Telkom Balaikota Makassar untuk urusan akuntan yaitu melakukan pengisian ONU SN dan VALINS ID pada Google Sheets.

‼️ PROGRAM INI HANYA UNTUK MAHASISWA MAGANG DI TELKOM BALAIKOTA ‼️

Februari2024



## Instalasi
1. Pastikan Anda memiliki Python yang terinstal di sistem Anda. Anda dapat mengunduh dan menginstal Python dari [situs web resminya](https://www.python.org/downloads/).
2. Unduh atau salin kode sumber program `readtbl.py` ke dalam direktori kerja Anda.
3. Instal library openpyxl dan pandas dengan menjalankan perintah berikut di terminal atau command prompt:
```bash
pip install openpyxl pandas
```

## Persiapan
1. Sebelum menggunakan program ini, pastikan kamu sudah menyiapkan file excel ini dan pastikan juga sudah memiliki jatah data untuk dikerjakan.

2. Copy data-data yang ada di Sheets sesuai dengan kolom yang disediakan di Excel.
3. Pste ke Excel dan kamu siap beraksi. 

## Penggunaan
Untuk menjalankan program, buka terminal di direktori tempat Anda menyimpan file `readtbl.py` dan ketikkan perintah sebagai berikut:


### Perintah yang Tersedia
1. **Tampilkan Semua Tabel**: `python readtbl.py -t all`
   - Menampilkan semua tabel yang ada dalam file Excel.

2. **Tampilkan Tabel dengan Kolom 'VALINS ID' Kosong**: `python readtbl.py -t nc`
   - Menampilkan tabel-tabel yang memiliki kolom 'VALINS ID' yang kosong atau tidak terisi.

3. **Tampilkan Tabel dengan Kolom 'VALINS ID' Terisi**: `python readtbl.py -t ac`
   - Menampilkan tabel-tabel yang memiliki kolom 'VALINS ID' yang sudah terisi.

4. **Edit Tabel**: `python readtbl.py -t edit -onu <ONU SN> -val <VALINS ID>`
   - Mengedit tabel dengan menambahkan atau mengubah nilai kolom 'VALINS ID' berdasarkan nomor serial ONU (ONU SN) yang diberikan.

### Contoh Penggunaan
- Menampilkan semua tabel: `python readtbl.py -t all`
- Menampilkan tabel dengan kolom 'VALINS ID' kosong: `python readtbl.py -t nc`
- Menampilkan tabel dengan kolom 'VALINS ID' terisi: `python readtbl.py -t ac`
- Mengedit tabel dengan menambahkan atau mengubah nilai kolom 'VALINS ID' untuk nomor serial ONU 'ZTEGD358C525': `python readtbl.py -t edit -onu ZTEGD358C525 -val 22995484`

Pastikan file Excel yang ingin Anda proses bernama `temp.xlsx` dan berada di direktori yang sama dengan file `readtbl.py`.

## Kontribusi
Jika Anda menemukan bug atau memiliki saran untuk meningkatkan program ini, jangan ragu untuk membuka "issue" atau membuat "pull request" di repositori ini.

Terima kasih telah menggunakan program `readtbl.py`!
