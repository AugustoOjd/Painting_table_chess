# Considera a un muchacho que se deleita pintando su tablero de ajedrez. Su objetivo es saturar cada celda con tonos rojos o azules. En busca de darle una identidad propia, procura tener un equilibrio entre los espacios rojos y azules, previniendo que dos filas o columnas contengan el mismo número de celdas rojas. ¿Lograría pintar el tablero de ajedrez siguiendo estas pautas? ¿Qué acontecería si, en vez de un tablero de ajedrez común de 8x8, tuviera uno monumental de 1000x1000?s


# Primero creo dos variables para agregas values desde inputs
Row = int(input("Enter the number of rows:"))
Column = int(input("Enter the number of columns:"))
 
# Creo una lista vacia
tablero = []

# Aplico for a los inputs ingresados
# Por cada row ingresada se crea una columna
# la columna seran de 0 y 1, 
# azul seria el 0 y rojo el 1

for row in range(Row):   
    a = []
    for column in range(Column):
        # Aplico condicionales para generar ceros y unos
        # Si el anterior es 1 agrego 0 sino lo contrario
        # Voy agregando todo la lista a
        for n in range(Row):
            if(len(a) > 1):
                if(a[n - 1] == 0):
                    a.append(1)
                elif(a[n - 1] == 1):
                    a.append(0)
            else:
                a.append(n)
    tablero.append(a)

# Despues te generar la cantidad de rows y columns
# Paso a imprimirlos en consola
# aplico otro for para mostrar la misma cantidad de rows y columns
for row in range(Row):
    for column in range(Column):
        # Cuando voy hacer un print a row le sumo columns para que corra un espacio
        print(tablero[row][row+column], end=" ")
    print()

# La otra menera mas facil era usando la libreria numpy pero quise hacer de forma

# row = int(input("Enter the number of rows:"))
# column = int(input("Enter the number of columns:"))
# Libreria numpy
# import numpy as np
# x = np.zeros((row, column))
# print(x)