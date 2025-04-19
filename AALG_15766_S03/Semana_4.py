def resta(a,b):

    return a-b

def multiplicacion(a:int,b:int) -> int:

    return a*b

def saludo(a:str) -> str:

    x = "Hola "+ a

    return x

def despedida(a:str) -> None:
    x = "Ponle ;  "+ a
    print(x)

c = 5
d : int = 2
print(resta(c,d))

print(multiplicacion(c,d))

print(saludo("Carlos"))

despedida("Carlos")