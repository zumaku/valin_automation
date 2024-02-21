# Valin Automation v1

## Abstrak
Program semi otomatis validasi valin untuk membantu mahasiswa magang di Telkom STO Balaikota pada Februari 2024.

## Library yang dibutuhkan
- `pandas` (pd)
- `sys`
- `datetime`

## Commands
| Command                            | Deskripsi                                                                                           |
|------------------------------------|-----------------------------------------------------------------------------------------------------|
| `-t`                               | Menampilkan isi tabel.                                                                              |
| `-t ac`                            | Menampilkan data yang telah divalidasi.                                                            |
| `-t nc`                            | Menampilkan data yang belum divalidasi.                                                             |
| `-t all`                           | Menampilkan semua data beserta dengan atribut timestamp.                                             |
| `-t edit -r <NO-ROW> -val <VALIN-ID>` | Mengisi data Valin ID berdasarkan nomer row yang dimasukkan.                                        |
| `-f`                               | Menjalankan flow 1 (Findport s.d. Recheck).                                                         |
| `-f2`                              | Menjalankan flow 2 (ODP s.d. Valins ID).                                                            |
| `-f3 -qr <QR-CODE>`                | Menjalankan flow 3 (Input QR Code).                                                                 |
