import pandas as pd
import sys

def read_excel_table(file_name):
    try:
        df = pd.read_excel(file_name)
        return df
    except Exception as e:
        print("Error reading Excel file:", e)
        return None



def main():
    file_name = 'temp.xlsx'
    
    if len(sys.argv) != 3 or sys.argv[1] != '-t' or sys.argv[2] != 'all':
        print("Usage: python readtbl.py -t all")
        sys.exit(1)

    table = read_excel_table(file_name)
    if table is not None:
        table.insert(0, 'No', range(1, len(table) + 1))
        print(table.to_string(index=False))  # Print all attributes without index

if __name__ == "__main__":
    main()
