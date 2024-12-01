
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', 3000)


df = pd.read_csv('Almond.csv')
num_duplicates = df.duplicated().sum()
print(f"Number of duplicated rows: {num_duplicates}")


df.isnull().sum()


df[df.isna().any(axis=1)]


import matplotlib.pyplot as plt

# Misalkan 'df' adalah DataFrame dan 'price' adalah kolom yang ingin dicek distribusinya
# plt.figure(figsize=(10, 6))
# plt.hist(df['Length (major axis)'], bins=30, color='blue', edgecolor='black')
# plt.title('Distribution of Length ')
# plt.xlabel('Nilai')
# plt.ylabel('Frekuensi')
# plt.show()


median_value = df['Length (major axis)'].isnull()
median_value = median_value.median()


for column in df.select_dtypes(include=['number']).columns:
    median_value = df['Length (major axis)'].median()
    df['Length (major axis)'].fillna(median_value, inplace=True)


import matplotlib.pyplot as plt

# # Misalkan 'df' adalah DataFrame dan 'price' adalah kolom yang ingin dicek distribusinya
# plt.figure(figsize=(10, 6))
# plt.hist(df['Length (major axis)'], bins=30, color='blue', edgecolor='black')
# plt.title('Distribution of Length ')
# plt.xlabel('Nilai')
# plt.ylabel('Frekuensi')
# plt.show()

for column in df.select_dtypes(include=['number']).columns:
    median_value = df['Aspect Ratio'].median()
    df['Aspect Ratio'].fillna(median_value, inplace=True)

plt.figure(figsize=(10, 6))
plt.hist(df['Aspect Ratio'], bins=30, color='blue', edgecolor='black')
plt.title('Distribution of Width ')
plt.xlabel('Nilai')
plt.ylabel('Frekuensi')
plt.show()

