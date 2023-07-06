import requests
import pandas as pd
from bs4 import BeautifulSoup

url = 'http://127.0.0.1:8000/'

html_doc = requests.get(url)

soup = BeautifulSoup(html_doc.text, 'html.parser')

titulo_datos = soup.h1.string

tabla = soup.find('table')

filas = tabla.find_all('tr')


nombres = []
apellidos = []
emails = []

for fila in filas :

    celdas = fila.find_all('td')
    if len(celdas)>0:

        nombres.append(celdas[1].string)
        apellidos.append(celdas[2].string)
        emails.append(celdas[3].string)

print(nombres)
print(apellidos)
print(emails)

df = pd.DataFrame({'Nombres':nombres,'Apellidos':apellidos,'Emails':emails})
df.to_csv('docentes.cvs', index=False, encoding='utf-8')

