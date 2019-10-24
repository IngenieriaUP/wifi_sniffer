import tkinter as tk
from tkinter import *
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from subprocess import Popen, PIPE

import os

import subprocess

import numpy as np

window = Tk()
texto = tk.Label(window,text="")

def tshark():
    #os.system('iwconfig')
    #subprocess.run('tshark -V -i wlx8416f9131ae9 -T fields -E separator=, -E quote=d -e wlan.sa')
    #subprocess.run("iwconfig")
    subprocess.call('sudo /usr/bin/tshark -V -i  wlx8416f9131ae9 -T fields -E header=y -E separator="/s" -E quote=d -a duration:10 -e wlan.sa -e wlan.ra -e wlan.ta -e wlan.da -e frame.time -q > apolo55.csv',shell=True)


def iniciar():
    texto.config(text="DISPOSITIVOS DETECTADOS")
    texto.place(x=175,y=225)
    tshark()
    #subprocess.run('tshark -V -i wlx8416f9131ae9 -T fields -E header=y -E separator=, -E quote=d -e wlan.sa  -e frame.time -q -a duration:5 > lectura3.csv')
    #window.after(10000,lambda : texto.config(text='DISPOSITIVOS DETECTADOS'))

def grafico():
    texto.config(text = "Generando grafico...")
    texto.place(x=175, y=225)

    datos = pd.read_csv('apolo55.csv', sep=' ')
    informacion = pd.read_csv('diccionariofinal.csv', sep=';')
    dflectura = pd.DataFrame({'A': datos['wlan.sa']})
    # df['A'].unique()
    matrix = dflectura['A'].unique()
    dflecturaunica = pd.DataFrame({'L': list(matrix)})

    dfdic = pd.DataFrame({'D': informacion['MAC'], 'E': informacion['FABRICANTE']})

    # dflecturaunica['P']=((dflecturaunica.L.str[0:8]).str.upper()).isin(dfdic.D)

    # dflecturaunica['P']=np.nan

    dflecturaunica["M"] = dflecturaunica.L.str[0:8].str.upper()

    dflecturaunica["P"] = ''

    # print(dflecturaunica)

    for i in range(len(dflecturaunica)):
        for j in range(len(dfdic)):
            if (dflecturaunica["M"][i] == dfdic.D[j]):
                dflecturaunica["P"][i] = dfdic.E.loc[j]

    # crear graficos
    df = dflecturaunica

    df['Cantidad'] = 1

    dims = (30, 50)
    fig, ays = plt.subplots(figsize=dims)  # cambiar el 2 luego por el numero de columnas del dataframe final

    df_2 = df.groupby('P').sum()

    print(df_2)
    df_2.reset_index(inplace=True)
    df_2 = df_2.tail(len(df_2) - 1)

    chart = sns.barplot(x='P', y='Cantidad', data=df_2)

    for p in chart.patches:
        chart.set_xticklabels(chart.get_xticklabels(), rotation=90)
        chart.annotate(format(p.get_height(), '.2f'), (p.get_x() + p.get_width() / 2., p.get_height()), ha='center',
                       va='center', xytext=(0, 10), textcoords='offset points')

    # df_2 = df.groupby('Minuto').sum()
    # df_2.reset_index(inplace = True)
    # sns.barplot(x="Minuto", y="Cantidad", data = df_2,ax=axs[1])

    o = "El numero de\ndispositivos registrados\nes de: " + str(len(df))
    plt.figtext(21,5,o)
    plt.show()

    o = "El numero de\ndispositivos registrados\nes de: " + str(len(df))
    texto.config(text=o,width=30)
    texto.place(x=150, y=195)

# setting geometry of tk window
window.geometry("400x400")

window.title(" Lecturas con Antena")

Boton1 = tk.Button(window,text='INICIAR',command=iniciar)
Boton3 = tk.Button(window,text='GRAFICO',command=grafico)

Boton1.place(x=40, y = 175)
Boton3.place(x=40, y = 275)

logo1 = tk.PhotoImage(file="inginf.gif")
logo2 = logo1.subsample(1,1)
imag = tk.Label(image = logo2,height = 92, width = 400)
imag.place(x =0, y = 0)

window.mainloop()
