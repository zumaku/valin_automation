# Posisi form input => X: 1475, Posisi Y: 1046
# Posisi tombol kirim => X: 1898, Posisi Y: 1042
# Posisi tombol Port tidak ada qrcode => X: 1444, Posisi Y: 989




# /findontport untuk membuka sebuah proses baru








"""
# === FLOW ====
1. Run Aplikasi

2. Masukkan IP
3. Masukkan Slot
4. Masukkan Port

5. (pilih lanjut atau tidak, tergantung dari rechecknya berhasil)(Click recal secara manual)

# Jika recheck berhasil
6. Masukkan ODP
7. Masukkan jumlah port
8. Masukkan port yang tersedia
9.  (otomatis send ODC)
10. (otomatis send ODP) 
11. (otomatis pilih panel)
12. (otomatis pilih jumlah port)
13. (otomatis share lokasi)
14. (otomatis pilih selesai di ODP)

15. (catat manual valins id)

16. Masukkan qrcode
17. (otomatis skip dan isi qrcode)

18. (hentikan manual)

"""







import pyautogui
import time
import sys


# form position
form_px = 1475
form_py = 1046

# send btn position
send_btn_px = 1898
send_btn_py = 1042

# recheck button position
recheck_btn_px = 1392
recheck_btn_py = 986

# panel button position
panel1_btn_px = 1403
panel1_btn_py = 937

panel2_btn_px = 1398
panel2_btn_py = 983

# jumlah port button position
jml_port4_btn_px = 1385
jml_port4_btn_py = 936

jml_port8_btn_px = 1429
jml_port8_btn_py = 940

jml_port12_btn_px = 1491
jml_port12_btn_py = 935

jml_port16_btn_px = 1534
jml_port16_btn_py = 941

# shareloc button postion
shareloc_btn_px = 1453
shareloc_btn_py = 983

send_shareloc_btn_px = 1857
send_shareloc_btn_py = 467


# ready port button position
rp1_btn_px = 1385
rp1_btn_py = 883

rp2_btn_px = 1432
rp2_btn_py = 890

rp3_btn_px = 1480
rp3_btn_py = 891

rp4_btn_px = 1528
rp4_btn_py = 888

rp5_btn_px = 1389
rp5_btn_py = 937

rp6_btn_px = 1438
rp6_btn_py = 942

rp7_btn_px = 1484
rp7_btn_py = 938

rp8_btn_px = 1533
rp8_btn_py = 940

# rp9_btn_px = 
# rp9_btn_py = 

# rp10_btn_px = 
# rp10_btn_py = 

# rp11_btn_px = 
# rp11_btn_py = 

# rp12_btn_px = 
# rp12_btn_py = 

# rp13_btn_px = 
# rp13_btn_py = 

# rp14_btn_px = 
# rp14_btn_py = 

# rp15_btn_px = 
# rp15_btn_py = 

# rp16_btn_px = 
# rp16_btn_py = 



# Selesai di ODP button position
sdodp_btn_px = 1455
sdodp_btn_py = 939



# QR Code Dropcore button position
qrcd_btn_px = 1471
qrcd_btn_py = 893


# Tidak ada dropcode button position
nnd_btn_px = 1477
nnd_btn_py = 983


# Global Variable
jmlport = None
readyport = None


def clickat(x,y):
    pyautogui.click(x, y)
    time.sleep(1)

def typensend(text):
    # Klik pada form
    pyautogui.click(form_px, form_py)
    time.sleep(1)

    # tuliskan teks pada form
    pyautogui.typewrite(text)
    time.sleep(2)

    # Klik send
    pyautogui.click(send_btn_px, send_btn_py)
    time.sleep(1)

def chngodp(odp):
    # Menghapus tanda "/" dan huruf setelahnya
    odp = odp.split("/")[0]
    
    # Mengubah huruf ke-3 menjadi "C"
    odp = odp[:2] + "C" + odp[3:]
    
    return odp

def flow_pt1():
    print("======= Flow Part 1, Dimulai! =======")

    ip = input("Masukkan IP: ")
    slot = input("Masukkan slot: ")
    port = input("Masukkan port: ")

    # Mengirimkan perintah /findontport
    print("=> Mengirim '/findontport'")
    typensend("/findontport")
    print("=> '/findontport' terkirim")
    time.sleep(5)

    # Mengirimkan ip
    print("=> Mengirim IP")
    typensend(ip)
    print("=> IP terkirim")
    time.sleep(5)


    # Mengirimkan slot
    print("=> Mengirim Slot")
    typensend(slot)
    print("=> Slot terkirim")
    time.sleep(5)

    # Mengirimkan port
    print("=> Mengirim Port")
    typensend(port)
    print("=> Port terkirim")
    time.sleep(5)

    print("======= Flow Part 1, Selesai! =======")
    print("Silahkan recheck dan bersiap untuk flow kedua")

def flow_pt2():
    print("======= Flow Part 2, Dimulai! =======")

    odp = input("Masukkan ODP: ")
    odc = chngodp(odp)
    jmlport = input("Masukkan Jumlah Port: ")
    readyport = input("Masukkan Port Yang Tersedia: ")

    # Mengirimkan ODC
    print("=> Mengirim ODC")
    typensend(odc)
    print("=> ODC terkirim")
    time.sleep(10)
    
    # Mengirimkan ODP
    print("=> Mengirim ODP")
    typensend(odp)
    print("=> ODP terkirim")
    time.sleep(10)
    
    # Memilih Panel
    print("=> Memilih Panel")
    if int(jmlport) == 8:
        clickat(panel1_btn_px, panel1_btn_py)
    elif int(jmlport) == 16:
        clickat(panel2_btn_px, panel2_btn_py)
    else:
        print("!!! Jumlah Port tidak sesuai !!!")
        sys.exit()
    print("=> Panel terpilih")
    time.sleep(5)

    # Memilih jumlah port
    print("=> Memilih jumlah port")
    if int(jmlport) == 8:
        clickat(jml_port8_btn_px, jml_port8_btn_py)
    else:
        clickat(jml_port16_btn_px, jml_port16_btn_py)
    print("=> Jumlah port terpilih")
    time.sleep(5)

    # Mengirim lokasi
    print("=> Mengirim lokasi")
    clickat(shareloc_btn_px, shareloc_btn_py)
    time.sleep(5)
    clickat(send_shareloc_btn_px, send_shareloc_btn_py)
    time.sleep(5)
    print("=> Lokasi Terkirim")
    time.sleep(5)

    # Memilih port yang tersedia
    print("=> Memilih Port yang tersedia")
    match readyport:
        case "1":
            clickat(rp1_btn_px, rp1_btn_py)
        case "2":
            clickat(rp2_btn_px, rp2_btn_py)
        case "3":
            clickat(rp3_btn_px, rp3_btn_py)
        case "4":
            clickat(rp4_btn_px, rp4_btn_py)
        case "5":
            clickat(rp5_btn_px, rp5_btn_py)
        case "6":
            clickat(rp6_btn_px, rp6_btn_py)
        case "7":
            clickat(rp7_btn_px, rp7_btn_py)
        case "8":
            clickat(rp8_btn_px, rp8_btn_py)
        case _:
            print("Error on switch case ready port")
    clickat(shareloc_btn_px, shareloc_btn_py)
    print("=> Port yang tersedia terpilih")
    time.sleep(5)
    
    # Memilih Selesai di ODP
    print("=> Memilih Selesai di ODP")
    clickat(sdodp_btn_px, sdodp_btn_py)
    print("=> Selesai di ODP terpilih")
    time.sleep(5)


    print("======= Flow Part 2, Selesai! =======")
    print("Silahkan simpan Valins ID")

def flow_pt3():
    print("======= Flow Part 2, Dimulai! =======")

    qrcode = input("Masukkan QR Code Dropcore: ")

    print("=> Mengklik QR Code Dropcore")
    clickat(qrcd_btn_px, qrcd_btn_py)
    time.sleep(5)
    print("=> QR Code Dropcore terklik")

    x = 1
    while x <= int(jmlport):
        if x == int(readyport):
            print("=> Mengirim QR Code Dropcore")
            typensend(qrcode)
            print("=> QR Code Dropcore Terkirim")
            time.sleep(5)
        else:
            print("=> Memilih 'Tidak ada Dropcore'")
            clickat(nnd_btn_px, nnd_btn_py)
            time.sleep(5)
            print("=> 'Tidak ada Dropcore' Terpilih")
        x+=1


    print("======= Flow Part 3, Selesai! =======")
    print("Hentikan manual sendiri")






def main():
    flow_pt1()

    print("Ketik 'y' untuk lanjut ke Flow 2..")
    if input("Lanjut? (y/n): ") == "y":
        flow_pt2()
    else:
        print("Program dihentikan.")
        sys.exit()

    print("Ketik 'y' untuk lanjut ke Flow 3..")
    if input("Lanjut? (y/n): ") == "y":
        flow_pt3()
        print("Program dihentikan.")
        sys.exit()

if __name__ == "__main__":
    main()
