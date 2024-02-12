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
    print("================ Flow Part 1, Dimulai! ================")

    # Mengirimkan perintah /findontport
    print("-> Mengirim '/findontport'")
    typensend("/findontport")
    print("   ✓ '/findontport' terkirim")
    time.sleep(4)

    # Mengirimkan Node ID
    print("-> Mengirim Node ID")
    typensend(node_id)
    print("   ✓ Node ID terkirim")
    time.sleep(4)


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

    print("================ Flow Part 1, Selesai! ================")
    print("Silahkan Recheck dan bersiap untuk flow kedua")