def crearCadena (cadena):
    nuevaCadena = []
    indice = len(cadena)
    while indice:
        indice -=1
        nuevaCadena.append(cadena[indice])
    return "".join(nuevaCadena)

cadena = "ATGC"

crearCadena(cadena)

