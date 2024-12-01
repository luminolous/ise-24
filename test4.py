import pandas as pd

# Membaca data dari file CSV
df = pd.read_csv('Almond.csv')

# Menghapus baris duplikat jika ada
df = df.drop_duplicates()

column = 'Length (major axis)'


Q1 = df[column].quantile(0.25)
Q3 = df[column].quantile(0.75)
IQR = Q3 - Q1
    

# Menghitung batas atas dan batas bawah
upper_boundary = Q3 + (IQR * 1.5)
lower_boundary = Q1 - (IQR * 1.5)

# Mendeteksi outliers
outliers = df[(df[column] > upper_boundary) | (df[column] < lower_boundary)]

# Menampilkan hasil
if outliers.empty:
    print(f"Tidak ada outliers untuk kolom '{column}'.")
else:
    print(f"Outliers untuk kolom '{column}':")
    print(outliers)
    print("\n")

    
