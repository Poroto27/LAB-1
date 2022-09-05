def codificar(mensaje, rotaciones):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    longitud_alfabeto = 26
    mensajeTemp = ""
    for letra in mensaje: # rot solo funciona con las letras del afabeto ingles, lo demas queda igual
        if not letra.isalpha() or letra.lower() == 'ñ':
            mensajeTemp += letra

        else:
            letraEnOrd = ord(letra)  #valor de la letra en ord

            if letra.isupper():
                inicioEnOrd = 65 #ord(65) = A, #ord(66) = B, ...
                posicion = (letraEnOrd - inicioEnOrd + rotaciones) % longitud_alfabeto # aplicar rot "rotaciones" a la letra
                mensajeTemp += (alfabeto[posicion]).upper() #agregar la letra al mensaje en proceso 

            else:
                inicioEnOrd = 97  #ord(97) = a, #ord(98) = b,...
                posicion = (letraEnOrd - inicioEnOrd + rotaciones) % longitud_alfabeto # aplicar rot "rotaciones" a la letra
                mensajeTemp += alfabeto[posicion] #agregar la letra al mensaje en proceso 

    return mensajeTemp


def decodificar(mensaje, rotaciones):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    longitud_alfabeto = 26
    mensajeTemp = ""
    for letra in mensaje: # rot solo funciona con las letras del afabeto ingles, lo demas queda igual
        if not letra.isalpha() or letra.lower() == 'ñ':
            mensajeTemp += letra
        
        else:
            letraEnOrd = ord(letra) #valor de la letra en ord

            if letra.isupper():
                inicioEnOrd = 65 #ord(65) = A, #ord(66) = B, ...
                posicion = (letraEnOrd - inicioEnOrd - rotaciones) % longitud_alfabeto # aplicar rot "rotaciones" a la letra
                mensajeTemp += (alfabeto[posicion]).upper() #agregar la letra al mensaje en proceso 

            else:
                inicioEnOrd = 97  #ord(97) = a, #ord(98) = b,...
                posicion = (letraEnOrd - inicioEnOrd - rotaciones) % longitud_alfabeto # aplicar rot "rotaciones" a la letra
                mensajeTemp += alfabeto[posicion] #agregar la letra al mensaje en proceso 

    return mensajeTemp
