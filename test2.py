import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

np.random.seed(42)

n = 1000
data = np.random.normal(loc=10, scale=2, size=n)


outliers = np.random.uniform(20, 25, 20)
data = np.concatenate([data, outliers])

def plot_histogram(data, title, color='skyblue'):
    plt.figure(figsize=(12, 6))
    plt.hist(data, bins=50, color=color, edgecolor='black', alpha=0.7)
    plt.axvline(np.mean(data), color='red', linestyle='dashed', linewidth=2, label=f'Mean: {np.mean(data):.2f}')
    plt.axvline(np.median(data), color='green', linestyle='dashed', linewidth=2, label=f'Median: {np.median(data):.2f}')
    plt.title(title)
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.legend()
    plt.show()


plot_histogram(data, 'Original Data with Outliers')

z_scores = np.abs(stats.zscore(data))
data_removed = data[z_scores < 3]
plot_histogram(data_removed, 'Data after Removing Outliers (z-score method)', color='lightgreen')

lower, upper = np.percentile(data, [2.5, 97.5])
data_capped = np.clip(data, lower, upper)
plot_histogram(data_capped, 'Data after Capping Outliers (Winsorization)', color='lightyellow')

z_scores = np.abs(stats.zscore(data))
data_replaced = data.copy()
data_replaced[z_scores >= 3] = np.mean(data)
plot_histogram(data_replaced, 'Data after Replacing Outliers with Mean', color='lightpink')