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
            preciario_depurado.append(n)

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



csv = pd.read_csv('C:\\Users\\segui\\Desktop\\quetiapina.csv')

print(csv)
print(csv.info())
print(csv.shape)
sns.set()
#f, ax = plt.subplots(figsize=(10, 2))
sns.set_theme(style="ticks", palette="pastel")
f, ax = plt.subplots(figsize=(30, 15))

#ax = sns.stripplot(x="total_bill", y="day", data=tips)
sns.boxplot(data= csv, order=["Quetiapina", "Clonazepam","Lamotrigina","Olanzapina", "Litio", "Fluoxetina"], whis=[0, 100], width=.2, color="pink")
sns.stripplot(data= csv, order=["Quetiapina", "Clonazepam","Lamotrigina","Olanzapina", "Litio", "Fluoxetina"], dodge=True, alpha=.95, zorder=1, jitter=0.03, color="blue")
sns.pointplot(data= csv, order=["Quetiapina", "Clonazepam","Lamotrigina","Olanzapina", "Litio", "Fluoxetina"], dodge=.8 - .8 / 3,join=False, color="red" ,markers="d", scale=.95, ci=None)

"""sns.boxplot(preciario_depurado5,whis=[0, 100], width=.2, palette="rocket")
sns.stripplot(preciario_depurado5, dodge=True, alpha=.95, zorder=1, jitter=0.03)
sns.pointplot(preciario_depurado5,dodge=.8 - .8 / 3,join=False, palette="dark" ,markers="d", scale=.95, ci=None)

sns.boxplot(preciario_depurado,whis=[0, 100], width=.2, palette="rocket")
sns.stripplot(preciario_depurado, dodge=True, alpha=.95, zorder=1, jitter=0.03)
sns.pointplot(preciario_depurado,dodge=.8 - .8 / 3,join=False, palette="dark" ,markers="d", scale=.95, ci=None)"""

#sns.boxplot(preciario_depurado2,whis=[0, 100], width=.2, palette="vlag")
#sns.boxplot(preciario_depurado6,whis=[0, 100], width=.2, palette="vlag")
#sns.stripplot(preciario_depurado, size=4, linewidth=0)

ax.xaxis.grid(True)
ax.set(ylabel="Farmacos", xlabel="Precios")
sns.despine(trim=False, left=False)

#lt.savefig('plot6.png',bbox_inches='tight', dpi=300)
plt.show()
