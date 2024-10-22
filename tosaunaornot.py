import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import os


url = 'https://www.porssisahkoa.fi'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find('table')

current_date = datetime.now().strftime('%d-%m-%Y')
filename = f'toSaunaOrNotToSauna_{current_date}.csv'


for file in os.listdir('.'):
    if file.startswith('toSaunaOrNotToSauna_') and file.endswith('.csv'):
        os.remove(file)
        print(f'Deleted existing file: {file} ')


with open(filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    writer.writerow(['Time', 'Price'])

    if table:
        rows = table.find_all('tr') 
        for row in rows:
            cells = row.find_all('td')
            if cells:
                hour = cells[0].text.strip()
                price = cells[1].text.strip()
                writer.writerow([hour, price])

    else: 
        print('Could not find the price table.')

print(f'Data has been written to {filename}')