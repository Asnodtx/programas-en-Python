import os

path = 'C:\\Users\\maren\\OneDrive\\Documentos\\test.txt'

if os.path.exists(path):
    print("Esa ubicacion existe")
    if os.path.isfile(path):
        print("Es un archivo")
    elif os.path.isdir(path):
        print("Es un directorio")
else:
    print("La ubicacion no existe")