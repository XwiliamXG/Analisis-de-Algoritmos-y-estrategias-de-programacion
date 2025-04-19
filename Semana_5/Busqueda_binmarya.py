

def busqueda_binaria(lista, objetivo):
    izquierda = 0
    derecha = len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) //2
        valor_medio = lista[medio]
        if valor_medio == objetivo:
            return medio  
        elif valor_medio < objetivo:
            izquierda = medio + 1  
        else:
            derecha = medio - 1  
    return -1  

Lista_numeros = [1, 3, 5, 7, 9, 11, 13, 15,100]
print("Ingresa el número a buscar:")
numero_buscar = int(input())
posicion = busqueda_binaria(Lista_numeros, numero_buscar)

if posicion != -1:
    print("Número:", numero_buscar, "encontrado en la posición:", posicion+1)
else:
    print("No hay ese numero chamo... escribe otro pe")



