import pandas
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import csv
import glob
import re
import statistics
from statistics import mean
import matplotlib.pyplot as ptl
import seaborn as sns
#input_2 = input("ingrese su farmaco: ")
#Data Visualization
#Accedo a las bases de datos de los medicamentos
preciario_depurado = []
with open("C:\\Users\\segui\\PycharmProjects\\pythonProject4\\Farmacos\\Enfermedades mentales\\clonazepam.csv", "r") as f:
    a = csv.reader(f)
    for row in a:
        try:
            n = row[1]
            n = float(n.replace(",", "."))
            if type == str:
                del row[1]
            preciario_depurado.append(n)
        except ValueError:
            pass
print(preciario_depurado)
print(sum(preciario_depurado)/len(preciario_depurado))

# import required module


# iterate over files in
# that directory
"""a = []
preciario_depurado = []
for numero in range(1, 5 + 1):
    locals()["preciario_depurado" + str(numero)] = 'preciario_depurado' + str(numero)

for filename in glob.iglob('C:\\Users\\segui\\PycharmProjects\\pythonProject4\\Farmacos\\Enfermedades mentales\\*.csv'):
    print(filename)
    with open(filename, "r") as n:
        de = csv.reader(n)
        for row in de:
            try:
                n = row[1]
                n = float(n.replace(",", "."))
                if type == str:
                    del row[1]
                preciario_depurado.append(n)

                #print(sum(preciario_depurado) / len(preciario_depurado))
                #print(preciario_depurado)
            except ValueError:
                pass



print(de)"""

""" df = open(filename, "r")
    print(df, type(df))"""


        #preciario_depurado.append(n)
        # print(sum(preciario_depurado) / len(preciario_depurado))

"""with open(filename, "r") as n:
        de = csv.reader(n)
        #print(de)
        for row in de:
            try:
                n = row[1]
                n = float(n.replace(",", "."))
                if type == str:
                    del row[1]
                preciario_depurado.append(n)

                #print(sum(preciario_depurado) / len(preciario_depurado))
                # print(preciario_depurado)
            except ValueError:
                pass"""
"""sns.set_theme(style="ticks")
f, ax = plt.subplots(figsize=(10, 2))

sns.boxplot(preciario_depurado,color= "plum",whis=[0, 100], width=.6, palette="vlag")
sns.stripplot(preciario_depurado, size=4, linewidth=0)
ptl.show()"""
