import pandas as pd
import sys
from datetime import datetime

import __init__ as var
import table as tbl
import flow as flw

table = tbl.read_excel_table(var.excel_file)

def main():
    if len(sys.argv) == 1:  # No arguments provided
            print(var.greating)
            sys.exit()
    
    if sys.argv[1] == '-t':
        print("Argumen -t")

        if len(sys.argv) > 2:
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
            elif sys.argv[2] == 'edit':
                if len(sys.argv) != 7 or sys.argv[3] != '-onu' or sys.argv[5] != '-val':
                    print("Usage: python readtbl.py -t edit -onu <ONU SN> -val <VALINS ID>")
                    sys.exit(1)
                onu_sn = sys.argv[4]
                valins_id = sys.argv[6]
                edited_table = tbl.edit_table(table, onu_sn, valins_id)
                if edited_table is not None:
                    print("Table edited successfully:")
                    print("VALINS ID: " + valins_id)
                    print("ONU SN: " + onu_sn)
                    tbl.display_table(edited_table)
                    
                    # Simpan perubahan ke dalam file Excel
                    edited_table.to_excel(var.excel_file, index=False)
                else:
                    print("Error editing table.")
                    sys.exit(1)
            else:
                print("Usage: python readtbl.py -t all/-t nc/-t ac/-t edit -onu <ONU SN> -val <VALINS ID>")
                sys.exit(1)
        else:
            print("Displaying all tables:")
            tbl.display_table(table)
    
    elif sys.argv[1] == '-f':
        if len(sys.argv) < 2:
            print("Masukkan argumen untuk row, contoh -f 2")
        else:
            # Mengambil data
            row = int(sys.argv[2])
            node_id = tbl.get_data(var.excel_file, "NODE ID", row)
            slot = tbl.get_data(var.excel_file, "SLOT", row)
            port = tbl.get_data(var.excel_file, "PORT", row)
            
            print("NODE ID: {} | SLOT: {} | PORT: {}".format(node_id, slot, port))
            if input("Lanjut? y/n : ") == "y":
                flw.flow_pt1(node_id, slot, port)

                # Mengcopy ONU SN
                onu_sn = tbl.get_data(var.excel_file, "ONU SN", row)
                var.copy_to_clipboard(onu_sn)
                print("✓ ONU SN tercopy!")

            else:
                sys.exit()

            
        
        

if __name__ == "__main__":
    main()