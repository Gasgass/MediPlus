import re
import csv
import time
import requests
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import selenium
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.expected_conditions import staleness_of
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import ElementNotSelectableException
import statistics
from statistics import mean
#URLs
website = "https://servicios.pami.org.ar/vademecum/views/consultaPublica/listado.zul"

#Pido las variables a analizar
input_2 = input("ingrese su farmaco: ")

#WebScraping Vademecum
driver = webdriver.Chrome(executable_path=r"C:\Users\segui\Downloads\chromedriver.exe")
driver.get(website)

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
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div/div[2]/div/div/div[3]/ul/li[4]/a/i"))) \
        .click()
    time.sleep(15)

try:
    droga = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input#zk_comp_28"))) \
        .send_keys(input_2)
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn-default.btn-sm.btn"))) \
        .click()

except TimeoutException:
    print("Tiempo de espera terminado. Reinicie el programa.")
    driver.quit()


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
quit()
with open(f"{input_2}.csv", "r"):
    file = pd.DataFrame(f"{input_2}.csv")
    print(file.head())
    print(file["Precio"].mean())
"""print(pd.DataFrame(f"{input_2}.csv").mean(axis=0))
with open(f"{input_2}.csv", "r") as f:
    print(f.mean(axis=0))
"""





