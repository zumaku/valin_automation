import pyperclip

# === Inisialisasi paket ===
print("Inisiasi valins_automation...")



# === Import modul yang akan digunakan ===
# Diisi nanti!


# === Variable Global ===
excel_file = '../docs/temp.xlsx'
greating = '''
Program ini akan mempermudah untuk melakukan kerjaan akuntan selama magang!

‼️ PROGRAM INI HANYA UNTUK MAHASISWA MAGANG DI TELKOM BALAIKOTA ‼️
Februari2024

---------------------------------------------------------------------------

Perintah yang Tersedia
'''

# Ini adalah semua posisi-posisi tombol dan form pada aplikasi Lensa Chetbot
# => Form Position <=
form_px = 1475
form_py = 1046


# => Send Button Position <=
send_btn_px = 1898
send_btn_py = 1042


# => Recheck Button Position <=
recheck_btn_px = 1392
recheck_btn_py = 986


# => Panel Button Position <=
panel1_btn_px = 1403
panel1_btn_py = 937

panel2_btn_px = 1398
panel2_btn_py = 983


# => Jumlah port Button Position <=
jml_port4_btn_px = 1385
jml_port4_btn_py = 936

jml_port8_btn_px = 1429
jml_port8_btn_py = 940

jml_port12_btn_px = 1491
jml_port12_btn_py = 935

jml_port16_btn_px = 1534
jml_port16_btn_py = 941


# => Shareloc Button postion <=
shareloc_btn_px = 1453
shareloc_btn_py = 983

send_shareloc_btn_px = 1857
send_shareloc_btn_py = 467


# => Ready Port Button Position <=
rp1_btn_px = 1370
rp1_btn_py = 892

rp2_btn_px = 1425
rp2_btn_py = 888

rp3_btn_px = 1475
rp3_btn_py = 888

rp4_btn_px = 1525
rp4_btn_py = 888

rp5_btn_px = 1372
rp5_btn_py = 937

rp6_btn_px = 1429
rp6_btn_py = 937

rp7_btn_px = 1475
rp7_btn_py = 937

rp8_btn_px = 1531
rp8_btn_py = 937

# Lanjutkan nanti untuk ready port 9-16, jika diperlukan!



# => Selesai di ODP Button Position <=
sdodp_btn_px = 1455
sdodp_btn_py = 939


# => QR Code Dropcore Button Position <=
qrcd_btn_px = 1471
qrcd_btn_py = 893


# => Tidak ada dropcode Button Position <=
nnd_btn_px = 1477
nnd_btn_py = 983


def copy_to_clipboard(text):
    try:
        pyperclip.copy(text)
        return True
    except:
        return False


# Mengekspor simbol-simbol (opsional)
# __all__ = [
#     'excel_file',
#     'greating',
# ]