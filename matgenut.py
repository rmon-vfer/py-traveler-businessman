# The Matrix Generation Utilities for TSM
# Ramón Vila Ferreres - 2018

import random

def genranmatr(alto, ancho):
    matriz = []
    for fila in range(alto):
        fila = []
        for elem in range(ancho):
            fila.append(random.choice(["*", "."]))
        matriz.append(fila)
    return matriz

def printmtrx(matriz):
    for fila in matriz:
        for elemento in fila:
            print(elemento, end="    ")
        print("\n")

def instcities(matriz):
    filaA = random.randint(0, len(matriz) - 1)
    filaB = random.randint(0, len(matriz) - 1)

    columnaA = random.randint(0, len(matriz[filaA]) - 1)
    columnaB = random.randint(0, len(matriz[filaB]) - 1)
    while columnaB == columnaA:
        columnaB = random.randint(0, len(matriz[filaB]) - 1)

    matriz[filaA][columnaA] = "A"
    matriz[filaB][columnaB] = "B"

    return [filaB, columnaB]

def checkenv(matriz, fila, columna):
    entorno = {}
    if fila == 0:
        if columna == 0:
            aba = matriz[fila + 1][columna]
            dcha = matriz[fila][columna + 1]
            aba_dcha = matriz[fila + 1][columna + 1]

            entorno["aba"] = {}
            entorno["dcha"] = {}
            entorno["aba_dcha"] = {}

            entorno["aba"]["pos"] = [fila + 1, columna]
            entorno["dcha"]["pos"] = [fila, columna + 1]
            entorno["aba_dcha"]["pos"] = [fila + 1, columna + 1]

            entorno["aba"]["elem"] = aba
            entorno["dcha"]["elem"] = dcha
            entorno["aba_dcha"]["elem"] = aba_dcha

        elif columna > 0 and columna < len(matriz[fila]) - 1:
            aba = matriz[fila + 1][columna]
            izq = matriz[fila][columna - 1]
            dcha = matriz[fila][columna + 1]

            aba_izq = matriz[fila + 1][columna - 1]
            aba_dcha = matriz[fila + 1][columna + 1]

            entorno["aba"] = {}
            entorno["izq"] = {}
            entorno["dcha"] = {}
            entorno["aba_izq"] = {}
            entorno["aba_dcha"] = {}

            entorno["aba"]["pos"] = [fila + 1, columna]
            entorno["izq"]["pos"] = [fila, columna - 1]
            entorno["dcha"]["pos"] = [fila, columna + 1]
            entorno["aba_izq"]["pos"] = [fila + 1, columna - 1]
            entorno["aba_dcha"]["pos"] = [fila + 1, columna + 1]

            entorno["aba"]["elem"] = aba
            entorno["izq"]["elem"] = izq
            entorno["dcha"]["elem"] = dcha
            entorno["aba_izq"]["elem"] = aba_izq
            entorno["aba_dcha"]["elem"] = aba_dcha

        elif columna == len(matriz[fila]) - 1:
            aba = matriz[fila + 1][columna]
            izq = matriz[fila][columna - 1]

            aba_izq = matriz[fila + 1][columna - 1]

            entorno["aba"] = {}
            entorno["izq"] = {}
            entorno["aba_izq"] = {}

            entorno["aba"]["pos"] = [fila + 1, columna]
            entorno["izq"]["pos"] = [fila, columna - 1]
            entorno["aba_izq"]["pos"] = [fila + 1, columna - 1]

            entorno["aba"]["elem"] = aba
            entorno["izq"]["elem"] = izq
            entorno["aba_izq"]["elem"] = aba_izq

    elif fila > 0 and fila < len(matriz) - 1:

        arr = matriz[fila - 1][columna]
        aba = matriz[fila + 1][columna]
        izq = matriz[fila][columna - 1]
        dcha = matriz[fila][columna + 1]

        arr_izq = matriz[fila - 1][columna - 1]
        arr_dcha = matriz[fila - 1][columna + 1]
        aba_izq = matriz[fila + 1][columna - 1]
        aba_dcha = matriz[fila + 1][columna + 1]

        entorno["arr"] = {}
        entorno["aba"] = {}
        entorno["izq"] = {}
        entorno["dcha"] = {}
        entorno["arr_izq"] = {}
        entorno["arr_dcha"] = {}
        entorno["aba_izq"] = {}
        entorno["aba_dcha"] = {}

        entorno["arr"]["pos"] = [fila - 1, columna]
        entorno["aba"]["pos"] = [fila + 1, columna]
        entorno["izq"]["pos"] = [fila, columna - 1]
        entorno["dcha"]["pos"] = [fila, columna + 1]
        entorno["arr_izq"]["pos"] = [fila - 1, columna - 1]
        entorno["arr_dcha"]["pos"] = [fila - 1, columna + 1]
        entorno["aba_izq"]["pos"] = [fila + 1, columna - 1]
        entorno["aba_dcha"]["pos"] = [fila + 1, columna + 1]

        entorno["arr"]["elem"] = arr
        entorno["aba"]["elem"] = aba
        entorno["izq"]["elem"] = izq
        entorno["dcha"]["elem"] = dcha

        entorno["arr_izq"]["elem"] = arr_izq
        entorno["arr_dcha"]["elem"] = arr_dcha
        entorno["aba_izq"]["elem"] = aba_izq
        entorno["aba_dcha"]["elem"] = aba_dcha

    elif fila == len(matriz) - 1:
        if columna == 0:
            arr = matriz[fila - 1][columna]
            dcha = matriz[fila][columna + 1]
            arr_dcha = matriz[fila - 1][columna + 1]

            entorno["arr"] = {}
            entorno["dcha"] = {}
            entorno["arr_dcha"] = {}

            entorno["arr"]["pos"] = [fila - 1, columna]
            entorno["dcha"]["pos"] = [fila, columna + 1]
            entorno["arr_dcha"]["pos"] = [fila - 1, columna + 1]

            entorno["arr"]["elem"] = arr
            entorno["dcha"]["elem"] = dcha

            entorno["arr_dcha"]["elem"] = arr_dcha

        elif columna > 0 and columna < len(matriz[fila]) - 1:
            arr = matriz[fila - 1][columna]
            izq = matriz[fila][columna - 1]
            dcha = matriz[fila][columna + 1]

            arr_izq = matriz[fila - 1][columna - 1]
            arr_dcha = matriz[fila - 1][columna + 1]

            entorno["arr"] = {}
            entorno["izq"] = {}
            entorno["dcha"] = {}
            entorno["arr_izq"] = {}
            entorno["arr_dcha"] = {}

            entorno["arr"]["pos"] = [fila - 1, columna]
            entorno["izq"]["pos"] = [fila, columna - 1]
            entorno["dcha"]["pos"] = [fila, columna + 1]
            entorno["arr_izq"]["pos"] = [fila - 1, columna - 1]
            entorno["arr_dcha"]["pos"] = [fila - 1, columna + 1]

            entorno["arr"]["elem"] = arr
            entorno["izq"]["elem"] = izq
            entorno["dcha"]["elem"] = dcha

            entorno["arr_izq"]["elem"] = arr_izq
            entorno["arr_dcha"]["elem"] = arr_dcha

        elif columna == len(matriz[fila]) - 1:
            arr = matriz[fila - 1][columna]
            izq = matriz[fila][columna - 1]
            arr_izq = matriz[fila - 1][columna - 1]

            entorno["arr"] = {}
            entorno["izq"] = {}
            entorno["arr_izq"] = {}

            entorno["arr"]["pos"] = [fila - 1, columna]
            entorno["izq"]["pos"] = [fila, columna - 1]
            entorno["arr_izq"]["pos"] = [fila - 1, columna - 1]

            entorno["arr"]["elem"] = arr
            entorno["izq"]["elem"] = izq
            entorno["arr_izq"]["elem"] = arr_izq

    return entorno

def check_if_iter_finished(matrix):
    matrix_elements = []

    for fila in matrix:
        for elemento in fila:
            matrix_elements.append(elemento)

    return  "." not in matrix_elements

def get_surrounding_elements(entorno):
    s_elements = []
    for k, v in entorno.items():
        s_elements.append(v["elem"])

    return s_elements

def search_waypoint(waypoint, m):
    for fila in range(len(m)):
        for columna in range(len(m[fila]) -1):
            if m[fila][columna] == waypoint:
                return [fila, columna]
