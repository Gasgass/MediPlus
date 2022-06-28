import time
import pandas as pd
import selenium
from selenium import webdriver
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
#Funciones de busqueda para el scrap
def keys(XPATH):
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, XPATH))) \
        .send_keys(input_1)

def click(XPATH):
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, XPATH))) \
        .click()

def find(XPATH):
    driver.find_elements_by_xpath(XPATH)
    x = []
    return(x)
#Llamo a las funciones y accedo al sitio
try:
    keys(XPATH="/html/body/div[1]/div[1]/nav/div/form/input")
    click(XPATH="/html/body/div[1]/div[1]/nav/div/form/div/i")
    click(XPATH="/html/body/div[3]/div/div[2]/div/div[1]/div[1]/a")
except TimeoutException:
    print(f"{input_1} no se encuentra en la base de datos. Reinicie el programa.")
    quit()

#Paso la data de la patologia a un diccionario
patologia = driver.find_elements_by_xpath("/html/body/div[3]/div[1]")
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
#Defino las funciones
def keys_2(XPATH):
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, XPATH))) \
        .send_keys(input_2)

def scrap(XPATH):
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable(
        (By.XPATH, XPATH)))

#Scraping data
def data_analysis(XPATH):
    scrap(XPATH= XPATH)
    medicamento = driver.find_elements_by_xpath(XPATH)
    n = []
    for a in medicamento:
        n.append(a.text)
    n = [ele for ele in n if ele.strip()]
    return n
#Esta funcion se encarga de tomar todos los datos de los farmacos y almacenarlos en archivos csv
def scrap_precios():
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    precio = driver.find_elements_by_xpath(
        "/html/body/div[1]/div/div/div/div[2]/div/div/div[2]/div[3]/table/tbody[1]/tr/td[7]/span")
    precios = []
    for a in precio:
        precios.append(a.text)
    precios = [ele for ele in precios if ele.strip()]
    farmaco = []
    for i in range(len(precios)):
        data = {"Precio": precios[i].strip("$"),
                }
        farmaco.append(data)
    df_data = pd.DataFrame(farmaco)
    print(df_data)
    df_data.to_csv("Precios.csv")
    data_base = pd.read_csv("Precios.csv")
    data_base.to_csv(f"{input_2}.csv", index=False, header=False, mode="a")

    medicamentos = data_analysis(
        XPATH="/html/body/div[1]/div/div/div/div[2]/div/div/div[2]/div[3]/table/tbody[1]/tr/td[9]/span")
    laboratorios = data_analysis(
        XPATH="/html/body/div[1]/div/div/div/div[2]/div/div/div[2]/div[3]/table/tbody[1]/tr/td[3]/span")
    presentaciones = data_analysis(
        XPATH="/html/body/div[1]/div/div/div/div[2]/div/div/div[2]/div[3]/table/tbody[1]/tr/td[6]/span")
    precios = data_analysis(
        XPATH="/html/body/div[1]/div/div/div/div[2]/div/div/div[2]/div[3]/table/tbody[1]/tr/td[7]/span")

    farmaco = []
    for i in range(len(medicamentos)):
        data = {"Droga": medicamentos[i],
                "Laboratorio": laboratorios[i],
                "Presentacion": presentaciones[i],
                "Precio": precios[i]
                }
        farmaco.append(data)
    df_data = pd.DataFrame(farmaco)
    df_data.to_csv("Vademecum.csv", index=False, header=False, mode="a")

    click(XPATH="/html/body/div/div/div/div/div[2]/div/div/div[3]/ul/li[4]/a/i")
    time.sleep(15)

#Accedo al sitio de ANMAT
try:
    keys_2(
        XPATH="/html/body/div/div/div/div/div[2]/div/div/div[1]/div[2]/div/div[3]/table/tbody[1]/tr[2]/td[3]/div/input")
    click(
        XPATH="/html/body/div/div/div/div/div[2]/div/div/div[1]/div[2]/div/div[3]/table/tbody[1]/tr[7]/td[3]/div/div/div[1]/button")
except TimeoutException:
    print(f"{input_2} no se encuentra en la base de datos. Reinicie el programa.")
    driver.quit()
    quit()

#Recorro pagina por paginas por cada medicamento
while True:
    scrap_precios()
    element = driver.find_element_by_xpath('//a[@name="zk_comp_99-next"]').get_attribute("disabled")
    if element == None:
        continue
    else:
        scrap_precios()
        time.sleep(30)
        driver.quit()
        quit()

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
    print(f"{input_2}, se encuentra en la base de datos")
    print(df_data)
elif input_2 not in x:
    print(f"{input_2} no coincide con la base de datos")
driver.quit()
quit()





