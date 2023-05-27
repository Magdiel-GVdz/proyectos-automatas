def contar_lineas(archivo):
    with open(archivo, 'r') as f:
        lineas = f.readlines()
        return len(lineas)

def main():
    nombre_archivo = "prueba.py"

    numero_lineas = contar_lineas(nombre_archivo)
    
    print(numero_lineas)

if __name__ == "__main__":
    main()
