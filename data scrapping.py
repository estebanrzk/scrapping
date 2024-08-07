# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 23:17:44 2024

@author: f
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

def paises_extraidos():
    #URL de la página web para hacer scraping
    url = "https://www.scrapethissite.com/pages/simple/"

    #Enviar una solicitud GET a la página web
    response = requests.get(url)

    #Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        #Analizar el contenido html usando BeautifulSoup y herramientas de desarrollador
        soup = BeautifulSoup(response.content, 'html.parser')

        #Encontrar todos los contenedores de países
        paises = soup.find_all('div', class_='col-md-4 country')

        #Crear lista
        data = []

        #identificar cada elemento donde se encuentra los datos de país y extraerlo, asegurate que en este caso sea country para que sea igual que el html
        for country in paises:
            name = country.find('h3', class_='country-name').get_text(strip=True)
            capital = country.find('span', class_='country-capital').get_text(strip=True)
            population = country.find('span', class_='country-population').get_text(strip=True)
            area = country.find('span', class_='country-area').get_text(strip=True)

            #Meter los datos a la lista
            data.append({
                'País': name,
                'Capital': capital,
                'Población': population,
                'Área': area
            })

        # Crear un DataFrame a partir de los datos extraídos
        datos = pd.DataFrame(data)

        return datos
    else:
        print("Error al recuperar la página web.")
        return None

# Extraer los datos y guardarlos en un archivo CSV
datos = paises_extraidos()
if datos is not None:
    datos.to_csv("datos_paises.csv", index=False)
    print(datos)
