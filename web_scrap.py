import re

import pandas as pd
import requests
from bs4 import BeautifulSoup

fecha_list = list()
pib_eur_list = list()
pib_dol_list = list()
variacion_list = list()
url = 'https://datosmacro.expansion.com/pib/ecuador'

html_doc = requests.get(url)
soup = BeautifulSoup(html_doc.text, 'html.parser')

tabla = soup.find('table', attrs={'class': 'table tabledat table-striped table-condensed table-hover'})

filas = tabla.find_all('tr')

for fila in filas:
     celdas = fila.find_all('td')
     if len(celdas)> 0:
          fecha = celdas[0].string
          pib_eur = re.sub(r'[^\d.]', '', str(celdas[1].string))
          pib_dol = re.sub(r'[^\d.]', '', str(celdas[2].string))
          variacion = celdas[3].string
          fecha_list.append(fecha)
          pib_eur_list.append(pib_eur)
          pib_dol_list.append(pib_dol)
          variacion_list.append(variacion)

print(fecha_list)
print(pib_eur_list)
print(pib_dol_list)
print(variacion_list)

df = pd.DataFrame({'FECHA': fecha_list,'PIB (EUROS)': pib_eur_list,'PIB (DOLARES)': pib_dol_list, 'VARIACION PIB':variacion_list})
df.to_csv('PibEc.csv', index=False, encoding='utf-8')

#BALLESTEROS ARELYS
#MINOTA CAROLINE
#FREIRE JEREMY
#GUARANDA MELANY

