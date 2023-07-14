import pandas as pd
import requests
from bs4 import BeautifulSoup

fechas = []
pibs = []
vars = []

url = 'https://datosmacro.expansion.com/pib/ecuador'

html_doc = requests.get(url)
soup = BeautifulSoup(html_doc.text, 'html.parser')

for table in soup.findAll('table', attrs={'class': 'table tabledat table-striped table-condensed table-hover'}):
    print(table)
    fecha = table.find('td', attrs={'class':'fecha'})
    print(fecha)
    pib = table.find('td', attrs={'class':'numero eur'})
    print(pib)
    var = table.find('td', attrs={'class':'numero'})
    print(var)

    fechas.append(fecha.text)
    pibs.append(pib.text)
    vars.append(var.text)

#BALLESTEROS ARELYS
#MINOTA CAROLINE
#FREIRE JEREMY
#GUARANDA MELANY

