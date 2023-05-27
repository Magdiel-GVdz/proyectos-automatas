import keyword
import re

def analizador_lexico(codigo):
    # Definición de patrones para los diferentes tipos de tokens
    patrones = {
        'NUMERO': r'\d+',                     # Números
        'OPERADOR': r'[+\-*/]',                # Operadores aritméticos
        'PARENTESIS': r'[()]',                 # Paréntesis
        'ESPACIO': r'\s+',                     # Espacios en blanco
        'COMENTARIO': r'#.*',                  # Comentarios
        'CADENA': r'"[^"]*"',                  # Cadenas de texto entre comillas dobles
        'BOOLEANO': r'True|False',              # Valores booleanos True y False
        'DOS_PUNTOS': r':',                     # Dos puntos
        'NONE': r'None',                        # Valor None
        'COMPARADOR': r'[<>!=]=?',              # Operadores de comparación
        'COMA': r',',                           # Coma
    }

    # Obtener palabras reservadas de Python y agregarlas a los patrones
    palabras_reservadas = keyword.kwlist
    patrones.update({palabra.upper(): r'\b' + palabra + r'\b' for palabra in palabras_reservadas})

    patron_identificador = r'[a-zA-Z_]\w*'     # Identificador válido

    tokens = []                                # Lista para almacenar los tokens encontrados
    posicion = 0                              # Posición actual en el código fuente

    regex_identificador = re.compile(patron_identificador)             # Regex para identificadores
    regex_patrones = {etiqueta: re.compile(patron) for etiqueta, patron in patrones.items()}    # Regex para los demás patrones

    while posicion < len(codigo):
        coincidencia_identificador = regex_identificador.match(codigo[posicion:])

        if coincidencia_identificador:
            valor_identificador = coincidencia_identificador.group(0)
            if valor_identificador in palabras_reservadas:
                token = (valor_identificador.upper(), valor_identificador)    # Token de palabra reservada
            else:
                token = ('IDENTIFICADOR', valor_identificador)                # Token de identificador
            tokens.append(token)
            posicion += coincidencia_identificador.end()
            continue

        for etiqueta, regex in regex_patrones.items():
            if regex.match(codigo[posicion:]):
                valor = regex.match(codigo[posicion:]).group(0)
                token = (etiqueta, valor)            # Token de tipo específico (número, operador, etc.)
                tokens.append(token)
                posicion += len(valor)
                break
        else:
            print('Error: Carácter no válido en la posición', posicion)
            break

    return tokens

def main():
    nombre_archivo = "prueba.py"

    with open(nombre_archivo, 'r') as archivo:
        codigo_fuente = archivo.read()

    tokens = analizador_lexico(codigo_fuente)

    for token in tokens:
        print(token)

if __name__ == "__main__":
    main()
