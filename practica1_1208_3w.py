print(" ")#sirve para dejar un espacio a la hora de ejecutar
print("Reyes Yañez Oscar Alonso_1208_3w:practica de diccionario sobre tipos de monedas")
print(" ")#sirve para dejar un espacio a la hora de ejecutar
divisas = {'Euro': '€', 'Dollar': '$', 'Yen': '¥'}#se guardan en el diccionario las divisas o tipos de monedas
print(" ")#sirve para dejar un espacio a la hora de ejecutar
divisa_input = input("Introduce una divisa (Euro, Dollar, Yen): ")#te solicita que introduzcas una divisa
print(" ")#sirve para dejar un espacio a la hora de ejecutar
if divisa_input in divisas:
    print(f"El símbolo de {divisa_input} es: {divisas[divisa_input]}")#te pide el simbolo de la divisa 
else:
    print("La divisa está en el diccionario.")#te manda un mensaje sobre que tu divisa no se encuentra en el diccionario
print(" ")#sirve para dejar un espacio a la hora de ejecutar