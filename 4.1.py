import pandas as pd
import matplotlib.pyplot as plt

brexit_tb = pd.read_csv('brexit_sth.csv', index_col='Unnamed: 0')
brexit_null = brexit_tb[brexit_tb.brexit == 0]
brexit_counts = brexit_null.groupby('age').count()
brexit_counts['brexit'].plot(kind='bar', figsize=(15, 8))
plt.show()
