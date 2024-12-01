# import statsmodels.api as sm
# import pandas as pd
# from sklearn.model_selection import train_test_split

# # Contoh dataset
# df = pd.DataFrame({
#     'A': [1, 2, 3, 4, 5],
#     'B': [2, 1, 2, 3, 5],
#     'C': [5, 4, 3, 2, 1],
#     'target': [1, 0, 1, 0, 1]
# })

# X = df[['A', 'B', 'C']]
# y = df['target']

# # Mulai dengan model kosong
# X_with_constant = sm.add_constant(X)
# model = sm.OLS(y, X_with_constant).fit()

# print(model.summary())


