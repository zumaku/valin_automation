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
        df.insert(0, 'No', range(1, len(df) + 1)) # Numbering to the rows
        print(df.to_string(index=False))  # Print all attributes without index
        print("Number of rows:", len(df))
        print("Number of columns:", len(df.columns))

def main():
    file_name = 'temp.xlsx'
    
    if len(sys.argv) == 1:  # No arguments provided
        print("Usage: python readtbl.py -t all/-t nc/-t ac")
        sys.exit(1)
    
    table = read_excel_table(file_name)

    if sys.argv[1] == '-t':
        if len(sys.argv) != 3:
            print("Usage: python readtbl.py -t all/-t nc/-t ac")
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
        else:
            print("Usage: python readtbl.py -t all/-t nc/-t ac")
            sys.exit(1)
    else:
        print("Usage: python readtbl.py -t all/-t nc/-t ac")
        sys.exit(1)

if __name__ == "__main__":
    main()
