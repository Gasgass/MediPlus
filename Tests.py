import time
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
import csv

preciario_depurado = []
with open("C:\\Users\\segui\\PycharmProjects\\pythonProject4\\levotiroxina.csv", "r") as f:
    a = csv.reader(f)
    for row in a:
        try:
            n = row[1]
            n = float(n.replace(",", "."))
            if type == str:
                del row[1]
            print(n, type(n))
            preciario_depurado.append(n)
        except ValueError:
            pass
#print(sum(preciario_depurado)/len(preciario_depurado))
csv = pd.read_csv("C:\\Users\\segui\\PycharmProjects\\pythonProject4\\levotiroxina.csv")
sns.boxplot(data= csv, whis=[0, 100], width=.2, color="pink")
sns.stripplot(data= csv, dodge=True, alpha=.95, zorder=1, jitter=0.03, color="#73c3ff")
sns.pointplot(data= csv, dodge=.8 - .8 / 3,join=False, color="blue" ,markers="d", scale=.95, ci=None)

plt.show()