import pandas
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import csv
import glob
import re
import statistics
from statistics import mean
print(sns.__version__)
import numpy as np
#input_2 = input("ingrese su farmaco: ")
def remove_punc(string):
    punt = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''
    for ele in string:
        if ele in punt:
            string = string.replace(ele, "")
    return string


"""if type == str:
    del row[1]"""
preciario_depurado = []
preciario_depurado2 = []
preciario_depurado3 = []
preciario_depurado4 = []
preciario_depurado5 = []
preciario_depurado6 = []
def prueba():
    a = csv.reader(f)
    for row in a:
        try:
            n = row[1]
            n = round(float(n.replace(",", ".")))
            if type == str:
                del row[1]
        except ValueError:
            pass
    promedio_preciario_depurado = sum(preciario_depurado) / len(preciario_depurado)
    preciario_depurado.clear()


with open("C:\\Users\\segui\\PycharmProjects\\pythonProject4\\Farmacos\\Enfermedades mentales\\clonazepam.csv", "r") as f:
    try:
        a = csv.reader(f)
        for row in a:
            try:
                n = row[1]
                n = round(float(n.replace(",", ".")))
                if type == str:
                    del row[1]
                preciario_depurado.append(n)
                promedio_preciario_depurado = sum(preciario_depurado) / len(preciario_depurado)
            except:
                pass

    except:
        pass



with open('C:\\Users\\segui\\PycharmProjects\\pythonProject4\\Farmacos\\Enfermedades mentales\\fluoxetina.csv', "r") as f:
    try:
        a = csv.reader(f)
        for row in a:
            try:
                n = row[1]
                n = round(float(n.replace(",", ".")))
                if type == str:
                    del row[1]
                preciario_depurado2.append(n)

            except ValueError:
                pass
        promedio_preciario_depurado2 = sum(preciario_depurado2) / len(preciario_depurado2)

    except:
        print("ok")
        pass

with open('C:\\Users\\segui\\PycharmProjects\\pythonProject4\\Farmacos\\Enfermedades mentales\\lamotrigina.csv', "r") as f:
    try:
        a = csv.reader(f)
        for row in a:
            try:
                n = row[1]
                n = round(float(n.replace(",", ".")))
                if type == str:
                    del row[1]
                preciario_depurado3.append(n)

            except ValueError:
                pass
        promedio_preciario_depurado3 = sum(preciario_depurado3) / len(preciario_depurado3)


    except:
        print("ok")
        pass

with open('C:\\Users\\segui\\PycharmProjects\\pythonProject4\\Farmacos\\Enfermedades mentales\\litio.csv', "r") as f:
    try:
        a = csv.reader(f)
        for row in a:
            try:
                n = row[1]
                n = round(float(n.replace(",", ".")))
                if type == str:
                    del row[1]
                preciario_depurado4.append(n)

            except ValueError:
                pass
        promedio_preciario_depurado4 = sum(preciario_depurado4) / len(preciario_depurado4)
    except:
        print("ok")
        pass

with open('C:\\Users\\segui\\PycharmProjects\\pythonProject4\\Farmacos\\Enfermedades mentales\\olanzapina.csv', "r") as f:
    try:
        a = csv.reader(f)
        for row in a:
            try:
                n = row[1]
                n = round(float(n.replace(",", ".")))
                if type == str:
                    del row[1]
                preciario_depurado5.append(n)

            except ValueError:
                pass
        promedio_preciario_depurado5 = sum(preciario_depurado5) / len(preciario_depurado5)
    except:
        print("ok")
        pass

with open('C:\\Users\\segui\\PycharmProjects\\pythonProject4\\Farmacos\\Enfermedades mentales\\quetiapina.csv', "r") as f:
    try:
        a = csv.reader(f)
        for row in a:
            try:
                n = row[1]
                n = round(float(n.replace(",", ".")))
                if type == str:
                    del row[1]
                preciario_depurado6.append(n)

            except ValueError:
                pass
        promedio_preciario_depurado6 = sum(preciario_depurado6) / len(preciario_depurado6)

    except:
        print("ok")
        pass

promedio_total = (promedio_preciario_depurado + promedio_preciario_depurado2 + promedio_preciario_depurado3 + promedio_preciario_depurado4 + promedio_preciario_depurado5 + promedio_preciario_depurado6)/6
print(promedio_total)



csv = pd.read_csv('C:\\Users\\segui\\PycharmProjects\\pythonProject4\\Farmacos\\Enfermedades_mentales.csv')
csv2 =pd.read_csv("C:\\Users\\segui\\PycharmProjects\\pythonProject4\\Farmacos\\vih.csv")
csv3 =pd.read_csv("C:\\Users\\segui\\PycharmProjects\\pythonProject4\\Farmacos\\parkinson.csv")
csv4 =pd.read_csv("C:\\Users\\segui\\PycharmProjects\\pythonProject4\\Farmacos\\acv.csv")
csv5 =pd.read_csv("C:\\Users\\segui\\PycharmProjects\\pythonProject4\\Farmacos\\diabetes.csv")
csv6 = pd.read_csv("C:\\Users\\segui\\PycharmProjects\\pythonProject4\\Farmacos\\tiroides.csv")
csv7 = pd.read_csv("C:\\Users\\segui\\PycharmProjects\\pythonProject4\\Farmacos\\vitaminas.csv")
print(csv)
print(csv.info())
print(csv.shape)
sns.set()

"""sns.set_theme(style="ticks", palette="pastel")
f, ax = plt.subplots(figsize=(30, 15))

sns.boxplot(data= csv, order=["Quetiapina", "Clonazepam","Lamotrigina","Olanzapina", "Litio", "Fluoxetina"], whis=[0, 100], width=.2, color="pink")
sns.stripplot(data= csv, order=["Quetiapina", "Clonazepam","Lamotrigina","Olanzapina", "Litio", "Fluoxetina"], dodge=True, alpha=.95, zorder=1, jitter=0.03, color="#73c3ff")
sns.pointplot(data= csv, order=["Quetiapina", "Clonazepam","Lamotrigina","Olanzapina", "Litio", "Fluoxetina"], dodge=.8 - .8 / 3,join=False, color="blue" ,markers="d", scale=.95, ci=None)


ax.xaxis.grid(True)
ax.set(ylabel="Precios", xlabel="Farmacos")
sns.despine(trim=False, left=False)

plt.savefig('plot.png',bbox_inches='tight', dpi=300)
plt.show()

sns.set_theme(style="ticks", palette="pastel")
f, ax = plt.subplots(figsize=(30, 15))
sns.boxplot(data= csv2, order=["Zidovudina", "Tenofovir","Rilpivirina","Ritonavir", "Nevirapina", "Lopinavir","Lamivudina","Fosamprenavir","Etravirina","Emtricitabina","Efavirenz","Doravirina","Abacavir","Atazanavir"], whis=[0, 100], width=.2, color="#73ce63")
sns.stripplot(data= csv2, order=["Zidovudina", "Tenofovir","Rilpivirina","Ritonavir", "Nevirapina", "Lopinavir","Lamivudina","Fosamprenavir","Etravirina","Emtricitabina","Efavirenz","Doravirina","Abacavir","Atazanavir"], dodge=True, alpha=.95, zorder=1, jitter=0.03, color="#73c3ff")
sns.pointplot(data= csv2, order=["Zidovudina", "Tenofovir","Rilpivirina","Ritonavir", "Nevirapina", "Lopinavir","Lamivudina","Fosamprenavir","Etravirina","Emtricitabina","Efavirenz","Doravirina","Abacavir","Atazanavir"], dodge=.8 - .8 / 3,join=False, color="blue" ,markers="d", scale=.95, ci=None)

ax.xaxis.grid(True)
ax.set(ylabel="Precios", xlabel="Farmacos")
sns.despine(trim=False, left=False)

plt.savefig('plot2.png',bbox_inches='tight', dpi=300)
plt.show()

sns.set_theme(style="ticks", palette="pastel")
f, ax = plt.subplots(figsize=(30, 15))
sns.boxplot(data= csv3, order=["Levodopa", "Amantadina"], whis=[0, 100], width=.2, color="#858d2a")
sns.stripplot(data= csv3, order=["Levodopa", "Amantadina"], dodge=True, alpha=.95, zorder=1, jitter=0.03, color="#73c3ff")
sns.pointplot(data= csv3, order=["Levodopa", "Amantadina"], dodge=.8 - .8 / 3,join=False, color="blue" ,markers="d", scale=.95, ci=None)


ax.xaxis.grid(True)
ax.set(ylabel="Precios", xlabel="Farmacos")
sns.despine(trim=False, left=False)

plt.savefig('plot3.png',bbox_inches='tight', dpi=300)
plt.show()

sns.set_theme(style="ticks", palette="pastel")
f, ax = plt.subplots(figsize=(30, 15))
sns.boxplot(data= csv4, order=["Clopidogrel", "Ticlopidina"], whis=[0, 100], width=.2, color="#508eff")
sns.stripplot(data= csv4, order=["Clopidogrel", "Ticlopidina"], dodge=True, alpha=.95, zorder=1, jitter=0.03, color="#73c3ff")
sns.pointplot(data= csv4, order=["Clopidogrel", "Ticlopidina"], dodge=.8 - .8 / 3,join=False, color="blue" ,markers="d", scale=.95, ci=None)


ax.xaxis.grid(True)
ax.set(ylabel="Precios", xlabel="Farmacos")
sns.despine(trim=False, left=False)

plt.savefig('plot4.png',bbox_inches='tight', dpi=300)
plt.show()

sns.set_theme(style="ticks", palette="pastel")
f, ax = plt.subplots(figsize=(30, 15))
sns.boxplot(data= csv5, order=["Insulina"], whis=[0, 100], width=.2, color="#ef4674")
sns.stripplot(data= csv5, order=["Insulina"], dodge=True, alpha=.95, zorder=1, jitter=0.03, color="#73c3ff")
sns.pointplot(data= csv5, order=["Insulina"], dodge=.8 - .8 / 3,join=False, color="blue" ,markers="d", scale=.95, ci=None)


ax.xaxis.grid(True)
ax.set(ylabel="Precios", xlabel="Farmacos")
sns.despine(trim=False, left=False)

plt.savefig('plot5.png',bbox_inches='tight', dpi=300)
plt.show()
"""
"""sns.set_theme(style="ticks", palette="pastel")
f, ax = plt.subplots(figsize=(30, 15))
sns.boxplot(data= csv6, order=["Levotiroxina", "Propranolol", "Metimazol"], whis=[0, 100], width=.2, color="#eff774")
sns.stripplot(data= csv6, order=["Levotiroxina", "Propranolol", "Metimazol"], dodge=True, alpha=.95, zorder=1, jitter=0.03, color="#73c3ff")
sns.pointplot(data= csv6, order=["Levotiroxina", "Propranolol", "Metimazol"], dodge=.8 - .8 / 3,join=False, color="blue" ,markers="d", scale=.95, ci=None)


ax.xaxis.grid(True)
ax.set(ylabel="Precios", xlabel="Farmacos")
sns.despine(trim=False, left=False)

plt.savefig('plot6.png',bbox_inches='tight', dpi=300)
plt.show()"""

sns.set_theme(style="ticks", palette="pastel")
f, ax = plt.subplots(figsize=(30, 15))
sns.boxplot(data= csv7, order=["Colecalciferol"], whis=[0, 100], width=.2, color="#f08d2a")
sns.stripplot(data= csv7, order=["Colecalciferol"], dodge=True, alpha=.95, zorder=1, jitter=0.03, color="#73c3ff")
sns.pointplot(data= csv7, order=["Colecalciferol"], dodge=.8 - .8 / 3,join=False, color="blue" ,markers="d", scale=.95, ci=None)


ax.xaxis.grid(True)
ax.set(ylabel="Precios", xlabel="Farmacos")
sns.despine(trim=False, left=False)

plt.savefig('plot7.png',bbox_inches='tight', dpi=300)
plt.show()


"""sns.boxplot(preciario_depurado5,whis=[0, 100], width=.2, palette="rocket")
sns.stripplot(preciario_depurado5, dodge=True, alpha=.95, zorder=1, jitter=0.03)
sns.pointplot(preciario_depurado5,dodge=.8 - .8 / 3,join=False, palette="dark" ,markers="d", scale=.95, ci=None)

sns.boxplot(preciario_depurado,whis=[0, 100], width=.2, palette="rocket")
sns.stripplot(preciario_depurado, dodge=True, alpha=.95, zorder=1, jitter=0.03)
sns.pointplot(preciario_depurado,dodge=.8 - .8 / 3,join=False, palette="dark" ,markers="d", scale=.95, ci=None)"""
