import Declaraciones
import re
#Abrir archivo
archivo = open("fuente.txt","r")
lol= archivo.read()
archivo.close()

#CADENA QUE SE VA ANALIZAR
#cadena='#hola mundo \n  hola="gjk5"; #otro INT  perro = 8; \n INT no_  45;'
cadena=lol
#print(cadena)
#Limpia comentarios, enter y tabulaciones
# (Cuaquier espacio en blanco y comentarios del lenguaje)
patron = re.compile(r'\s')
depuracion= patron.sub('',COMENTARIOS(cadena))
#depuración es una variable co el codigo del programa sin basura
print("Depuracion: "+depuracion)
#detecta instruccion por instruccion para analizar
cad=""
lineas=[]

for i in depuracion:
        if i == ';':
            #print(cad)
            instrucciones(cad)
            cad=""
        else:
            #print(cad)
            cad+=i
