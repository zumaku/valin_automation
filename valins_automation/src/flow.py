import pyautogui
import time
import sys
import __init__ as var

def clickat(x,y):
    pyautogui.click(x, y)
    time.sleep(1)

def typensend(text):
    # Klik pada form
    pyautogui.click(var.form_px, var.form_py)
    time.sleep(1)

    # tuliskan teks pada form
    pyautogui.typewrite(text)
    time.sleep(2)

    # Klik send
    pyautogui.click(var.send_btn_px, var.send_btn_py)
    time.sleep(1)

def chngodp(odp):
    # Menghapus tanda "/" dan huruf setelahnya
    odp = odp.split("/")[0]
    
    # Mengubah huruf ke-3 menjadi "C"
    odp = odp[:2] + "C" + odp[3:]
    
    return odp


def flow_pt1(node_id, slot, port):
    print("================ Flow 1, Dimulai! ================")

    # Mengirimkan perintah /findontport
    print("-> Mengirim '/findontport'")
    typensend("/findontport")
    print("   ✓ '/findontport' terkirim")
    time.sleep(3)

    # Mengirimkan Node ID
    print("-> Mengirim Node ID")
    typensend(node_id)
    print("   ✓ Node ID terkirim")
    time.sleep(3)


    # Mengirimkan slot
    print("-> Mengirim Slot")
    typensend(str(slot))
    print("   ✓ Slot terkirim")
    time.sleep(4)

    # Mengirimkan port
    print("-> Mengirim Port")
    typensend(str(port))
    print("   ✓ Port terkirim")
    time.sleep(4)

    print("================ Flow 1, Selesai! ================")
    print("Silahkan Recheck dan bersiap untuk flow kedua")


def flow_pt2(odp, jmlport, readyport, panel):
    print("======= Flow 2, Dimulai! =======")

    odc = chngodp(odp)

    # Mengirimkan ODC
    print("-> Mengirim ODC")
    typensend(odc)
    print("   ✓ ODC terkirim")
    time.sleep(5)
    
    # Mengirimkan ODP
    print("-> Mengirim ODP")
    typensend(odp)
    print("   ✓ ODP terkirim")
    time.sleep(5)
    
    # Memilih Panel
    print("-> Memilih Panel")
    if int(panel) == 1:
        clickat(var.panel1_btn_px, var.panel1_btn_py)
    elif int(panel) == 2:
        clickat(var.panel2_btn_px, var.panel2_btn_py)
    else:
        print("!!! Jumlah Port tidak sesuai !!!")
        sys.exit()
    print("   ✓ Panel terpilih")
    time.sleep(4)

    # Memilih jumlah port
    print("-> Memilih jumlah port")
    if int(jmlport) == 8:
        clickat(var.jml_port8_btn_px, var.jml_port8_btn_py)
    else:
        clickat(var.jml_port16_btn_px, var.jml_port16_btn_py)
    print("   ✓ Jumlah port terpilih")
    time.sleep(4)

    # Mengirim lokasi
    print("-> Mengirim lokasi")
    clickat(var.shareloc_btn_px, var.shareloc_btn_py)
    time.sleep(4)
    clickat(var.send_shareloc_btn_px, var.send_shareloc_btn_py)
    time.sleep(3)
    print("   ✓ Lokasi Terkirim")
    time.sleep(4)

    # Memilih port yang tersedia
    print("-> Memilih Port yang tersedia")
    if jmlport == 8:    # Jika Portnya 8
        if int(readyport) == 1:
            clickat(var.rp1_p1_btn_px, var.rp1_p1_btn_py)
        elif int(readyport) == 2:
            clickat(var.rp2_p1_btn_px, var.rp2_p1_btn_py)
        elif int(readyport) == 3:
            clickat(var.rp3_p1_btn_px, var.rp3_p1_btn_py)
        elif int(readyport) == 4:
            clickat(var.rp4_p1_btn_px, var.rp4_p1_btn_py)
        elif int(readyport) == 5:
            clickat(var.rp5_p1_btn_px, var.rp5_p1_btn_py)
        elif int(readyport) == 6:
            clickat(var.rp6_p1_btn_px, var.rp6_p1_btn_py)
        elif int(readyport) == 7:
            clickat(var.rp7_p1_btn_px, var.rp7_p1_btn_py)
        elif int(readyport) == 8:
            clickat(var.rp8_p1_btn_px, var.rp8_p1_btn_py)
        else:
            print("Error on switch case ready port")
            sys.exit(1)
    else:   # Jika Portnya 16
        if int(readyport) == 1:
            clickat(var.rp1_p2_btn_px, var.rp1_p2_btn_py)
        elif int(readyport) == 2:
            clickat(var.rp2_p2_btn_px, var.rp2_p2_btn_py)
        elif int(readyport) == 3:
            clickat(var.rp3_p2_btn_px, var.rp3_p2_btn_py)
        elif int(readyport) == 4:
            clickat(var.rp4_p2_btn_px, var.rp4_p2_btn_py)
        elif int(readyport) == 5:
            clickat(var.rp5_p2_btn_px, var.rp5_p2_btn_py)
        elif int(readyport) == 6:
            clickat(var.rp6_p2_btn_px, var.rp6_p2_btn_py)
        elif int(readyport) == 7:
            clickat(var.rp7_p2_btn_px, var.rp7_p2_btn_py)
        elif int(readyport) == 8:
            clickat(var.rp8_p2_btn_px, var.rp8_p2_btn_py)
        elif int(readyport) == 9:
            clickat(var.rp9_p2_btn_px, var.rp9_p2_btn_py)
        elif int(readyport) == 10:
            clickat(var.rp10_p2_btn_px, var.rp10_p2_btn_py)
        elif int(readyport) == 11:
            clickat(var.rp11_p2_btn_px, var.rp11_p2_btn_py)
        elif int(readyport) == 12:
            clickat(var.rp12_p2_btn_px, var.rp12_p2_btn_py)
        elif int(readyport) == 13:
            clickat(var.rp13_p2_btn_px, var.rp13_p2_btn_py)
        elif int(readyport) == 14:
            clickat(var.rp14_p2_btn_px, var.rp14_p2_btn_py)
        elif int(readyport) == 15:
            clickat(var.rp15_p2_btn_px, var.rp15_p2_btn_py)
        elif int(readyport) == 16:
            clickat(var.rp16_p2_btn_px, var.rp16_p2_btn_py)
        else:
            print("Error on switch case ready port")
            sys.exit(1)
    print("   ✓ Port yang tersedia terpilih")
    time.sleep(6)
    
    # Memilih Selesai di ODP
    print("-> Memilih Selesai di ODP")
    clickat(var.sdodp_btn_px, var.sdodp_btn_py)
    print("   ✓ Selesai di ODP terpilih")
    time.sleep(4)


    print("================ Flow 2, Selesai! ================")
    print("Silahkan simpan Valins ID")


def flow_pt3(jmlport, qrcode, readyport):
    print("================ Flow 3, Dimulai! ================")

    print("-> Mengklik QR Code Dropcore")
    clickat(var.qrcd_btn_px, var.qrcd_btn_py)
    time.sleep(5)
    print("   ✓ QR Code Dropcore terklik")

    x = 1
    while x <= jmlport:
        if x == int(readyport):
            print("-> Mengirim QR Code Dropcore pada Port {}".format(x))
            typensend(qrcode)
            print("   ✓ QR Code Dropcore Terkirim pada Port {}".format(x))
            time.sleep(5)
        else:
            print("-> Memilih 'Tidak ada Dropcore di Port {}'".format(x))
            clickat(var.nnd_btn_px, var.nnd_btn_py)
            time.sleep(5)
            print("   ✓ 'Tidak ada Dropcore di Port {}' Terpilih".format(x))
        x+=1


    print("================ Flow 3, Selesai! ================")
    print("Hentikan manual sendiri")