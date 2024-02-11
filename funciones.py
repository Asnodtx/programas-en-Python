def saludo(primer_nombre, apellido, edad):
    print("Hola " + primer_nombre + " " + apellido)
    print("Tienes " + str(edad) + " " + "Años")
    
nombre  = input("Ingresa tu nombre: ")
elapellido = input("Ingresa tu apellido: ")
anos = int(input("Ingresa tu edad: "))

saludo(nombre, elapellido, anos)