import Declaraciones as DEC
import re

def nombreVAR(index1,idVar):
    for i in lineas:
        #print("id "+ i.getID() + " valor " + i.getVALOR() + " tipo " + i.getTIPO())
        if(i.getID()!= "" and
            i.getVALOR!= "" and
            i.getTIPO()!= ""):#Asegura que no este vacio el nodo
            if(index1 != lineas.index(i)):
                if(idVar == i.getID()):
                    print(DEC.ERRORES[5]+ idVar)
                    break

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
depuracion= patron.sub('',DEC.COMENTARIOS(cadena))
#depuración es una variable co el codigo del programa sin basura
print("Depuracion: "+depuracion)
#detecta instruccion por instruccion para analizar
cad=""
lineas=[]
nodo=DEC.NODO()
nodo.setTIPO("")
nodo.setID("")
nodo.setVALOR("")
for i in depuracion:
        if i == ';':
            #print(cad)
            nodo=DEC.instrucciones(cad)
            lineas.append(nodo)
            index1=lineas.index(nodo)#retorna el index del nodo actual
            nombreVAR(index1,nodo.getID())
            cad=""
        else:
            cad+=i
