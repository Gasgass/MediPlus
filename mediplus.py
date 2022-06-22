import requests
import bs4
from bs4 import BeautifulSoup
import pandas as pd
import urllib.request
import matplotlib
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import pprint
import time
from requests_html import HTMLSession
import matplotlib.pyplot as plt
import seaborn as sns
#URLs
website = "https://servicios.pami.org.ar/vademecum/views/consultaPublica/listado.zul"
input_2 = input("ingrese su farmaco: ")


XPATH = [  "/html/body/div[1]/div[1]/nav/div/form/input",
           "/html/body/div[1]/div[1]/nav/div/form/div/i",
           "/html/body/div[3]/div/div[2]/div/div[1]/div[1]/a",
           ]


def webscrap(XPATH):
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, XPATH))) \
        .click()
    return

#WebScraping Vademecum
driver = webdriver.Chrome(executable_path=r"C:\Users\segui\Downloads\chromedriver.exe")
driver.get(website)
def webscrapkeys(XPATH):
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, XPATH))) \
        .send_keys(input_2)
    return

def scrap(XPATH):
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable(
        (By.XPATH, XPATH)))
    return

def find(XPATH):
    driver.find_elements_by_xpath(XPATH)
    x = []
    return(x)

webscrapkeys(XPATH= "/html/body/div/div/div/div/div[2]/div/div/div[1]/div[2]/div/div[3]/table/tbody[1]/tr[2]/td[3]/div/input")
webscrap(XPATH= "/html/body/div/div/div/div/div[2]/div/div/div[1]/div[2]/div/div[3]/table/tbody[1]/tr[7]/td[3]/div/div/div[1]/button")
"""try:
except TimeoutException:
    print("Tiempo de espera terminado. Reinicie el programa.")
    driver.quit()"""

"""if TimeoutException:
    print("Tiempo de espera terminado. Reinicie el programa.")
    driver.quit()
else:
    pass"""
scrap(XPATH= "/html/body/div[1]/div/div/div/div[2]/div/div/div[2]/div[3]/table/tbody[1]/tr/td[9]/span")
medicamento = driver.find_elements_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/div/div[2]/div[3]/table/tbody[1]/tr/td[9]/span")
medicamentos = []
for a in medicamento:
    medicamentos.append(a.text)
medicamentos = [ele for ele in medicamentos if ele.strip()]

scrap(XPATH= "/html/body/div[1]/div/div/div/div[2]/div/div/div[2]/div[3]/table/tbody[1]/tr/td[3]/span")
laboratorio = driver.find_elements_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/div/div[2]/div[3]/table/tbody[1]/tr/td[3]/span")
laboratorios = []
for a in laboratorio:
    laboratorios.append(a.text)
laboratorios = [ele for ele in laboratorios if ele.strip()]

scrap(XPATH= "/html/body/div[1]/div/div/div/div[2]/div/div/div[2]/div[3]/table/tbody[1]/tr/td[6]/span")
presentacion = driver.find_elements_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/div/div[2]/div[3]/table/tbody[1]/tr/td[6]/span")
presentaciones = []
for a in presentacion:
    presentaciones.append(a.text)
presentaciones = [ele for ele in presentaciones if ele.strip()]

scrap(XPATH= "/html/body/div[1]/div/div/div/div[2]/div/div/div[2]/div[3]/table/tbody[1]/tr/td[7]/span")
precio = driver.find_elements_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/div/div[2]/div[3]/table/tbody[1]/tr/td[7]/span")
precios = []
for a in precio:
    precios.append(a.text)
precios = [ele for ele in precios if ele.strip()]

farmaco = []
for i in range(10):
    data = {"Droga" : medicamentos[i],
           "Laboratorio" : laboratorios[i],
           "Presentacion" : presentaciones[i],
           "Precio" : precios[i]
           }
    farmaco.append(data)
    driver.quit()
df_data = pd.DataFrame(farmaco)
#print(df_data)
df_data.to_csv("Vademecum.csv")

#Armo una lista con split()
with open("Tratamiento.txt", "r") as f:
    for line in f:
        x = line.strip().split()

#Ordeno y depuro el archivo de texto
def remove_punc(string):
    punt = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''
    for ele in string:
        if ele in punt:
            string = string.replace(ele, "")
    return string
x = [remove_punc(i) for i in x]
if input_2 in x:
    print(df_data)
elif input_2 not in x:
    print("Este farmaco no coincide con la base de datos")

#Visualizacion de datos
data_base = pd.read_csv("Vademecum.csv")
data_base.to_csv("sample.csv", index=False, header=False, mode= "a")
sns.scatterplot(x="Precio", y='Droga', data=data_base)
plt.show()



"""r = requests.get("https://www.orpha.net/consor4.01/www/cgi-bin/Disease_Search_List.php?lng=ES&TAG=H"
)
sopa = BeautifulSoup(r.content, "html.parser")
s = sopa.find("div", id="result-box")
cuerpo = s.find("ul")
patologias = cuerpo.find_all('li')
#Manejo de datos
lista = []
for i in patologias:
    lista.append(i.text.lower())
print(lista)

#Frontend
pato_paci = input("ingrese la patologia:")
pato_paci = pato_paci.lower()"""

"""print(pato_paci)
for pato_paci in lista:
    print(pato_paci.pop(lista.index()))"""