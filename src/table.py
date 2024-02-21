import pandas as pd
import sys
from datetime import datetime

def read_excel_table(file_name):
    try:
        df = pd.read_excel(file_name)
        return df
    except Exception as e:
        print("Error reading Excel file:", e)
        return None

def display_table(df, all=False):
    if df is not None:
        if 'No' not in df.columns:  # Memeriksa apakah kolom 'No' sudah ada
            df.insert(0, 'No', range(1, len(df) + 1)) # Numbering to the rows
        if all:
            print(df.to_string(index=False))  # Print all attributes without index
        else:
            # Membuat salinan DataFrame yang hanya berisi kolom yang tidak ingin ditampilkan
            df_partial = df.drop(columns=['First Updated', 'Last Updated'])
            print(df_partial.to_string(index=False))  # Print all attributes except 'First Updated' and 'Last Updated'
        print("Number of rows:", len(df))
        print("Number of columns:", len(df.columns))

def edit_table(df, row, valins_id):
    try:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if 'First Updated' not in df.columns or df.loc[df['No'] == row, 'First Updated'].isnull().all():
            df.loc[df['No'] == row, 'First Updated'] = now
        df.loc[df['No'] == row, 'Last Updated'] = now
        df.loc[df['No'] == row, 'VALINS ID'] = valins_id
        return df
    except Exception as e:
        print("Error editing table:", e)
        return None
    
def get_data(excel_file, colm, row):
    try:
        # Baca file Excel menjadi DataFrame
        df = pd.read_excel(excel_file)
        
        # Ambil data berdasarkan kolom (colm) dan baris (row) yang diberikan
        data = df.loc[row - 1, colm]
        
        return data
    except Exception as e:
        print("Error:", e)
        return None