import re
#Expresiones regulares de palabras reservadas y OPERADORES
RESERVADAS = {
    'BLANCO':r'\s',
    'ENTERO':'INT',
    'CADENA':'STR',
    'OUTPUT':r'SALIDA\(".*"\)',
    'INPUT' :r'ENTRADA'
}
OPERADORES = {
    'ID'     :r'[A-Za-z]+[A-Za-z_0-9]*=+.*',
    'ASIG'   :r'=.*',
    'COMENT' :r'\#.*',
    'NUMEROS':r'\d',
    'CARACTERES':r'".*"$'
}
#DICCIONARIO DE ERRORES
ERRORES = {
    1:"NO EXISTE EL TIPO DE DATO: ",
    2:"NOMBRE INVALIDO: ",
    3:"VARIABLE NO INICIALIZADA: ",
    4:"NO ES POSIBLE GUARDAR EL VALOR: ",
    5:"YA EXISTE LA VARIABLE: "
}
#Clase para identificar variables con su información correspondiente
class NODO:
    def __int__(self):
        self.id=""
        self.tipo=""
        self.valor=""

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
#IMPRIMIR CADENAS DE TEXTO
def SALIDAtexto():
    pass
#IMPRIMIR VARIABLES STR
def SALIDASTR():
    pass
#IMPRIMIR VARIABLES INT
def SALIDAINT():
    pass
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
    #valores iniciales del nodo
    nodo.setTIPO(tip)
    nodo.setID("")
    nodo.setVALOR("")
    p_INT=re.compile(OPERADORES['ID'])
    matcher = p_INT.match(t)
    if matcher:#verifica si es valido el nombre de la variable
        cad=""
        for i in t:
            if (i == "="):
                print ("IDENTIFICADOR: "+cad)
                j=t.find("=")#obtiene la posición del simbolo =
                nodo.setID(cad)#Guarda el valor del indentificador
                cad=t[j:]#corta la cadena para tener solo el valor de la variable
                break
            else:
                cad+=i
        t=cad
        p_INT=re.compile(OPERADORES['ASIG'])
        matcher = p_INT.match(t)
        if matcher:#Revisa si esta inicializada la variable
            if(n==1):
                p_INT=re.compile(OPERADORES['NUMEROS'])
            elif(n==2):
                p_INT=re.compile(OPERADORES['CARACTERES'])
            t=t[1:]
            matcher = p_INT.match(t)
            if matcher:#Revisa que sea valio el valor en la variable
                print ("VALOR: "+t)
                nodo.setVALOR(cad)#valor de la variable
            else:
                print(ERRORES[4]+t)
        else:
            print(ERRORES[3]+t)
    else:
        print(ERRORES[2]+t)
    return nodo


#Manda cada instrucción a su función correspondiente
#dependiendo si delcaración de variables INT o STR, IMPRIMIR, LEER)
def instrucciones(ins):
    #Se envia a analizar(tip,cadena,tipo) tip: cadena con el nombre del tipo de dato
    #  1)ENTERO 2)CADENA
    nodo=NODO()
    nodo.setTIPO("")
    nodo.setID("")
    nodo.setVALOR("")
    swt=ins[:3]
    if(swt == RESERVADAS['ENTERO']):
        #Guarda el tipo de dato de la variable
        nodo=t_ANALIZA(swt,ins[3:],1)
    elif(swt == RESERVADAS['CADENA']):
        nodo=t_ANALIZA(swt,ins[3:],2)
    else:
        swt=ins[:6]
        impresion=""
        mensaje=""
        if(swt== "SALIDA"):
            patron=re.compile(RESERVADAS['OUTPUT'])
            if(patron.match(ins)):
                mensaje=ins[8:-2]
                print(mensaje)
                print("Correcto")
            else:
                print("Incorrecto")
        else:
            print(ERRORES[1]+ins)
            nodo.setTIPO("")
            nodo.setID("")
            nodo.setVALOR("")
    return nodo
