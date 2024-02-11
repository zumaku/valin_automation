import pandas as pd
import sys

def read_excel_table(file_name):
    try:
        df = pd.read_excel(file_name)
        return df
    except Exception as e:
        print("Error reading Excel file:", e)
        return None

def display_table(df):
    if df is not None:
        if 'No' not in df.columns:  # Memeriksa apakah kolom 'No' sudah ada
            df.insert(0, 'No', range(1, len(df) + 1)) # Numbering to the rows
        print(df.to_string(index=False))  # Print all attributes without index
        print("Number of rows:", len(df))
        print("Number of columns:", len(df.columns))


def edit_table(df, onu_sn, valins_id):
    try:
        df.loc[df['ONU SN'] == onu_sn, 'VALINS ID'] = valins_id
        return df
    except Exception as e:
        print("Error editing table:", e)
        return None

def main():
    file_name = 'temp.xlsx'
    
    if len(sys.argv) == 1:  # No arguments provided
        print("Usage: python readtbl.py -t all/-t nc/-t ac/-t edit -onu <ONU SN> -val <VALINS ID>")
        sys.exit(1)
    
    table = read_excel_table(file_name)

    if sys.argv[1] == '-t':
        print(sys.argv)

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
                edited_table.to_excel(file_name, index=False)
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
