#Codigo modificado
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests

chrome_path = r"C:\Users\Cpu\OneDrive\Escritorio\proyectos\PRUEBA 1\chromedriver.exe"  # ruta del chromedriver
driver = webdriver.Chrome(chrome_path)

driver.get('https://www.walmart.com.mx/content/despensa/980004')
time.sleep(5)
elementos = driver.find_elements(By.XPATH,
                                 "//ul/li/div/span/span[contains(text(),' ')]")

precios = driver.find_elements(By.XPATH,
                               "//ul/li/div/div/span[@class='w_q67L']")

# Creación de la data
etiqueta_list = []
valor_precio = []

for elemento in elementos:
    etiqueta = elemento.text
    etiqueta_list.append(etiqueta)

for precio in precios:
    valor_p = precio.text
    valor_precio.append(valor_p)

# Creación DataFrame
df = pd.DataFrame()
dfp = pd.DataFrame()
df['Producto'] = etiqueta_list
dfp['Valor'] = valor_precio

#Combinado de ambas DataFrames
df_final = pd.concat([df, dfp], axis=1, ignore_index=False)

#Exportar excel
df_final.to_excel('outputfinal.xlsx', index=False)

driver.close()

#Url de la API
url = 'C:\\Users\\Cpu\\OneDrive\\Escritorio\\proyectos\\PRUEBA_3'

#Iniciando petición
response = requests.get(url)
data = response.json()

#Creando DataFrame
convert_data_json = pd.DataFrame(data)

#Exportar excel
convert_data_json.to_excel('output_final.xlsx', index=False)

#Codigo original
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

#Url de la API
url = 'url_api'

#Iniciando petición
response = requests.get(url)
data = response.json()

#Creando DataFrame
convert_data_json = pd.DataFrame(data)

#Exportar excel
convert_data_json.to_excel('output_final.xlsx', index=False)

chrome_path = r"C:\Users\Cpu\OneDrive\Escritorio\proyectos\PRUEBA 1\chromedriver.exe"  # ruta del chromedriver
driver = webdriver.Chrome(chrome_path)

driver.get('https://www.walmart.com.mx/content/despensa/980004')
time.sleep(5)
elementos = driver.find_elements(By.XPATH,
                                 "//ul/li/div/span/span[contains(text(),' ')]")

precios = driver.find_elements(By.XPATH,
                               "//ul/li/div/div/span[@class='w_q67L']")

# Creación de la data
etiqueta_list = []
valor_precio = []

for elemento in elementos:
    etiqueta = elemento.text
    etiqueta_list.append(etiqueta)

for precio in precios:
    valor_p = precio.text
    valor_precio.append(valor_p)

# Creación DataFrame
df = pd.DataFrame()
dfp = pd.DataFrame()
df['Producto'] = etiqueta_list
dfp['Valor'] = valor_precio

#Combinado de ambas DataFrames
df_final = pd.concat([df, dfp], axis=1, ignore_index=False)

#Exportar excel
df_final.to_excel('outputfinal.xlsx', index=False)

driver.close()