def ordenar(lista):
    for i in range(len(lista)):
        for j in range(i+1,len(lista)):
            if lista[j] < lista[i]:
                lista[i],lista[j] = lista[j],lista[i]
    return lista
    
lista = [19,354,11000,7,0.5]
listaCerto = ordenar(lista)
print("A lista ordenada é:", listaCerto)

