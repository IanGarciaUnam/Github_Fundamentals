
a=7
b=13
def suma(a,b):
    return a+b
def resta(a,b):
    return a-b
def division(a,b):
    if b==0:
        return "no es posible dividir entre 0"
    return a//b

def potencia(a,b):
    return a**b

def multiplicacion(a,b):
    return a*b

print("Suma: ",suma(a,b))
print("Resta: ", resta(a,b))
print("Division", division(a,b))
print("potencia: ",potencia(a,b))
print("multiplicacion: ",multiplicacion(a,b))