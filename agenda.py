#guardar contactos en un archivo
contactos = ["Emmanuel - 9613482476", "Fatima - 331710 3413"]
with open("contactos.txt", "w") as archivo:
    for contacto in contactos:
        archivo.write(contacto + "\n")
print("Contactos guardados en contactos.txt")

# leer contactos desde un archivo
with open("contactos.txt", "r") as archivo:
    contendido = archivo.read()
    print(contendido)