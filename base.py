#!/usr/bin/env python3

#falta: leer de json, ademas falta poder agregar multiples definiciones
#y tratar de alguna forma a los argumentos que se pasen

#importar
import sys
import json
import os

def capturar():
    palabra_agre = input("Que se va a definir: ")
    definicion_agre = input(f"Cual es el significado de {palabra_agre}: ")
    return (palabra_agre,definicion_agre)

def consultar():
    palabra_cons = input("Que palabra quieres consultar? ")
    return palabra_cons


argumentos = [x[1:] for x in sys.argv if "-"==x[0]]

if("e" in argumentos):
    palabra = capturar()
    diccionario_presente = 'diccionario.json' in os.listdir()
    if(diccionario_presente):
        with open('diccionario.json', 'r') as diccio:
            datos = json.load(diccio)
            datos[palabra[0]] = palabra[1]
    else:
        datos = {palabra[0]:palabra[1]}
    with open('diccionario.json', 'w') as diccio:
        json.dump(datos,diccio, indent = 2)
elif("c" in argumentos):
    palabra = consultar()
    with open('diccionario.json', 'r') as diccio:
        datos = json.load(diccio)
        if(palabra in datos.keys()):
            print(f"{palabra}: {datos[palabra]}")
        else:
            print("palabra no encontrada")
