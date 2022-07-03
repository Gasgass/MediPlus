import time
import pandas as pd
import csv
import seaborn as sns
import matplotlib.pyplot as plt
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
""""Antes de empezar tengo que aclarar que todos los paths a archivos estan linkeados a mi pc y tienen mis direcciones, 
para que funcione el programa en otra pc hay que cambiar las lineas: 23, 76 y 148.
Tambien se van a generar cinco archivos en el directorio donde este alojado el programa, un txt, tres csv y un png."""
#URLs
website = "https://servicios.pami.org.ar/vademecum/views/consultaPublica/listado.zul"
website2 = "https://www.tuotromedico.com/"

#Pido las variables a analizar
input_1 = input("Ingrese su patologia: ")
input_2 = input("ingrese su farmaco: ")

#WebScraping patologia
driver = webdriver.Chrome(executable_path=r"C:\Users\segui\PycharmProjects\pythonProject4\chromedriver.exe")
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
    data = {"Manejo y tratamiento" : drogas[i].replace("\n", " ")}
    farmaco.append(data)
print(farmaco)
driver.quit()

#Armo el data frame y el archivo txt
df_data = pd.DataFrame(farmaco)
file = open(f"{input_1}.txt", "w")
for link in farmaco:
    l = str(link)
    file.write(l)
file.flush()
file.close()

#WebScraping Vademecum
driver = webdriver.Chrome(executable_path=r"C:\Users\segui\PycharmProjects\pythonProject4\chromedriver.exe")
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

    #Este bucle toma solo los precios de los farmacos, para usarlos en el grafico posterior
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

    #Apartir de aca armo un Vademecum por cada farmaco scrapeado
    medicamentos = data_analysis(
        XPATH="/html/body/div[1]/div/div/div/div[2]/div/div/div[2]/div[3]/table/tbody[1]/tr/td[9]/span")
    laboratorios = data_analysis(
        XPATH="/html/body/div[1]/div/div/div/div[2]/div/div/div[2]/div[3]/table/tbody[1]/tr/td[3]/span")
    presentaciones = data_analysis(
        XPATH="/html/body/div[1]/div/div/div/div[2]/div/div/div[2]/div[3]/table/tbody[1]/tr/td[6]/span")
    precios = data_analysis(
        XPATH="/html/body/div[1]/div/div/div/div[2]/div/div/div[2]/div[3]/table/tbody[1]/tr/td[7]/span")

    # Este bucle se encarga de tomar todos los datos completos de los farmacos
    farma = []
    for i in range(len(medicamentos)):
        dat = {"Droga": medicamentos[i],
                "Laboratorio": laboratorios[i],
                "Presentacion": presentaciones[i],
                "Precio": precios[i]
                }
        print(i)
        farma.append(dat)
    a_data = pd.DataFrame(farma)
    print(a_data)
    a_data.to_csv("Vademecum.csv", index=False, header=False, mode="a")

    click(XPATH="/html/body/div/div/div/div/div[2]/div/div/div[3]/ul/li[4]/a/i")
    time.sleep(15)

#Defino una funcion para imprimir un grafico por cada farmaco
def grafica():
    #Data Visualization
    csv = pd.read_csv("C:\\Users\\segui\\PycharmProjects\\pythonProject4\\"f"{input_2}.csv")
    sns.set_theme(style="ticks", palette="pastel")
    f, ax = plt.subplots(figsize=(30, 15))
    sns.boxplot(data=csv, whis=[0, 100], width=.2, color="pink")
    sns.stripplot(data=csv, dodge=True, alpha=.95, zorder=1, jitter=0.03, color="#73c3ff")
    sns.pointplot(data=csv, dodge=.8 - .8 / 3, join=False, color="blue", markers="d", scale=.95, ci=None)
    ax.xaxis.grid(True)
    ax.set(ylabel="Precios", xlabel=f"{input_2}")
    sns.despine(trim=False, left=False)
    plt.savefig(f"{input_2}.png", bbox_inches='tight', dpi=300)
    plt.show()

#Mas adelante uso esta funcion para limpiar el texto extraido de la patologia y evitar errores cuando comparo el farmaco ingresado con los datos extraidos
def remove_punc(string):
    punt = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''
    for ele in string:
        if ele in punt:
            string = string.replace(ele, "")
    return string

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

#Recorro pagina a pagina por cada medicamento
while True:
    scrap_precios()
    element = driver.find_element_by_xpath('//a[@name="zk_comp_99-next"]').get_attribute("disabled")
    if element == None:
        continue
    else:
        scrap_precios()
        grafica()
        time.sleep(30)
        driver.quit()
        quit()

#Armo una lista con split()
with open(f"{input_1}.txt", "r") as f:
    for line in f:
        x = line.strip().split()

#Ordeno y depuro el archivo de texto
x = [remove_punc(i) for i in x]
if input_2 in x:
    print(f"{input_2}, se encuentra en la base de datos")
    print(df_data)
elif input_2 not in x:
    print(f"{input_2} no coincide con la base de datos")
driver.quit()
quit()