import random, pprint, time

def generarListaAleatoria(largo):
    lista = []
    for num in range(largo):
        lista.append(random.choice(["*", "-"]))

    return lista

def generarMatrizAleatoria(alto, ancho):
    matriz = []
    for columna in range(alto):
        matriz.append(generarListaAleatoria(ancho))

    return matriz

def printMatriz(matriz):
    for fila in matriz:
        for elemento in fila:
            print(elemento, end="    ")
        print("\n")

def insertWaypoints(matriz):

    # Insertar aleatoriamente una "a"
    filaA_index = random.randint(0, len(matriz) -1)
    posA = random.randint(0, len(matriz[filaA_index]) -1)
    matriz[filaA_index][posA] = "A"

    # En "b", comprobar antes que no haya una "a" en la misma posicion
    filaB_index = random.randint(0, len(matriz) -1)
    posB = random.randint(0, len(matriz[filaB_index]) -1)

    # Evitar que a y b estén en la misma posicion
    # aunque si pueden estar en la misma fila
    while posB == posA:
        posB = random.randint(0, len(matriz[filaB_index]) -1)

    matriz[filaB_index][posB] = "B"

def comprobarEntorno(matriz, pX, pY):
    """
    Comprueba si existe un * en el entorno
    de un elemento
    """
    keys = {"*": 1, "-": 0, "A": 0, "B": 0}
    if pY > 0:
        arriba = matriz[pY - 1][pX]
        found.append(arriba)

        if pX < len(matriz[pX]):
            arriba_derecha = matriz[pY - 1][pX + 1]
            found.append(arriba_derecha)

        if pX > 0:
            arriba_izquierda = matriz[pY - 1][pX - 1]
            found.append(arriba_izquierda)

    if pY < len(matriz) - 1:
        abajo = matriz[pY + 1][pX]
        found.append(abajo)

        if pX < len(matriz[pX]):
            abajo_derecha = matriz[pY + 1][pX + 1]
            found.append(abajo_derecha)

        if pX > 0:
            abajo_izquierda = matriz[pY + 1][pX - 1]
            found.append(abajo_izquierda)

    if pX < len(matriz[pX]):
        derecha = found.append(matriz[pY][pX + 1])
        found.append(derecha)

    if pX > 0:
        izquierda = matriz[pY][pX - 1]
        found.append(izquierda)

    pprint.pprint(found, indent=4)
    return found

# indica si existe algun camino entre A y B
def hayCamino(matriz): #posA, posB):
    # En primer lugar, buscar puntos en el entorno de A
    #for fila in range(len(matriz)):
    #    for elemento in range(len(matriz[fila])):
    print(matriz[0][0])
    print(f"({0}, {0})--> {comprobarEntorno(matriz, 0, 0)} ")

def main():
    mapa = generarMatrizAleatoria(2,2)
    insertWaypoints(mapa)
    printMatriz(mapa)
    hayCamino(mapa)

main()

