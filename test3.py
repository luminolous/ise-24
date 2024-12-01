import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)
data = np.concatenate([
    np.random.normal(10, 2, 1000),  # Data utama
    np.random.uniform(20, 30, 50)   # Outlier
])

def cap_data(data, lower_percentile=1, upper_percentile=99):
    lower_bound = np.percentile(data, lower_percentile)
    upper_bound = np.percentile(data, upper_percentile)
    return np.clip(data, lower_bound, upper_bound)


data_capped = cap_data(data)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))

ax1.hist(data, bins=50, edgecolor='black')
ax1.set_title('Data Asli dengan Outlier')
ax1.set_xlabel('Nilai')
ax1.set_ylabel('Frekuensi')


ax2.hist(data_capped, bins=50, edgecolor='black')
ax2.set_title('Data setelah Capping')
ax2.set_xlabel('Nilai')
ax2.set_ylabel('Frekuensi')

plt.tight_layout()
plt.show()

print("Statistik Data Asli:")
print(pd.Series(data).describe())
print("\nStatistik Data setelah Capping:")
print(pd.Series(data_capped).describe())