import re
import csv
import requests
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import selenium
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

#URLs
website = "https://servicios.pami.org.ar/vademecum/views/consultaPublica/listado.zul"
website2 = "https://www.tuotromedico.com/"

#Pido las variables a analizar
input_1 = input("Ingrese su patologia: ")
input_2 = input("ingrese su farmaco: ")


#WebScraping patologias
driver = webdriver.Chrome(executable_path=r"C:\Users\segui\Downloads\chromedriver.exe")
driver.get(website2)
driver.maximize_window()
try:
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/nav/div/form/input"))) \
        .send_keys(input_1)
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/nav/div/form/div/i"))) \
        .click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div[2]/div/div[1]/div[1]/a"))) \
        .click()

except TimeoutException:
    print("Tiempo de espera terminado. Reinicie el programa.")
    driver.quit()

#WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[1]/div[5]")))\
    #.click()
patologia = driver.find_elements_by_xpath("/html/body/div[3]/div[1]")

#Paso la data de la patologia a un diccionario
drogas = []
for a in patologia:
    drogas.append(a.text)
drogas = [ele for ele in drogas if ele.strip()]

farmaco = []
for i in range(len(drogas)):
    data = {"Manejo y tratamiento" : drogas[i] }
    farmaco.append(data)
print(farmaco)
driver.quit()

#Armo el data frame y el archivo txt
df_data = pd.DataFrame(farmaco)
file = open("Tratamiento.txt", "w")
for link in farmaco:
    l = str(link)
    file.write(l)
file.flush()
file.close()

#WebScraping Vademecum
driver = webdriver.Chrome(executable_path=r"C:\Users\segui\Downloads\chromedriver.exe")
driver.get(website)
try:
    droga = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input#zk_comp_28"))) \
        .send_keys(input_2)
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn-default.btn-sm.btn"))) \
        .click()
except TimeoutException:
    print("Tiempo de espera terminado. Reinicie el programa.")
    driver.quit()

WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div[2]/div[3]/table/tbody[1]/tr/td[9]/span")))
medicamento = driver.find_elements_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/div/div[2]/div[3]/table/tbody[1]/tr/td[9]/span")
medicamentos = []
for a in medicamento:
    medicamentos.append(a.text)
medicamentos = [ele for ele in medicamentos if ele.strip()]

WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div[2]/div[3]/table/tbody[1]/tr/td[3]/span")))
laboratorio = driver.find_elements_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/div/div[2]/div[3]/table/tbody[1]/tr/td[3]/span")
laboratorios = []
for a in laboratorio:
    laboratorios.append(a.text)
laboratorios = [ele for ele in laboratorios if ele.strip()]

WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div[2]/div[3]/table/tbody[1]/tr/td[6]/span")))
presentacion = driver.find_elements_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/div/div[2]/div[3]/table/tbody[1]/tr/td[6]/span")
presentaciones = []
for a in presentacion:
    presentaciones.append(a.text)
presentaciones = [ele for ele in presentaciones if ele.strip()]

WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div[2]/div[3]/table/tbody[1]/tr/td[7]/span")))
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
print(x)
print(input_2 in x)
if input_2 in x:
    print(df_data)
elif input_2 not in x:
    print("Este farmaco no coincide con la base de datos")

#Visualizacion de datos
data_base = pd.read_csv("Vademecum.csv")
data_base.to_csv("sample.csv", index=False, header=False, mode= "a")
sns.scatterplot(x="Precio", y='Droga', data=data_base)
plt.show()


