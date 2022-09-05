import Rot
import Vigenere
import requests
def cifrado(mensaje,clave):
    defi=Rot.codificar(mensaje,8)
    defini=Vigenere.cifrar_mensaje(clave,defi)
    definite=Rot.codificar(defini,12)
    print('Mensaje cifrado: ',definite)
    return(definite)
def decifrado(mensaje,clave):
    defi=Rot.decodificar(mensaje,12)
    defini=Vigenere.descifrar_mensaje(clave,defi)
    definite=Rot.decodificar(defini,8)
    print('Mensaje descifrado: ',definite)
    return(definite)

##Desafio 1
print('Desafio 1')
Clave='heropassword'
mensaje=input('Escriba un mensaje:')
print('El mensaje es: ',mensaje)
headers = {
    'Content-Type': 'text/plain',
}

data = {"msg":cifrado(mensaje,Clave)}

response = requests.post('https://finis.mmae.cl/SendMsg', headers=headers, data=data)
##Desafio 2
print('Desafio 2')
Clave='finispasswd'
headers = {
    'Content-Type': 'text/plain',
}
response = requests.get('https://finis.mmae.cl/GetMsg', headers=headers)
mensaje2='DuaqQbOzYukrcqgEnwdqjl'
decodificado= decifrado(mensaje2,Clave)
