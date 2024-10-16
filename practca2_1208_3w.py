print(" ")#sirve para dejar un espacio a la hora de ejecutar
print("Reyes Yañez Oscar Alonso_1208_3w:practica sobre datos personales")
print(" ")#sirve para dejar un espacio a la hora de ejecutar
nombre = input("Introduce tu nombre: ")#pide al usuario que ingrese su nombre 
edad = input("Introduce tu edad: ")#pide al usuario su edad
direccion = input("Introduce tu dirección: ")#pide la direccion de la persona
telefono = input("Introduce tu número de teléfono: ")#pide el numero de telefono
print(" ")#sirve para dejar un espacio a la hora de ejecutar
datos_usuario = {#se abre un diciionario donde saldran los siguientes datos
    'nombre': nombre,#declaracion de variable
    'edad': edad,#declaracion de variable
    'direccion': direccion,#declaracion de variable
    'telefono': telefono#declaracion de variable
}
print(" ")#sirve para dejar un espacio a la hora de ejecutar
print(f"{datos_usuario['nombre']} "
      f"tiene {datos_usuario['edad']} años, "
      f"vive en {datos_usuario['direccion']} "
      f"y su número de teléfono es {datos_usuario['telefono']}.")
print(" ")#sirve para dejar un espacio a la hora de ejecutar
