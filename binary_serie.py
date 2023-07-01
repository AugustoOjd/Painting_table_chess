
lista = []
for n in range(10):
    if(len(lista) > 1):
        if(lista[n - 1] == 0):
            lista.append(1)
        elif(lista[n - 1] == 1):
            lista.append(0)
    else:
        lista.append(n)
    print(lista)