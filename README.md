# Valin Automation v1.1

## Abstrak
Program semi otomatis validasi valin untuk membantu mahasiswa magang di Telkom STO Balaikota pada Februari 2024.

## Library yang dibutuhkan
- `pandas`
- `sys`
- `datetime`

## Commands
| Command                            | Deskripsi                                                                                           |
|------------------------------------|-----------------------------------------------------------------------------------------------------|
| `-t`                               | Menampilkan isi tabel.                                                                              |
| `-t ac`                            | Menampilkan data yang telah divalidasi.                                                             |
| `-t nc`                            | Menampilkan data yang belum divalidasi.                                                             |
| `-t all`                           | Menampilkan semua data beserta dengan atribut timestamp.                                            |
| `-edit <NO-ROW>`                   | Mengisi data Valin ID berdasarkan nomer row yang dimasukkan.                                        |
| `-f <NO-ROW>`                      | Menjalankan flow 1 (Findport s.d. Recheck) untuk nomer row yang dimasukkan.                         |
| `-f2 <NO-ROW>`                     | Menjalankan flow 2 (ODP s.d. Valins ID) untuk nomer row yang dimasukkan.                            |
| `-f3 <NO-ROW>`                     | Menjalankan flow 3 (Input QR Code) untuk nomer row yang dimasukkan.                                 |
| `-clk <JML-CLICK>`                 | Mengklik 'tidak ada qr-code' pada flow 3.                                                           |
