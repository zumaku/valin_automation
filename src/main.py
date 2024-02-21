import pandas as pd
import sys
import time
from datetime import datetime
from colorama import Fore

import __init__ as var
import table as tbl
import flow as flw

table = tbl.read_excel_table(var.excel_file)

def main():
    # print(sys.argv)

    if len(sys.argv) == 1:
        var.displayDescription()
        sys.exit()
    
    if sys.argv[1] == '-t':
        if len(sys.argv) == 3:
            if sys.argv[2] == 'all':
                print("Displaying tables with all attributes:")
                tbl.display_table(table, all=True)
            elif sys.argv[2] == 'nc':
                print("Displaying tables with 'VALINS ID' attribute empty:")
                nc_table = table[table['VALINS ID'].isnull()]
                tbl.display_table(nc_table)
            elif sys.argv[2] == 'ac':
                print("Displaying tables with 'VALINS ID' attribute not empty:")
                ac_table = table.dropna(subset=['VALINS ID'])
                tbl.display_table(ac_table)
            else:
                print("Argumen yang dimasukkan salah.")
                sys.exit(1)
        else:
            print("Displaying all tables:\n")
            tbl.display_table(table)
    
    elif sys.argv[1] == '-f':
        if len(sys.argv) == 3:
            # Mengambil data
            row = int(sys.argv[2])
            node_id = tbl.get_data(var.excel_file, "NODE ID", row)
            slot = tbl.get_data(var.excel_file, "SLOT", row)
            port = tbl.get_data(var.excel_file, "PORT", row)
            
            print("NODE ID: {} | SLOT: {} | PORT: {}".format(node_id, slot, port))
            if input("Lanjut? y/n : ") == "y":
                # Menjalankan flow 1
                flw.flow_pt1(node_id, slot, port)

                # Mengcopy ONU SN
                onu_sn = tbl.get_data(var.excel_file, "ONU SN", row)
                var.copy_to_clipboard(onu_sn)
                print("✓ ONU SN tercopy!")
            else:
                sys.exit()
        else:
            print("Argumen yang dimasukkan salah.")
            print("Gunakan -f1 <NO ROW>")
            sys.exit(1)
    
    elif sys.argv[1] == '-f2':
        if len(sys.argv) == 3:
            # Mengambil number row
            row = int(sys.argv[2])

            # === Tambahkan pengecekan untuk isi databta!!! ===
            odp = tbl.get_data(var.excel_file, "ODP", row)
            jmlport = tbl.get_data(var.excel_file, "Max Port", row)
            readyport = tbl.get_data(var.excel_file, "Ready Port", row)
            panel = tbl.get_data(var.excel_file, "Panel", row)

            print("ODP: {} | Jumlah Port: {} | Ready Port: {}".format(odp, jmlport, readyport))
            if input("Lanjut? y/n : ") == "y":
                # Menjalankan flow 1
                flw.flow_pt2(odp, jmlport, readyport, panel)
            else:
                sys.exit()
        else:
            print("Argumen yang dimasukkan salah.")
            print("Gunakan -f2 <NO ROW>")
            sys.exit(1)

    elif sys.argv[1] == '-edit':
        if len(sys.argv) == 3:
            
            row = sys.argv[2]
            valins_id = input("Isi Valin ID: ")
            edited_table = tbl.edit_table(table, int(row), valins_id)
            
            if edited_table is not None:
                print("Table edited successfully!")
                print("VALINS ID: " + valins_id)
                print("ROW: " + row)
                tbl.display_table(edited_table)
                
                # Simpan perubahan ke dalam file Excel
                edited_table.to_excel(var.excel_file, index=False)
            else:
                print("Error editing table.")
                sys.exit(1)
        else:
            print("Argumen yang dimasukkan salah.")
            print("Gunakan -edit <NO ROW>")
            sys.exit(1)

    elif sys.argv[1] == '-f3':
        if len(sys.argv) == 3:
            row = int(sys.argv[2])
            jmlport = tbl.get_data(var.excel_file, "Max Port", row)
            readyport = tbl.get_data(var.excel_file, "Ready Port", row)
            qrcode = input("Masukkan QR Code: ")
            
            # Jika QR Code terlalu pendek
            if len(qrcode) < 10:
                print("QR Code Tidak Dapat Diterima.")
                sys.exit(1)
            
            print("Jumlah Port: {} | QR CODE: {} | Ready Port: {}".format(jmlport, qrcode, readyport))
            if input("Lanjut? y/n : ") == "y":
                # Menjalankan flow 3
                flw.flow_pt3(jmlport, qrcode, readyport)
            else:
                sys.exit()
        else:
            print("Argumen yang dimasukkan salah.")
            print("Gunakan -f3 <NO ROW>")
            sys.exit(1)

    elif sys.argv[1] == '-clk':
        if len(sys.argv) == 3:
            x = 1
            while x <= int(sys.argv[2]):
                print("-> Terklik {}X".format(x))
                flw.clickat(var.nnd_btn_px, var.nnd_btn_py)
                time.sleep(5)
                x += 1
        else:
            print("Argumen yang dimasukkan salah.")
            print("Gunakan -f3 <NO ROW>")
            sys.exit(1)


    else:
        print("Argumen '{}' tidak diketahui".format(sys.argv[1]))
    
    print(Fore.WHITE + "\nProgram ini dibuat oleh " + Fore.RED + var.create_hyperlink("Zumaku", "https://github.com/zumaku"))
    print(Fore.WHITE + "Semoga Membantu " + Fore.RED + ":)")

if __name__ == "__main__":
    main()