import re
#Expresiones regulares de palabras reservadas y OPERADORES
RESERVADAS = {
    'BLANCO':r'\s',
    'ENTERO':'INT',
    'CADENA':'STR',
    'OUTPUT':r'SALIDA'
}
OPERADORES = {
    'ID'     :r'[A-Za-z][A-Za-z_0-9]=*.*',
    'ASIG'   :r'.*=.*',
    'COMENT' :r'\#.*',
    'NUMEROS':r'.*\d',
    'CARACTERES':r'.*".*"'
}
#DICCIONARIO DE ERRORES
ERRORES = {
    1:"NO EXISTE EL TIPO DE DATO: ",
    2:"NOMBRE INVALIDO: ",
    3:"VARIABLE NO INICIALIZADA: ",
    4:"NO ES POSIBLE GUARDAR ESTE VALOR: "
}
#Clase para identificar variables con su información correspondiente
class NODO:
    def __int__(self):
        self.id=i
        self.tipo=t
        self.valor=v

    def setTIPO(self,t):
        self.tipo=t

    def setID(self,i):
        self.id=i

    def setVALOR(self,v):
        self.valor=v

    def getTIPO(self):
        return self.tipo

    def getID(self):
        return self.id

    def getVALOR(self):
        return self.valor

#REMOVER COMENTARIOS
def COMENTARIOS(cadena):
    p=re.compile(OPERADORES['COMENT'])
    aux=p.sub("",cadena)
    return aux;
# REVISA LA DECLARACIÓN DE LAS VARIABES
# NO TOMA EN CUANTA EL VALOR
def t_ANALIZA(tip,t,n):
    print("TIPO: "+tip)
    #Creacion del nodo para añadirlo a la lista
    nodo = NODO()
    nodo.setTIPO(tip)
    p_INT=re.compile(OPERADORES['ID'])
    matcher = p_INT.match(t)
    if matcher:#verifica si es valido el nombre de la variable
        cad=""
        for i in t:
            if (i == "="):
                print ("IDENTIFICADOR: "+cad)
                nodo.setID(cad)#Guarda el valor del indentificador
            else:
                cad+=i
        p_INT=re.compile(OPERADORES['ASIG'])
        matcher = p_INT.match(t)
        if matcher:#Revisa si esta inicializada la variable
            if(n==1):
                p_INT=re.compile(OPERADORES['NUMEROS'])
            elif(n==2):
                p_INT=re.compile(OPERADORES['CARACTERES'])
            matcher = p_INT.match(t)
            if matcher:#Revisa que sea valio el valor en la variable
                cad=""
                for i in t:
                    if i== "=":
                        print ("VALOR: "+cad)
                        nodo.setVALOR(cad)#valor de la variable
                        lineas.append(nodo)
                    else:
                        cad+=i
            else:
                print(ERRORES[4]+t)
        else:
            print(ERRORES[3]+t)

    else:
        print(ERRORES[2]+t)


#Manda cada instrucción a su función correspondiente
#dependiendo si delcaración de variables INT o STR, IMPRIMIR, LEER)
def instrucciones(ins):
    #Se envia a analizar(cadena,tipo) 1)ENTERO 2)CADENA
    swt=ins[:3]
    if(swt == RESERVADAS['ENTERO']):
        #Guarda el tipo de dato de la variable
        t_ANALIZA(swt,ins[3:],1)
    elif(swt == RESERVADAS['CADENA']):
        t_ANALIZA(swt,ins[3:],2)
    else:
        print(ERRORES[1]+ins)

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
