import pandas as pd
import requests

# xls_milieux = pd.ExcelFile('../../output/Levures_ref_equivalents.xlsx')

# df = pd.read_excel(xls_milieux, 'Feuil1')

# count = 0
# total = 0

# df = df.reset_index(drop=True)  # make sure indexes pair with number of rows
# for index, row in df.iterrows():
#     refs_equis = row[7].split(';')

#     total += 1
#     for ref in refs_equis:
#         if 'atcc' in ref.lower():
#             count += 1

# print(count)
# print(total)

x = requests.post("https://www.atcc.org/api/product")
print(x.text)
