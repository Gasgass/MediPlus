import pandas as pd
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#URLs
website = "https://servicios.pami.org.ar/vademecum/views/consultaPublica/listado.zul"
#Pido las variables a analizar
input_2 = input("ingrese su farmaco: ")

def click(XPATH):
    WebDriverWait(driver, 35).until(
        EC.element_to_be_clickable((By.XPATH, XPATH))) \
        .click()

def find(XPATH):
    driver.find_elements_by_xpath(XPATH)
    x = []
    return(x)

#WebScraping Vademecum
driver = webdriver.Chrome(executable_path=r"C:\Users\segui\Downloads\chromedriver.exe")
driver.get(website)
def keys_2(XPATH):
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, XPATH))) \
        .send_keys(input_2)

def scrap(XPATH):
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
        (By.XPATH, XPATH)))

keys_2(XPATH= "/html/body/div/div/div/div/div[2]/div/div/div[1]/div[2]/div/div[3]/table/tbody[1]/tr[2]/td[3]/div/input")
click(XPATH= "/html/body/div/div/div/div/div[2]/div/div/div[1]/div[2]/div/div[3]/table/tbody[1]/tr[7]/td[3]/div/div/div[1]/button")

while True:
    precio = driver.find_elements_by_xpath(
        "/html/body/div[1]/div/div/div/div[2]/div/div/div[2]/div[3]/table/tbody[1]/tr/td[7]/span")
    precios = []
    """for a in precio:
        precios.append(a.text)"""
    precios = [ele for ele in precios if ele.strip()]
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    scrap(XPATH= "/html/body/div/div/div/div/div[2]/div/div/div[3]/ul/li[4]/a/i")
    click(XPATH= "/html/body/div/div/div/div/div[2]/div/div/div[3]/ul/li[4]/a")
else:
    quit()

def data_analysis(XPATH):
    scrap(XPATH=XPATH)
    medicamento = driver.find_elements_by_xpath(XPATH)
    n = []
    for a in medicamento:
        n.append(a.text)
    n = [ele for ele in n if ele.strip()]
    return(n)

"""click(XPATH="/html/body/div/div/div/div/div[2]/div/div/div[3]/ul/li[4]/a")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")"""

    #precios = find(XPATH= "/html/body/div[1]/div/div/div/div[2]/div/div/div[2]/div[3]/table/tbody[1]/tr/td[7]/span")
    #print(precios)
#else:


"""def data_analysis(XPATH):
    scrap(XPATH= XPATH)
    medicamento = driver.find_elements_by_xpath(XPATH)
    n = []
    for a in medicamento:
        n.append(a.text)
    n = [ele for ele in n if ele.strip()]
    return n


medicamentos = data_analysis(XPATH= "/html/body/div[1]/div/div/div/div[2]/div/div/div[2]/div[3]/table/tbody[1]/tr/td[9]/span")
laboratorios = data_analysis(XPATH= "/html/body/div[1]/div/div/div/div[2]/div/div/div[2]/div[3]/table/tbody[1]/tr/td[3]/span")
presentaciones = data_analysis(XPATH= "/html/body/div[1]/div/div/div/div[2]/div/div/div[2]/div[3]/table/tbody[1]/tr/td[6]/span")
precios = data_analysis(XPATH= "/html/body/div[1]/div/div/div/div[2]/div/div/div[2]/div[3]/table/tbody[1]/tr/td[7]/span")


farmaco = []
for i in range(10):
    data = {"Droga" : medicamentos[i],
           "Laboratorio" : laboratorios[i],
           "Presentacion" : presentaciones[i],
           "Precio" : precios[i]
           }
    farmaco.append(data)
    #driver.quit()
df_data = pd.DataFrame(farmaco)
df_data.to_csv("Vademecum.csv")
#driver.quit()
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
print(df_data)
if input_2 in x:
    print(f"{input_2}, se encuentra en la base de datos")
    print(df_data)
elif input_2 not in x:
    print(f"{input_2} no coincide con la base de datos")
#Visualizacion de datos
data_base = pd.read_csv("Vademecum.csv")
data_base.to_csv("sample.csv", index=False, header=False, mode= "a")
sns.scatterplot(x="Precio", y='Droga', data=data_base)
plt.show()

while click(XPATH= "/html/body/div/div/div/div/div[2]/div/div/div[3]/ul/li[4]/a/i") == True:
    precio_venta = data_analysis(
        XPATH="/html/body/div[1]/div/div/div/div[2]/div/div/div[2]/div[3]/table/tbody[1]/tr/td[7]/span")
    promedio = []
    for i in range(10):
        datos = {"Precio": precio_venta[i]}
        promedio.append(datos)
        driver.quit()
    df_datas = pd.DataFrame(promedio)
    df_datas.to_csv("Promedio.csv")
    print(df_datas)
    driver.quit()"""