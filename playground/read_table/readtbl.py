import pandas as pd
import sys
from datetime import datetime

excel_file = 'temp.xlsx'
greating = '''
Program ini akan mempermudah untuk melakukan kerjaan akuntan selama magang!

‼️ PROGRAM INI HANYA UNTUK MAHASISWA MAGANG DI TELKOM BALAIKOTA ‼️
Februari2024

---------------------------------------------------------------------------

Perintah yang Tersedia
1. Tampilkan Semua Tabel: `python readtbl.py -t all`

2. Tampilkan Semua Tabel Dengan Timestamp: `python readtbl.py -t whole`

3. Tampilkan Tabel dengan Kolom 'VALINS ID' Kosong: `python readtbl.py -t nc`

4. Tampilkan Tabel dengan Kolom 'VALINS ID' Terisi: `python readtbl.py -t ac`

5. Edit Tabel: `python readtbl.py -t edit -onu <ONU SN> -val <VALINS ID>`
    Mengedit tabel dengan mengubah nilai kolom 'VALINS ID' berdasarkan nomor serial ONU (ONU SN) yang diberikan.
'''

def read_excel_table(file_name):
    try:
        df = pd.read_excel(file_name)
        return df
    except Exception as e:
        print("Error reading Excel file:", e)
        return None

def display_table(df, whole=False):
    if df is not None:
        if 'No' not in df.columns:  # Memeriksa apakah kolom 'No' sudah ada
            df.insert(0, 'No', range(1, len(df) + 1)) # Numbering to the rows
        if whole:
            print(df.to_string(index=False))  # Print all attributes without index
        else:
            # Membuat salinan DataFrame yang hanya berisi kolom yang tidak ingin ditampilkan
            df_partial = df.drop(columns=['First Updated', 'Last Updated'])
            print(df_partial.to_string(index=False))  # Print all attributes except 'First Updated' and 'Last Updated'
        print("Number of rows:", len(df))
        print("Number of columns:", len(df.columns))


def edit_table(df, onu_sn, valins_id):
    try:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if 'First Updated' not in df.columns or df.loc[df['ONU SN'] == onu_sn, 'First Updated'].isnull().all():
            df.loc[df['ONU SN'] == onu_sn, 'First Updated'] = now
        df.loc[df['ONU SN'] == onu_sn, 'Last Updated'] = now
        df.loc[df['ONU SN'] == onu_sn, 'VALINS ID'] = valins_id
        return df
    except Exception as e:
        print("Error editing table:", e)
        return None

def main():
    
    if len(sys.argv) == 1:  # No arguments provided
        # print("Usage: python readtbl.py -t all/-t nc/-t ac/-t edit -onu <ONU SN> -val <VALINS ID>")
        print(greating)
        sys.exit(1)
    
    table = read_excel_table(excel_file)

    if sys.argv[1] == '-t':
        # Minimal ada satu argumen yang diberikan
        if len(sys.argv) < 3:
            print("Atleast give me 1 argument")
            print("Usage: python readtbl.py -t all/-t nc/-t ac/-t edit -onu <ONU SN> -val <VALINS ID>")
            sys.exit(1)

        if sys.argv[2] == 'all':
            print("Displaying all tables:")
            display_table(table)
        elif sys.argv[2] == 'nc':
            print("Displaying tables with 'VALINS ID' attribute empty:")
            nc_table = table[table['VALINS ID'].isnull()]
            display_table(nc_table)
        elif sys.argv[2] == 'ac':
            print("Displaying tables with 'VALINS ID' attribute not empty:")
            ac_table = table.dropna(subset=['VALINS ID'])
            display_table(ac_table)
        elif sys.argv[2] == 'whole':  # Menambahkan opsi '-t whole'
            print("Displaying tables with all attributes:")
            display_table(table, whole=True)
        elif sys.argv[2] == 'edit':
            if len(sys.argv) != 7 or sys.argv[3] != '-onu' or sys.argv[5] != '-val':
                print("Usage: python readtbl.py -t edit -onu <ONU SN> -val <VALINS ID>")
                sys.exit(1)
            onu_sn = sys.argv[4]
            valins_id = sys.argv[6]
            edited_table = edit_table(table, onu_sn, valins_id)
            if edited_table is not None:
                print("Table edited successfully:")
                print("VALINS ID: " + valins_id)
                print("ONU SN: " + onu_sn)
                display_table(edited_table)
                
                # Simpan perubahan ke dalam file Excel
                edited_table.to_excel(excel_file, index=False)
            else:
                print("Error editing table.")
                sys.exit(1)
        else:
            print("Usage: python readtbl.py -t all/-t nc/-t ac/-t edit -onu <ONU SN> -val <VALINS ID>")
            sys.exit(1)
    else:
        print("Usage: python readtbl.py -t all/-t nc/-t ac/-t edit -onu <ONU SN> -val <VALINS ID>")
        sys.exit(1)

if __name__ == "__main__":
    main()
