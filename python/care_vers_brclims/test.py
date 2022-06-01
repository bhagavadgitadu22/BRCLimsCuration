import pandas as pd
import matplotlib.pyplot as plt

data = {'A': {'pos': 289794, 'neg': 515063},
        'B': {'pos': 174790, 'neg': 292551},
        'C': {'pos': 375574, 'neg': 586616},
        'D': {'pos': 14932, 'neg': 8661}}
df = pd.DataFrame(data)

for i in range(len(df)):
    print(df[df.columns[i]])
    for j in range(len(df[df.columns[0]])):
        norme = df.iloc[i, j]
        print(type(norme))
# df = df.T
# print(df)

# df ['sum'] = df.sum(axis=1)
# df.sort_values('sum', ascending=False)[['neg','pos']].plot.bar() 
# plt.show()
