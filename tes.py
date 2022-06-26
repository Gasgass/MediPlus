import re
import csv
import requests
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import selenium
from selenium import webdriver
from selenium.webdriver.support.expected_conditions import staleness_of
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

#URLs
website = "https://servicios.pami.org.ar/vademecum/views/consultaPublica/listado.zul"

#Pido las variables a analizar
input_2 = input("ingrese su farmaco: ")

#WebScraping Vademecum
driver = webdriver.Chrome(executable_path=r"C:\Users\segui\Downloads\chromedriver.exe")
driver.get(website)
def prueba_2():
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div/div[2]/div/div/div[3]/ul/li[4]/a/i"))) \
        .click()

try:
    droga = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input#zk_comp_28"))) \
        .send_keys(input_2)
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn-default.btn-sm.btn"))) \
        .click()

except TimeoutException:
    print("Tiempo de espera terminado. Reinicie el programa.")
    driver.quit()
while True:
    prueba_2()

else:
    pass

def prueba():
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable(
        (By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div[2]/div[3]/table/tbody[1]/tr/td[7]/span")))
    WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div/div[2]/div/div/div[3]/ul/li[4]/a/i"))) \
        .click()
    precio = driver.find_elements_by_xpath(
        "/html/body/div[1]/div/div/div/div[2]/div/div/div[2]/div[3]/table/tbody[1]/tr/td[7]/span")
    precios = []
    for a in precio:
        precios.append(a.text)
    precios = [ele for ele in precios if ele.strip()]
    farmaco = []
    for i in range(10):
        data = {"Precio": precios[i]}
        farmaco.append(data)
    df_data = pd.DataFrame(farmaco)
    print(df_data)
    df_data.to_csv("Precios.csv")

"""i = []

while i in range(3):
    WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div/div[2]/div/div/div[3]/ul/li[4]/a/i"))) \
        .click()
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable(
        (By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div[2]/div[3]/table/tbody[1]/tr/td[7]/span")))
    WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div/div[2]/div/div/div[3]/ul/li[4]/a/i"))) \
        .click()
    precio = driver.find_elements_by_xpath(
        "/html/body/div[1]/div/div/div/div[2]/div/div/div[2]/div[3]/table/tbody[1]/tr/td[7]/span")
    precios = []
    for a in precio:
        precios.append(a.text)
    precios = [ele for ele in precios if ele.strip()]
    farmaco = []
    for i in range(10):
        data = {"Precio": precios[i]}
        farmaco.append(data)
    df_data = pd.DataFrame(farmaco)
    print(df_data)
    df_data.to_csv("Precios.csv")"""




"""i = []
for i in range(3):
    try:
        prueba()
        i += 1
    except:
        driver.quit()
"""

"""farmaco = []
for i in range(10):
    data = {"Precio" : precios[i]}
    farmaco.append(data)
    driver.quit()
print(farmaco)
df_data = pd.DataFrame(farmaco)
#print(df_data)
df_data.to_csv("Precios.csv")"""





