import matgenut, pprint, time

"""
Suponer que SIEMPRE se empieza conociendo la posición de A
"""

m = matgenut.genranmatr(5,5)
posB = matgenut.instcities(m)
matgenut.printmtrx(m)

iter = 0
finished = matgenut.check_if_iter_finished(m)
added_wave_positions = []

while not finished:
    iter += 1
    for fila in range(len(m)):
        for columna in range(len(m[fila]) -1):

            enviroment = matgenut.checkenv(m, fila, columna)
            enviroment_positions = enviroment.keys()
            surrounding_items = matgenut.get_surrounding_elements(enviroment)

            # (current_element of the enviroment)
            # c_env_elem = enviroment[position]["elem"]

            # Para la primera iteración, asegurar que se coloca un 1
            if m[fila][columna] == "A":
                print("Found A")
                m[0][0] == 1

                for position in enviroment_positions:
                    c_env_elem = enviroment[position]["elem"]
                    m[0][0] == 1

                    if c_env_elem == ".":
                        pos_fila = enviroment[position]["pos"][0]
                        pos_columna = enviroment[position]["pos"][1]
                        m[0][0] == 1

            # Si encuentra un numero, compararlo con la iteracion actual
            # y procesarlo si es de la iteracion anterior
            elif type(m[fila][columna]) == "int" and iter - m[fila][columna] == 1:

                for position in enviroment_positions:
                    c_env_elem = enviroment[position]["elem"]

                    if c_env_elem == ".":
                        pos_fila = enviroment[position]["pos"][0]
                        pos_columna = enviroment[position]["pos"][1]
                        m[pos_fila][pos_columna] == iter

            finished = matgenut.check_if_iter_finished(m)
            print("\n\n")
            matgenut.printmtrx(m)



print("Fin del algoritmo")
print("La matriz resultante es: ")
matgenut.printmtrx(m)
