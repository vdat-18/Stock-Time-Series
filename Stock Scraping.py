import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://vinacorp.vn/trade-history/HPG'
response = requests.get(url)
print(response)

soup = BeautifulSoup(response.content, 'html.parser')
table = soup.find('table')
table_data = []
rows = table.find_all('tr')

data = []  
for row in rows:
    cols = row.find_all('td')
    cols = [col.text.strip() for col in cols]
    if cols: 
        data.append(cols)

df = pd.DataFrame(data, columns = ['Date', 'Close', '+/-', '%', 'Open', 'High', 'Low', 'Volume', 'Total GTGD'])
df = df.drop(columns=['+/-', '%', 'Total GTGD'])

df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')

cols_to_convert = ['Close', 'Open', 'High', 'Low', 'Volume']

for col in cols_to_convert:
    df[col] = df[col].str.replace(',', '')
    df[col] = pd.to_numeric(df[col], errors='coerce').astype('Int64')  

df_filtered = df[(df['Date'] >= '2010-01-01') & (df['Date'] <= '2024-03-31')]

df_filtered_1 = df_filtered.drop_duplicates()
df_reversed = df_filtered_1.iloc[::-1].reset_index(drop=True)
print(df_reversed)

