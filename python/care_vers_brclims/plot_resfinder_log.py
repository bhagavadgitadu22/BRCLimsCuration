import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
from matplotlib.ticker import FormatStrFormatter

import textwrap
def wrap_labels(ax, width, break_long_words=False):
    labels = []
    for label in ax.get_yticklabels():
        text = label.get_text()
        labels.append(textwrap.fill(text, width=width,
                      break_long_words=break_long_words))
    ax.set_yticklabels(labels, rotation=0)

xls_resfinder = pd.ExcelFile('C:/Users/mboutrou/Documents/bilan_genes.xlsx')
df = pd.read_excel(xls_resfinder, 'Statistics', index_col=0)

df = df.T
print(df)

plt.rcParams["figure.figsize"] = (20,8)
ax = df.plot(kind="barh", width = 0.8)
wrap_labels(ax, 30)
plt.title("Number of resistance genes per genus per antimicrobial class")
plt.xlabel("Number of resistance genes")
plt.ylabel("Antimicrobial classes")
plt.yticks(fontsize=8)
plt.gcf().subplots_adjust(left=0.2)
plt.xscale("log")
plt.gca().get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
plt.grid(axis='x')
plt.ylim(-0.5, len(plt.gca().get_yticklabels())-.5)
for i in range(len(plt.gca().get_yticklabels())):
    plt.gca().axhline(i+0.5, color = 'gray', linestyle = '--', linewidth = 0.5)
plt.show()
