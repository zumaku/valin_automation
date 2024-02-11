import pyautogui
import time
import sys
import positions as pst


# Global Variable
jmlport = None
readyport = None


def clickat(x,y):
    pyautogui.click(x, y)
    time.sleep(1)

def typensend(text):
    # Klik pada form
    pyautogui.click(pst.form_px, pst.form_py)
    time.sleep(1)

    # tuliskan teks pada form
    pyautogui.typewrite(text)
    time.sleep(2)

    # Klik send
    pyautogui.click(pst.send_btn_px, pst.send_btn_py)
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
        clickat(pst.panel1_btn_px, pst.panel1_btn_py)
    elif int(jmlport) == 16:
        clickat(pst.panel2_btn_px, pst.panel2_btn_py)
    else:
        print("!!! Jumlah Port tidak sesuai !!!")
        sys.exit()
    print("=> Panel terpilih")
    time.sleep(5)

    # Memilih jumlah port
    print("=> Memilih jumlah port")
    if int(jmlport) == 8:
        clickat(pst.jml_port8_btn_px, pst.jml_port8_btn_py)
    else:
        clickat(pst.jml_port16_btn_px, pst.jml_port16_btn_py)
    print("=> Jumlah port terpilih")
    time.sleep(5)

    # Mengirim lokasi
    print("=> Mengirim lokasi")
    clickat(pst.shareloc_btn_px, pst.shareloc_btn_py)
    time.sleep(5)
    clickat(pst.send_shareloc_btn_px, pst.send_shareloc_btn_py)
    time.sleep(5)
    print("=> Lokasi Terkirim")
    time.sleep(5)

    # Memilih port yang tersedia
    print("=> Memilih Port yang tersedia")
    match readyport:
        case "1":
            clickat(pst.rp1_btn_px, pst.rp1_btn_py)
        case "2":
            clickat(pst.rp2_btn_px, pst.rp2_btn_py)
        case "3":
            clickat(pst.rp3_btn_px, pst.rp3_btn_py)
        case "4":
            clickat(pst.rp4_btn_px, pst.rp4_btn_py)
        case "5":
            clickat(pst.rp5_btn_px, pst.rp5_btn_py)
        case "6":
            clickat(pst.rp6_btn_px, pst.rp6_btn_py)
        case "7":
            clickat(pst.rp7_btn_px, pst.rp7_btn_py)
        case "8":
            clickat(pst.rp8_btn_px, pst.rp8_btn_py)
        case _:
            print("Error on switch case ready port")
    clickat(pst.shareloc_btn_px, pst.shareloc_btn_py)
    print("=> Port yang tersedia terpilih")
    time.sleep(5)
    
    # Memilih Selesai di ODP
    print("=> Memilih Selesai di ODP")
    clickat(pst.sdodp_btn_px, pst.sdodp_btn_py)
    print("=> Selesai di ODP terpilih")
    time.sleep(5)


    print("======= Flow Part 2, Selesai! =======")
    print("Silahkan simpan Valins ID")

def flow_pt3():
    print("======= Flow Part 2, Dimulai! =======")

    qrcode = input("Masukkan QR Code Dropcore: ")

    print("=> Mengklik QR Code Dropcore")
    clickat(pst.qrcd_btn_px, pst.qrcd_btn_py)
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
            clickat(pst.nnd_btn_px, pst.nnd_btn_py)
            time.sleep(5)
            print("=> 'Tidak ada Dropcore' Terpilih")
        x+=1


    print("======= Flow Part 3, Selesai! =======")
    print("Hentikan manual sendiri")



# ============================================================
# ============================================================


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
