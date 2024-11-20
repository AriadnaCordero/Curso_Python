'''

Escribe un programa que solicite al usuario dos números y muestre su
suma, resta, multiplicación, división, división entera y residuo (módulo).

'''
num1= float(input("ingresa el primer numero: "))
num2= float(input("ingresa el segundo numero: "))
suma= num1+num2
resta= num1-num2
mult= num1=num2
division= num1/num2 if num2 !=0 else "No se puede dividir entre cero"
divisionEntera= num1//num2 if num2 !=0 else "No se puede dividir entre cero"
modulo= num1%num2 if num2 !=0 else "No se puede calcular el residuo"
print(f"suma: {suma}")
print(f"resta: {resta}")
print(f"mult: {mult}")
print(f"division: {division}")
print(f"division Entera: {divisionEntera}")
print(f"modulo: {modulo}")