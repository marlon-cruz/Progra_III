# calculadora
num1 = float(input("ingrese el primer numero para el calculo: "))
num2 = float(input("ingrese el segundo numero para el calculo: "))

operacion = input("Ingrese la operacion, suma, resta, multi, divi: ").lower()

if operacion == "suma":
    print("El resultado de la suma es: ", num1 + num2)
elif operacion == "resta":
    print("El resultado de la resta es: ", num1 - num2)
elif operacion == "multi":
    print("El resultado de la multiplicación es es: ", num1 * num2)
elif operacion == "divi":
    print("El resultado de la división es: ", num1 / num2)
else:
    print("Entre las selecciones no se encuentra lo que ha ingresado")