print("----------------------------")
print("-------Lista de datos-------")
print("----------------------------")
print("----------------------------")
num1 = int(input("Ingrese un numero de 1 a 100: "))
lista = list(range(1,num1 +1))
if num1 > 100 or num1 < 1:
    print("El numero debe estar entre 1 y 100")
else:
    result = sum(lista)
    print(f"La suma de la lista hasta {num1} es {result}")

