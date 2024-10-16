print(" ")#sirve para dejar un espacio a la hora de ejecutar
print("Reyes Yañez Oscar Alonso_1208_3w:practica sobre frutas, kilos y precio ")
print(" ")#sirve para dejar un espacio a la hora de ejecutar
precios_frutas = {#se crea un diccionario
    'manzana': 12, #variable nro1 del diccionario
    'plátano': 15,#variable 2 del diccionario
    'naranja': 10,#variable 3 del diccionario
    'fresa': 15,#variable 4 del diccionario
    'kiwi':20#variable 5 del diccionario
}
print(" ")#sirve para dejar un espacio a la hora de ejecutar
fruta = input("Introduce la fruta (manzana, platano macho, naranja, fresa, kiwi ): ").lower()#te pide que selecciones una fruta
kilos = float(input("Introduce el número de kilos: "))#te pide que ingreses la cantidad de kilos
print(" ")#sirve para dejar un espacio a la hora de ejecutar
if fruta in precios_frutas:
    precio_total = precios_frutas[fruta] * kilos
    print(f"El precio de {kilos} kilos de {fruta} es: {precio_total:.2f} pesos")#te dice el precio por los kilos que seleccionaste
else:
    print("La fruta no está en el diccionario.")#te dice que la fruta que seleccionaste no esta en el diccionario
print(" ")#sirve para dejar un espacio a la hora de ejecutar