

def busqueda_binaria_Recursiva(lista, objetivo, izquierda,derecha): 
    while izquierda <= derecha:
        medio = (izquierda + derecha) //2
        valor_medio = lista[medio]
        if valor_medio == objetivo:          
            return medio  
        elif valor_medio < objetivo:
            return busqueda_binaria_Recursiva(lista, objetivo, medio+1, derecha)
        else:
            return busqueda_binaria_Recursiva(lista, objetivo, izquierda, medio-1)
    return -1

Lista_numeros = [1, 3, 5, 7, 9, 11, 13, 15,100]

numero_buscar = int(input("Ingresa un numero a buscar:"))

resultado= busqueda_binaria_Recursiva(Lista_numeros, numero_buscar, 0, len(Lista_numeros)-1)

if(resultado != -1):
    print("Número:", numero_buscar, "encontrado en la posición:", resultado)
else:
    print("No hay ese numero chamo... escribe otro pe")
