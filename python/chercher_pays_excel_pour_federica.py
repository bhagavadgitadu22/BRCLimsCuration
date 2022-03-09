import pandas as pd
import csv

xls_milieux = pd.ExcelFile('C:/Users/mboutrou/Downloads/find_country.xlsx')

f = open('C:/Users/mboutrou/Downloads/countries.csv', 'r', newline='')
records = csv.reader(f, delimiter=';')
countries = [record[0] for record in records]
f.close()

print(countries)

df = pd.read_excel(xls_milieux, 'Sheet1')
col_nom = df.columns[0]

df = df.reset_index(drop=True)  # make sure indexes pair with number of rows
locations = []
for index, row in df.iterrows():
    val = ''
    for c in countries:
        if c.lower() in row[col_nom].lower():
            val = c
    locations.append(val)

print(locations)
print(len(locations))
print(len(df))

df["Pays"] = locations

with pd.ExcelWriter("C:/Users/mboutrou/Downloads/countries_found.xlsx") as writer:
    df.to_excel(writer, sheet_name="countries", index=False)
