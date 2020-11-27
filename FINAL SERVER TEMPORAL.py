#Globales
cola_de_espera = []
impuestoCanasta1 = 13
impuestoCanasta0 = 1
lista__1=[]
lista__2=[]
lista__3=[]
lista__4=[]
lista_gon=[]
lista_fac=[]
lista_tot=[]
abcd = ''
factura = ''
lista_reportes = ''
lista_grande_admi = ''
factura2 = ''
repo = ''



#escribir
def escribir_cliente(string):
    string = string.split('-')
    string = string[:-1]
    lista = []
    i=0
    while(i<=len(string)-1):
        if i == 0:
            lista+=[[string[i]]]
            i+=1
        else:
            lista[0]+=[string[i].split(';')]
            i+=1
    lista_a_mod = leer_marcas()
    i=0
    lis = lista[0]
    n=1
    while(n<=len(lis)-1):
        i=0
        while(i<=len(lista_a_mod)-1):
            if lis[n][2]==lista_a_mod[i][2]:
                res = abs(int(lista_a_mod[i][4])-int(lis[n][5]))
                lista_a_mod[i][4]= str(res)
                i+=1
            else:
                i+=1
        n+=1
    i=0
    f = open("MarcasProductos.txt","w")
    while(i<=len(lista_a_mod)-1):
        f.write(';'.join(lista_a_mod[i])+'\n')
        i+=1
    f.close()
    #########
    f = open("lista_clientes.txt","a")
    i=0
    while(i<=len(lista)-1):
        x = lista[i]
        j=0
        while(j<=len(x)-1):
            if j==0:
                f.write(x[0])
                f.write('-')
            else:
                f.write(';'.join(x[j])+'-')
            j+=1
        f.write('\n')
        i+=1          
    f.close()



#FUNCIONES DE LEER

#LEER ADMINISTRADORES
def leer_administrador():
    f = open("Administradores.txt","r")
    datos = f.read()
    f.close()
    lista = datos.split("\n")
    return leer_administrador_aux(lista)

def leer_administrador_aux(lista):
    i=0
    listaNueva = []
    while(i<=len(lista)-1):
        listaNueva += [lista[i].split(";")]
        i+=1
    while(listaNueva[-1]==[""]):
        listaNueva=listaNueva[:-1]
    listaNueva=Buscador_inicial_1(listaNueva)
    return listaNueva
    

#LEER CLIENTES
def leer_clientes():
    f = open("Clientes.txt","r")
    datos = f.read()
    f.close()
    lista = datos.split("\n")
    return read_clientes_aux(lista)
def read_clientes_aux(lista):
    i=0
    listaNueva=[]
    while(i<=len(lista)-1):
        listaNueva += [lista[i].split(";")]
        i+=1
    while(listaNueva[-1]==[""]):
        listaNueva=listaNueva[:-1]
    listaNueva=Buscador_inicial_1(listaNueva)
    return listaNueva


# TXT PRODUCTOS PASILLOS
def leer_productos():
    f = open("ProductosPasillos.txt","r")
    datos = f.read()
    f.close()
    lista = datos.split("\n")
    return read_prod_aux(lista)
def read_prod_aux(lista):
    i = 0
    listaNueva = []
    largo = len(lista)-1
    while(i<=largo):
        listaNueva += [lista[i].split(";")]
        i+=1
    while(listaNueva[-1]==[""]):
        listaNueva=listaNueva[:-1]
    listaNueva=Buscador_inicial_2(listaNueva)
    return listaNueva 


#TXT INVENTARIO
def leer_inventario():
    f = open("Inventario.txt","r")
    datos = f.read()
    f.close()
    lista = datos.split("\n")
    return leer_inventario_aux(lista)
def leer_inventario_aux(lista):
    i = 0
    listaNueva = []
    largo = len(lista)-1
    while(i<=largo):
        listaNueva += [lista[i].split(";")]
        i+=1
    while(listaNueva[-1]==[""]):
        listaNueva=listaNueva[:-1]
    listaNueva=Buscador_inicial_3(listaNueva)
    return listaNueva 


#TXT PASILLOS
def leer_pasillos():
    f = open("Productos.txt","r")
    datos = f.read()
    f.close()
    lista = datos.split("\n")
    return read_pasillos_aux(lista)
def read_pasillos_aux(lista):
    i=0
    listaNueva=[]
    while(i<=len(lista)-1):
        listaNueva += [lista[i].split(";")]
        i+=1
    while(listaNueva[-1]==[""]):
        listaNueva=listaNueva[:-1]
    listaNueva=Buscador_inicial_1(listaNueva)
    return listaNueva


#TXT MARCAS
def leer_marcas():
    f = open("MarcasProductos.txt","r")
    datos = f.read()
    f.close()
    lista = datos.split("\n")
    return leer_marcas_aux(lista)
def leer_marcas_aux(lista):
    i=0
    listaNueva=[]
    while(i<=len(lista)-1):
        listaNueva += [lista[i].split(";")]
        i+=1
    while(listaNueva[-1]==[""]):
        listaNueva=listaNueva[:-1]
    listaNueva=Buscador_inicial_3(listaNueva)
    return listaNueva

#TXT CIUDADES
def leer_ciudades():
    f = open("Ciudades.txt","r")
    datos = f.read()
    f.close()
    lista = datos.split("\n")
    return read_ciudades_aux(lista)


def read_ciudades_aux(lista):
    i=0
    listaNueva=[]
    while(i<=len(lista)-1):
        listaNueva += [lista[i].split(";")]
        i+=1
    while(listaNueva[-1]==[""]):
        listaNueva=listaNueva[:-1]
    return listaNueva

#FUNCION QUE CREA UN TXT Y GUARDA EL CLIENTE ACTUAL Q COMPRA
def leer_lista_clientes():
    try:
        f = open("lista_clientes.txt","r")
        datos = f.read()
        f.close()
        lista = datos.split("\n")
        largo = len(lista)-1
        return leer_lista_clientes_aux(lista, largo, 0,[],datos)
    except FileNotFoundError:
        return []

def leer_lista_clientes_aux(lista, largo, i,listaNueva,datos):
    lista_new = []
    lista_ulti=[]
    while(i<=largo):
        listaNueva += [lista[i].split("-")]
        i+=1
    i=0
    while(i<=len(listaNueva)-1):
        j=0
        while(j<=len(listaNueva[i])-1):
            if j!=0:
                lista_ulti += [listaNueva[i][j].split(";")]
                j+=1
            else:
                lista_ulti += [listaNueva[i][j]]
                j+=1
        if (lista_ulti[-1]==[""] or lista_ulti[-1]==''):
            lista_ulti=lista_ulti[:-1]
        lista_new+=[lista_ulti]
        lista_ulti = []
        i+=1
    if lista_new == [[]] or lista_new==[]:
        return []
    while((lista_new[-1]==[]or lista_new[-1]=='')):
        lista_new=lista_new[:-1]
    lista_new = Buscador_inicial_1(lista_new)
    return lista_new

#!!!!!!!AUXILIARES BUSCADORES!!!!!!!
def copia_M(matriz):
    i=0
    lista_new=[]
    while(i<=len(matriz)-1):
        lista_new+=[matriz[i]]
        i+=1
    return lista_new

def inversa(matriz):
    i=0
    lista_new=[]
    i=(len(matriz)-1)
    while(i!=-1):
        lista_new+=[matriz[i]]
        i-=1
    return lista_new

#BUSCADOR (*,ALGO)
def Buscador_inicial_1(matriz):
    ma = inversa(matriz)
    bandera = 0
    lista=[]
    i = 0
    p = 1
    while(i<len(matriz)):
        p = i + 1
        while(p<len(matriz)):
            if ma[i][0]==ma[p][0]:
                bandera=1
                p+=1
            else:
                p+=1
        if bandera==0:
            lista=[ma[i]]+lista
        i+=1
        bandera=0
    return lista



#BUSCADOR (ALGO,*,ALGO)
def Buscador_inicial_2(matriz):
    ma = inversa(matriz)
    bandera = 0
    lista=[]
    i = 0
    p = 1
    while(i<len(matriz)):
        p = i + 1
        while(p<len(matriz)):
            if ma[i][1]==ma[p][1]:
                bandera=1
                p+=1
            else:
                p+=1
        if bandera==0:
            lista=[ma[i]]+lista
        i+=1
        bandera=0
    return lista



#BUSCADOR (ALGO,ALGO,*,ALGO)
def Buscador_inicial_3(matriz):
    ma = inversa(matriz)
    bandera = 0
    lista=[]
    i = 0
    p = 1
    while(i<len(matriz)):
        p = i + 1
        while(p<len(matriz)):
            if ma[i][2]==ma[p][2]:
                bandera=1
                p+=1
            else:
                p+=1
        if bandera==0:
            lista=[ma[i]]+lista
        i+=1
        bandera=0
    return lista

####################################################
###################USUARIO##########################
####################################################

def parsear_Ciudades():
    lista = leer_ciudades()
    for i in range(0,len(lista)):
        lista[i]=';'.join(lista[i])
    lista='-'.join(lista)
    return lista

def parsear_Clientes():
    lista = leer_clientes()
    for i in range(0,len(lista)):
        lista[i]=';'.join(lista[i])
    lista='-'.join(lista)
    return lista


def parsear_Inventario():
    lista = leer_inventario()
    for i in range(0,len(lista)):
        lista[i]=';'.join(lista[i])
    lista='-'.join(lista)
    return lista

def parsear_MarcasProductos():
    lista = leer_marcas()
    for i in range(0,len(lista)):
        lista[i]=';'.join(lista[i])
    lista='-'.join(lista)
    return lista

def parsear_Pasillos():
    lista = leer_pasillos()
    for i in range(0,len(lista)):
        lista[i]=';'.join(lista[i])
    lista='-'.join(lista)
    return lista

def parsear_ProductosPasillos():
    lista = leer_productos()
    for i in range(0,len(lista)):
        lista[i]=';'.join(lista[i])
    lista='-'.join(lista)
    return lista

def parsear_administrador():
    lista = leer_administrador()
    for i in range(0,len(lista)):
        lista[i]=';'.join(lista[i])
    lista = '-'.join(lista)
    return lista
            
def parsear_todo():
    lista1 = parsear_Ciudades()+'+'
    lista2 = parsear_Clientes()+'+'
    lista3 = parsear_Inventario()+'+'
    lista4 = parsear_MarcasProductos()+'+'
    lista5 = parsear_Pasillos()+'+'
    lista6 = parsear_ProductosPasillos()+'+'
    lista7 = parsear_administrador()
    listafinal = lista1+lista2+lista3+lista4+lista5+lista6+lista7
    return listafinal


def man(listaC):
    if listaC==[]:
        return 'p'
    else:
        mandar = ''
        mandar2 = ''
        #listaC = leer_lista_clientes()
        i=0
        while(i<=len(listaC)-1):
            j=0
            mandar2 = ''
            for j in range(0,len(listaC[i])-1):
                mandar2+='-'+";".join(listaC[i][1:][j])
            mandar += listaC[i][0] +  mandar2 + '+'
            i+=1
        return mandar

def nam(string):
    if len(string)==0:
        return []
    else:
        lista = []
        lista2 = []
        i = 0
        string = string.split('+')
        for i in range(0,len(string)):
            string[i] = string[i].split('-')
        while(string[-1]==['']):
            string = string[:-1]
        i=0
        #y[0][1:][0]
        while(i<=len(string)-1):
            j = 0
            lista = []
            for j in range(0,len(string[i])-1):
                lista += [string[i][1:][j].split(";")]
            lista2 += [[string[i][0]] + lista]
            i+=1
        return lista2


#reportes y factura

def convertir(string):
    string = string.split('+')
    lista = []
    for i in range(0,len(string)):
        lista+=[string[i].split(";")]
    while(lista[-1]==['']):
        lista = lista[:-1]
    return lista
        
def generar_factura_aux():
    global lista__1
    global lista__2
    global lista__3
    global lista__4
    global impuestoCanasta1
    global impuestoCanasta0
    global lista_reportes
    global factura2
    listaNueva = []
    lista = leer_clientes()
    largo = len(lista)-1
    listaNueva = lista
    inventario = leer_inventario()
    if len(lista_reportes)==0:
        lista_ordenada = []
    else:
        print("La lista de reportes es:",lista_reportes)
        lista_ordenada = lista_reportes.split("*")
        lista__1+=lista_ordenada[1].split(";")
        lista__2+=convertir(lista_ordenada[2])
        lista__3+=convertir(lista_ordenada[3])
        lista__4+=convertir(lista_ordenada[4])
        lista_ordenada = nam(lista_ordenada[0])
    i=0
    while(i<=len(listaNueva)-1):
        if lista_ordenada[0][0]==listaNueva[i][0]:
            total=0
            global lista_fac
            lista_fac+=[lista_ordenada[0][0]]
            texto = ".txt"
            f = open(lista_ordenada[0][0]+texto,"a")
            f.write("*********************************************")
            factura2+="*********************************************"
            f.write("\n")
            factura2+="\n"
            f.write("-----------SUPER MERCADO SANCHEZE------------")
            factura2+="-----------SUPER MERCADO SANCHEZE------------"
            f.write("\n")
            factura2+="\n"
            f.write("Nombre:")
            factura2 += "Nombre:"
            f.write(listaNueva[i][1])
            factura2+=listaNueva[i][1]
            f.write("||")
            factura2 += "||"
            f.write("Número de cédula:")
            factura2 += "Número de cédula:"
            f.write(listaNueva[i][0])
            factura2+=listaNueva[i][0]
            f.write("||")
            factura2 += "||"
            f.write("\n")
            factura2 += "\n"
            lista_ordenada = lista_ordenada[0]
            for n in range(1,len(lista_ordenada)):
                p = 0
                while(p<=len(inventario)-1):
                    lista1 = lista_ordenada[n][0]+lista_ordenada[n][1]+lista_ordenada[n][2]
                    lista2 = inventario[p][0]+inventario[p][1]+inventario[p][2]
                    if lista1==lista2:
                        f.write("PRODUCTO:"+lista_ordenada[n][3]+"||")
                        factura2 += "PRODUCTO:"+lista_ordenada[n][3]+"||"
                        f.write("MARCA:"+lista_ordenada[n][4]+"||")
                        factura2 += "MARCA:"+lista_ordenada[n][4]+"||"
                        f.write("CANTIDAD:"+lista_ordenada[n][5]+"||")
                        factura2 += "CANTIDAD:"+lista_ordenada[n][5]+"||"
                        f.write("PRECIO:"+"¢"+lista_ordenada[n][6]+"||")
                        factura2 += "PRECIO:"+"¢"+lista_ordenada[n][6]+"||"
                        f.write("CÓDIGO CANASTA BÁSICA:"+inventario[p][5]+"||")
                        factura2 += "CÓDIGO CANASTA BÁSICA:"+inventario[p][5]+"||"
                        f.write("\n")
                        factura2 += "\n"
                        if int(inventario[p][5])==0:
                            f.write("\n")
                            factura2+="\n"
                            f.write("IMPUESTO DE"+"||"+ str(impuestoCanasta0)+"%" +"||"+ "POR UNIDAD")
                            factura2+= "IMPUESTO DE"+"||"+ str(impuestoCanasta0)+"%" +"||"+ "POR UNIDAD"
                            f.write("\n")
                            factura2+="\n"
                            res1=int(lista_ordenada[n][6])*int(lista_ordenada[n][5])
                            res = int(impuestoCanasta0)/100
                            res1+=int(lista_ordenada[n][6])*res*int(lista_ordenada[n][5])
                            total+=res1
                            f.write("TOTAL A PAGAR:"+str(res1))
                            factura2+="TOTAL A PAGAR:"+str(res1)
                            f.write("\n")
                            factura2+="\n"
                            f.write("---------------------------------------------")
                            factura2+="---------------------------------------------"
                            f.write("\n")
                            factura2+="\n"
                            p+=1
                        else:
                            f.write("\n")
                            factura2+="\n"
                            f.write("IMPUESTO DE"+"||"+ str(impuestoCanasta1)+"%" +"||"+"POR UNIDAD")
                            factura2+= "IMPUESTO DE"+"||"+ str(impuestoCanasta1)+"%" +"||"+"POR UNIDAD"
                            f.write("\n")
                            factura2+="\n"
                            res1=int(lista_ordenada[n][6])*int(lista_ordenada[n][5])
                            res = int(impuestoCanasta1)/100
                            res1+=int(lista_ordenada[n][6])*res*int(lista_ordenada[n][5])
                            total+=res1
                            f.write("TOTAL A PAGAR:"+str(res1))
                            factura2 += "TOTAL A PAGAR:"+str(res1)
                            f.write("\n")
                            factura2+="\n"
                            f.write("---------------------------------------------")
                            factura2+="---------------------------------------------"
                            f.write("\n")
                            factura2+="\n"
                            p+=1
                    else:
                        p+=1
            global lista_tot
            lista_tot+=[str(int(total))]
            f.write("\n")
            factura2 += "\n"
            f.write("TOTAL DE LA FACTURA: ")
            factura2 += "TOTAL DE LA FACTURA: "
            f.write(str(total))
            factura2 += str(total)
            f.write("\n")
            factura2 += "\n"
            f.write("*********************************************")
            factura2+="*********************************************"
            f.write("\n")
            factura2+="\n"
            f.close()
            i+=1
        else:
            i+=1
    global factura
    f = open(lista_ordenada[0]+texto,"r")
    datos = f.read()
    factura = datos+"#"+str(impuestoCanasta1)+"#"+str(impuestoCanasta0)
    f.close()
    print("\n")
    print("Su factura se ha realizado con exito")
    print("revise la carpeta de archivos")
    print("\n")
    return True


# Generar  Reporte administrador

def generar_reporte():
    global lista__1
    global lista__2
    global lista__3
    global lista__4
    global repo
    print("\n")
    print("Algunos reportes se generaron según las ventas")
    print("Ejemplo: pasillos más visitados| se colocarón SOLAMENTE los pasillos visitados por los cliente")
    print("\n")
    PasilloMASVisitado = ver_repetido(lista__1)
    PasilloMENOSVisitado = ver_repetido2(lista__1)
    print("\n")
    print("Se realizaran preguntas :")
    print("***PRODUCTOS POR PASILLO MÁS VENDIDOS***")
    num=int(input("ingrese un pasillo---->"))
    prod_pasillo_mas_vendidos = pasillo_mas_producto(lista__2,num)
    print("\n")#aqui
    lista_marca_mas = marca_mas_vendida(lista__3)
    lista_mayorcliente = mayor_pagado(lista__4)
    lista_menorcliente = menor_pagado(lista__4)
    gondolas = ver_repetido(lista_gon)
    mas_fact=ver_repetido(lista_fac)
    imprime_marcas= repor_6()
    #total = mayor_total(lista_tot)
    total = factura_mas_alta(lista__4)
    pro_pasi=repor_4()
    f = open("REPORTES.txt","w")
    f.write("*********************************************")
    repo += "*********************************************"
    f.write("\n")
    repo += "\n"
    f.write("-----------SUPER MERCADO SANCHEZE------------")
    repo += "-----------SUPER MERCADO SANCHEZE------------"
    f.write("\n")
    repo += "\n"
    f.write("-------------------REPORTE--------------------")
    repo += "-------------------REPORTE--------------------"
    f.write("\n")
    repo += "\n"
    f.write("\n")
    repo += "\n"
    f.write("Pasillo más visitado: Es el ")
    repo += "Pasillo más visitado: Es el "
    f.write(PasilloMASVisitado)
    repo += PasilloMASVisitado
    f.write("\n")
    repo += "\n"
    f.write("\n")
    repo += "\n"
    f.write("Pasillo menos visitado: Es el ")
    repo += "Pasillo menos visitado: Es el "
    f.write(PasilloMENOSVisitado)
    repo += PasilloMENOSVisitado
    f.write("\n")
    repo += "\n"
    f.write("\n")
    repo += "\n"
    f.write("Producto del pasillo ")
    repo += "Producto del pasillo "
    f.write(str(num))
    repo += str(num)
    f.write(" más vendido: Es el ")
    repo+=" más vendido: Es el "
    f.write(prod_pasillo_mas_vendidos)
    repo+=prod_pasillo_mas_vendidos
    f.write("\n")
    repo += "\n"
    f.write("\n")
    repo+="\n"
    f.write("Marca más vendida: Es la ")
    repo+="Marca más vendida: Es la "
    f.write(lista_marca_mas)
    repo+=lista_marca_mas
    f.write("\n")
    repo+="\n"
    f.write("\n")
    repo+="\n"
    f.write("Cliente que más compro: ")
    repo+="Cliente que más compro: "
    f.write("CEDULA: ")
    repo+="CEDULA: "
    f.write(lista_mayorcliente)
    repo+=lista_mayorcliente
    f.write("\n")
    repo+="\n"
    f.write("\n")
    repo+="\n"
    f.write("Cliente que menos compro")
    repo+="Cliente que menos compro"
    f.write("CEDULA: ")
    repo+="CEDULA: "
    f.write(lista_menorcliente)
    repo+=lista_menorcliente
    f.write("\n")
    repo+="\n"
    f.write("\n")
    repo+="\n"
    f.write("Producto que se gasto más: ")
    repo+="Producto que se gasto más: "
    f.write(gondolas)
    repo+=gondolas
    f.write("\n")
    repo+="\n"
    f.write("\n")
    repo+="\n"
    f.write("max num de facturas las realizo el de cedula: ")
    repo+="max num de facturas las realizo el de cedula: "
    f.write(mas_fact)
    repo+=mas_fact
    f.write("\n")
    repo+="\n"
    f.write("\n")
    repo+="\n"
    f.write("Marcas de un producto: ")
    repo+="Marcas de un producto: "
    f.write(imprime_marcas)
    repo+=imprime_marcas
    f.write("\n")
    repo+="\n"
    f.write("\n")
    repo+="\n"
    f.write("Factura de mayor monto: ")
    repo+="Factura de mayor monto: "
    f.write(total)
    repo+=total
    f.write("\n")
    repo+="\n"
    f.write("\n")
    repo+="\n"
    f.write("Productos de un pasillo:")
    repo+="Productos de un pasillo:"
    f.write(pro_pasi)
    repo+=pro_pasi
    f.write("\n")
    repo+="\n"
    f.write("\n")
    repo+="\n"
    f.write("Lista de clientes Supermercado:")
    repo+="Lista de clientes Supermercado:"
    f.write(str(leer_clientes()))
    repo+=str(leer_clientes())
    f.write("\n")
    repo+="\n"
    f.write("\n")
    repo+="\n"
    f.write("Pasillos Supermercado:")
    repo+="Pasillos Supermercado:"
    f.write(str(leer_pasillos()))
    repo+=str(leer_pasillos())
    f.write("\n")
    repo+="\n"
    f.write("\n")
    repo+="\n"
    f.write("TODO LO DEL SUPERMERCADO SANCHEZE:")
    repo+="TODO LO DEL SUPERMERCADO SANCHEZE:"
    f.write(str(leer_inventario()))
    repo+=str(leer_inventario())
    f.write("\n")
    repo+="\n"
    f.write("\n")
    repo+="\n"
    f.write("*********************************************")
    repo+="*********************************************"
    f.close()
    return True

def marca_mas_vendida(lista):
    lista_frecuencias = []
    if lista == []:
        return "No se encontro."
    else:
        for i in range (0,len(lista)):
            lista_frecuencias += [int(lista[i][2])]
        maximo = max(lista_frecuencias)
        bandera = False
        for i in range(0,len(lista)):
            if int(lista[i][2]) == maximo:
                producto = lista[i]
                bandera = True
                break
        if bandera == True:
            suma = 0
            for i in range(0,len(lista)):
                if lista[i][1] == producto[1]:
                    suma += int(lista[i][2])
            return producto[1]
        else:
            return "No se encontro."

def repor_4():
    print("\n")
    print("número de ese pasillo, se imprimen todos los productos del pasillo")
    op1=int(input("ingrese un pasillo---->"))
    productos = leer_productos()
    i=0
    var=''
    while(i<=len(productos)-1):
        if int(productos[i][0])==op1:
            var += productos[i][2]
            var+=";"
        i+=1
    if len(var)==0:
        var = "No hay marcas"
        return var
    else:
        return var
   
   
def repor_6():
    print("\n")
    print("•Marcas de un producto: Indica el pasillo, indica el producto pasillo, imprime todas las marcas de un producto")
    op1=int(input("ingrese un pasillo---->"))
    op2=int(input("ingrese codigo producto pasillo---->"))
    marcas = leer_marcas()
    i=0
    var=''
    while(i<=len(marcas)-1):
        if int(marcas[i][0])==op1:
            if int(marcas[i][1])==op2:
                var += marcas[i][3]
                var+=";"
        i+=1
    if len(var)==0:
        var = "No hay marcas"
        return var
    else:
        return var
        
        
        
    


def mayor_total(lista):
    i=0
    var=''
    if lista==[]:
        var="(NO SE ENCONTRARON)"
        return var
    else:
        for i in range(0,len(lista)):
            for j in range(0,len(lista)):
                if int(lista[i])>int(lista[j]):
                    var=str(lista[i][0]) 
        return var




def mayor_pagado(lista):
    i=0
    var=''
    if lista==[]:
        var="(NO SE ENCONTRARON)"
        return var
    else:
        for i in range(0,len(lista)):
            for j in range(0,len(lista)):
                if int(lista[i][1])>int(lista[j][1]):
                    var=lista[i][0]
        return var


def menor_pagado(lista):
    i=0
    var=''
    if lista==[]:
        var="(NO SE ENCONTRARON)"
        return var
    else:
        for i in range(0,len(lista)):
            for j in range(0,len(lista)):
                if int(lista[i][1])<int(lista[j][1]):
                    var=lista[i][0]
        return var


def pasillo_mas_producto(lista,num):
    lista_new=[]
    i=0
    if lista==[]:
        x =''
        x += "No se encontro"
        return x
    else:
        for i in range(0,len(lista)):
            if int(lista[i][0])==num:
                lista_new+=[lista[i][1:]]
        return pasillo_mas_producto_aux(lista_new)

def pasillo_mas_producto_aux(lista):
    i=0
    res=1
    cont=0
    var=''
    if lista==[]:
        var="(NO SE ENCONTRARON)"
        return var
    else:
        for i in range(0,len(lista)):
            j=0
            cont=0
            for j in range(0,len(lista)):
                if lista[i][0]==lista[j][0]:
                    cont+=1
                    j+=1
                else:
                    j+=1
            if cont+1>res:
                var=lista[i][1]
                res=1
                res+=cont
        return var
                

def ver_repetido(lista):
    i=0
    res=1
    cont=0
    var=''
    if lista==[]:
        var="(NO SE ENCONTRARON)"
        return var
    else:
        for i in range(0,len(lista)):
            j=0
            cont=0
            for j in range(0,len(lista)):
                if lista[i]==lista[j]:
                    cont+=1
                    j+=1
                else:
                    j+=1
            if cont+1>res:
                var=lista[i]
                res=1
                res+=cont
        return var

    
#revisar aqui
def ver_repetido2(lista):
    i=0
    res=len(lista)
    cont=0
    var=''
    if lista==[]:
        var="(NO SE ENCONTRARON)"
        return var
    else:
        for i in range(0,len(lista)):
            j=0
            cont=0
            for j in range(0,len(lista)):
                if lista[i]==lista[j]:
                    cont+=1
                    j+=1
                else:
                    j+=1
            if cont<=res:
                if len(lista[0])>1:
                    var=lista[i]
                    res=0
                    res+=cont
                else:
                    var=lista[i]
                    res=0
                    res+=cont
        return var

def factura_mas_alta(lista):
    x=''
    lista_frecuencias = []
    if lista == []:
        return "No se han facturado compras."
    else:
        for i in range(0,len(lista)):
            lista_frecuencias += [int(lista[i][1])]
        maximo = max(lista_frecuencias)
        bandera = False
        for i in range(0,len(lista)):
            if int(lista[i][1]) == maximo:
                producto = lista[i]
                bandera = True
                break
        if bandera == True:
            x = "La factura de mayor monto es la del cliente " + producto[0] + " con un valor de: "+producto[1]
            #producto[1]
            return x
        else:
            return "No se han facturado compras."

def desparsear(string):
    string = string.split('-')
    for i in range(0,len(string)):
        string[i] = string[i].split(';')
    return string

def poner_cliente(lista):
    i=0
    f = open("Clientes.txt","w")
    while(i<=len(lista)-1):
        f.write(';'.join(lista[i])+'\n')
        i+=1
    f.close()
    return True
    
def escribir_ciudades(lista):
    i=0
    f = open("Ciudades.txt","w")
    while(i<=len(lista)-1):
        f.write(';'.join(lista[i])+'\n')
        i+=1
    f.close()
    return True
    
def escribir_marcas(lista):
    i=0
    f = open("MarcasProductos.txt","w")
    while(i<=len(lista)-1):
        f.write(';'.join(lista[i])+'\n')
        i+=1
    f.close()
    return True
    
def escribir_productos(lista):
    i=0
    f = open("ProductosPasillos.txt","w")
    while(i<=len(lista)-1):
        f.write(';'.join(lista[i])+'\n')
        i+=1
    f.close()
    return True
    
def escribir_pasillos(lista):
    i=0
    f = open("Productos.txt","w")
    while(i<=len(lista)-1):
        f.write(';'.join(lista[i])+'\n')
        i+=1
    f.close()
    return True
    
def escribir_inventario(lista):
    i=0
    f = open("Inventario.txt","w")
    while(i<=len(lista)-1):
        f.write(';'.join(lista[i])+'\n')
        i+=1
    f.close()
    return True
    
def recibir(data):
    print(data)
    string = data.split('+')
    lista_ciudades = []
    lista_clientes = []
    lista_inventario = []
    lista_marcas = []
    lista_pasillos = []
    lista_productos = []
    lista_ciudades = desparsear(string[0])
    lista_clientes = desparsear(string[1])
    lista_inventario = desparsear(string[2])
    lista_marcas = desparsear(string[3])
    lista_pasillos = desparsear(string[4])
    lista_productos = desparsear(string[5])
    if (poner_cliente(lista_clientes)==True and  escribir_ciudades(lista_ciudades)==True and  escribir_marcas(lista_marcas)==True and escribir_productos(lista_productos)==True and escribir_pasillos(lista_pasillos)==True and escribir_inventario(lista_inventario)==True):
        return True
    
    

###############
   

import socket
import threading

def server():
    HOST = ''  # Standard loopback interface address (localhost)
    PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
    server_socket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(20)
    global abcd
    global factura
    global lista_reportes
    global lista_grande_admi
    while True:
        conn,address = server_socket.accept()
        data = conn.recv(10000000000)
        if data.decode()=='abrir_menu':
            if abcd == 'parado':
                conn.sendall('parado'.encode())
            else:
                conn.sendall(parsear_todo().encode())
        elif data.decode()=='cola':
            mandar = man(leer_lista_clientes())
            f= open("lista_clientes.txt","w")
            f.close()
            conn.sendall(mandar.encode())
        elif data.decode()[0:2]=='00':
            x=data.decode()[2:]
            x = escribir_cliente(x)
            data = '01'
            if abcd == 'parado':
                conn.sendall('parado'.encode())
            else:
                conn.sendall(data.encode())
        elif data.decode()=='01':
            data='02'
            if abcd == 'parado':
                conn.sendall('parado'.encode())
            else:
                conn.sendall(parsear_todo().encode())
        elif data.decode()=='verificando':
            if abcd == 'parado':
                conn.sendall('parado'.encode())
            else:
                conn.sendall(parsear_todo().encode())
        elif data.decode()=='hilo':
            abcd = 'parado'
            #conn.sendall('parado'.encode())
        elif data.decode()=='nohilo':
            abcd = ''
            #conn.sendall('nada'.encode())
        elif data.decode()=='factura':
            if factura=='':
                conn.sendall("no".encode())
            else:
                conn.sendall(factura.encode())
                factura = ''
        elif data.decode()[0:2]=='87':
            m = data.decode()[2:]####aqui esta fallando
            if m!='9':
                lista_reportes = m
            else:
                if generar_factura_aux() == True:
                    global factura2
                    conn.sendall(factura2.encode())
                else:
                    conn.sendall('NO FACTURADA'.encode())

        elif data.decode()=='genere':
            if generar_reporte()==True:
                global repo
                conn.sendall(repo.encode())
            else:
                conn.sendall('NO HAY REPORTE'.encode())
        elif data.decode()[0]=='!':
            lista_grande_admi = data.decode()[1:]
            if recibir(lista_grande_admi)==True:
                conn.sendall('yeah'.encode())
                
    conn.close()
    

server()
hiloAceptador = threading.Thread(target=server)
hiloAceptador.start()
#inicio()
