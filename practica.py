valores=list('0123456789')
n=50
pila=[]
postfija=[]
tope=-1

def menu():
    print("""
-------------------------------------------
LENGUAJES FORMALES Y DE PROGRAMACIÓN
MARCOS GEOVANI JOSÍAS PÉREZ SECAY
201903878
-------------------------------------------
1.- Cargar archivo
2.- Graficar operación
3.- Salir
""")

def llena():
    if(tope==(n-1)):
        print ("Lleno")
        return True
    return False

def vacia():
    if(tope==-1):
        print ("vacio")
        return True
    return False

def push(dato):
    if (llena()!=True):
        global tope
        tope=tope+1
        pila.insert(tope,dato)

def pop():
    if (vacia()!=True):
        global tope
        auxiliar=pila[tope]
        del pila[tope]
        tope=tope-1
        return auxiliar
    else:
        return 0

def infija(i,en_lista):
    if en_lista[i]=='^':
        prioridadexp=4
        return prioridadexp
    elif en_lista[i]=='*':
        prioridadexp=2
        return prioridadexp
    elif en_lista[i]=='/':
        prioridadexp=2
        return prioridadexp
    elif en_lista[i]=='+':
        prioridadexp=1
        return prioridadexp
    elif en_lista[i]=='-':
        prioridadexp=1
        return prioridadexp
    elif en_lista[i]=='(':
        prioridadexp=5
        return prioridadexp

def prioridadpila(pila):
    if pila[tope]=='^':
        prioridadPI=3
        return prioridadPI
    elif pila[tope]=='*':
        prioridadPI=2
        return prioridadPI
    elif pila[tope]=='/':
        prioridadPI=2
        return prioridadPI
    elif pila[tope]=='+':
        prioridadPI=1
        return prioridadPI
    elif pila[tope]=='-':
        prioridadPI=1
        return prioridadPI
    elif pila[tope]=='(':
        prioridadPI=0
        return prioridadPI

def to_pos(en_lista):
    for i in range(len(en_lista)):
        if en_lista[i] in valores:
            postfija.append(en_lista[i])
            print("Voy pasando por 1")
        elif en_lista[i]!=')':
            if tope==-1:
                push(en_lista[i])
                print("Voy pasando por 2")
            else:
                if infija(i,en_lista)<=prioridadpila(pila):
                    postfija.append(pop())
                    push(en_lista[i])
                    print("Voy pasando por 3")
                elif infija(i,en_lista)>prioridadpila(pila):
                    push(en_lista[i]) #Se desapila
                    print("Voy pasando por 4")
        elif en_lista[i]==')':
            while pila[tope]!='(':
                postfija.append(pop())
                print("Voy pasando por 5")
            if pila[tope]=='(':
                pop()
                print("Voy pasando por 6")
                    
            elif tope!=-1:
                    postfija.append(pop())
                    print("Voy pasando por 7")
    while tope>-1:
        postfija.append(pop())
    print("".join(postfija))
    print("aca tendria que imprimir la pila")

#Acá se abre el documento
def OpenFile():
    ruta = input("INGRESA LA RUTA DE ARCHIVO: ") #Ingreso la ruta
    leyendo = open (ruta,'r')#Se abre en modo lectura
    linea = leyendo.readline()#Lee linea por linea
    while linea!="": #Mientras hayan lineas (No se si sea correcto decir eso)
        print(linea, end='')#Imprimo la operacion original
        en_lista=list(linea.rstrip('\n').split())#y lo paso a una lista
        #Antes de imprimir todo tengo que usar la función que usé para imprimir la lista ordenada
        print (en_lista)#imprimo la lista  
        linea = leyendo.readline()#Continua leyendo
        to_pos(en_lista)  
    

          
    #Fin del ciclo while

    input("Proceso terminado...\nPulsa una tecla para continuar")
#AQUI VA EL TEXTO QUE INGRESA                   

while True:
    # Muestra el menú de opciones
    menu()
 
    # Usuario ingresa una opcion
    opcion = input("inserta una opcion: ")
    #Para cargar archivo
    if opcion=="1":
        print("CARGAR ARCHIVO")
        OpenFile()

    #Para graficar archivo
    elif opcion=="2":
        
        input("Has pulsado la opción 2...")
    #SALIR
    elif opcion=="3":
        break
    else:
        
        input("Opcion incorrecta...\nPulsa una tecla para continuar")

