print("----------------------------")
print("-------Marlon Cruz----------")
print("----Codigo: USTR025024------")
print("----------------------------")
def tipo_numero(num1):
    if num1 > 0:
        tipo = "Positivo"
    elif num1 < 0:
        tipo = "negativo"
    else:
        tipo = "El numero es 0"
    return tipo
num = int(input("Ingrese un numero:" ))
print(f"El numero {num} es {tipo_numero(num)} ")