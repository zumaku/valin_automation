import pyperclip

# === Inisialisasi paket ===
print("Inisiasi valins_automation...")



# === Import modul yang akan digunakan ===
# Diisi nanti!


# === Variable Global ===
excel_file = '../docs/temp.xlsx'
greating = '''
            _ _                         _                        _   _             
__   ____ _| (_)_ __  ___    __ _ _   _| |_ ___  _ __ ___   __ _| |_(_) ___  _ __  
\ \ / / _` | | | '_ \/ __|  / _` | | | | __/ _ \| '_ ` _ \ / _` | __| |/ _ \| '_ \ 
 \ V / (_| | | | | | \__ \ | (_| | |_| | || (_) | | | | | | (_| | |_| | (_) | | | |
  \_/ \__,_|_|_|_| |_|___/  \__,_|\__,_|\__\___/|_| |_| |_|\__,_|\__|_|\___/|_| |_|                                                                                 
'''
print(greating)

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


# => Ready Port Button Position | Panel 1 <=
rp1_p1_btn_px = 1370
rp1_p1_btn_py = 892

rp2_p1_btn_px = 1425
rp2_p1_btn_py = 888

rp3_p1_btn_px = 1475
rp3_p1_btn_py = 888

rp4_p1_btn_px = 1525
rp4_p1_btn_py = 888

rp5_p1_btn_px = 1372
rp5_p1_btn_py = 937

rp6_p1_btn_px = 1429
rp6_p1_btn_py = 937

rp7_p1_btn_px = 1475
rp7_p1_btn_py = 937

rp8_p1_btn_px = 1531
rp8_p1_btn_py = 937


# => Ready Port Button Position | Panel 2 <=
rp1_p2_btn_px = 1369
rp1_p2_btn_py = 798

rp2_p2_btn_px = 1422
rp2_p2_btn_py = 798

rp3_p2_btn_px = 1470
rp3_p2_btn_py = 798

rp4_p2_btn_px = 1517
rp4_p2_btn_py = 798

rp5_p2_btn_px = 1370
rp5_p2_btn_py = 839

rp6_p2_btn_px = 1422
rp6_p2_btn_py = 839

rp7_p2_btn_px = 1470
rp7_p2_btn_py = 839

rp8_p2_btn_px = 1517
rp8_p2_btn_py = 839

rp9_p2_btn_px = 1370
rp9_p2_btn_py = 888

rp10_p2_btn_px = 1422
rp10_p2_btn_py = 888

rp11_p2_btn_px = 1470
rp11_p2_btn_py = 888

rp12_p2_btn_px = 1517
rp12_p2_btn_py = 888

rp13_p2_btn_px = 1370
rp13_p2_btn_py = 935

rp14_p2_btn_px = 1422
rp14_p2_btn_py = 935

rp15_p2_btn_px = 1470
rp15_p2_btn_py = 935

rp16_p2_btn_px = 1517
rp16_p2_btn_py = 935


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