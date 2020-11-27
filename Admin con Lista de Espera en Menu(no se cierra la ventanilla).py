#Globales
from tkinter import *
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
lista_ordenada = []
#######
#new###
leer_ciudades = []
leer_administrador = []
leer_inventario = []
leer_marcas = []
leer_pasillos = []
leer_productos = []
leer_clientes  = []
ordenada = ''
string1 = ''
string2 = ''
string3 = ''
string4 = ''
reportes_conexion = ''
####################
cola_de_espera = []
cola_de_pagar = []
todo = ''
todo1 = ''
cedula_vieja = ''
actualizador = 0
repo = ''




#AQUI INICIA EL PROGRAMA
def inicio():
    global cola_de_pagar
    global cola_de_espera
    if Administrador('1')==True:
        return menu_digital()

##def menu(cola_de_espera,cola_de_pagar):
##    global reportes_conexion
##    global abcd
##    abcd = ''
##    if Administrador('2')==False and Administrador('1')==True:
##        print("-"*12,"MENÚ","-"*12)
##        print("*"*60)
##        print("1.  Insertar Pasillo                                       *")
##        print("2.  Insertar Producto Pasillo                              *")
##        print("3.  Insertar Marca                                         *")
##        print("4.  Insertar Cliente                                       *")
##        print("5.  Modificar el precio                                    *")
##        print("6.  Modificar el % de impuesto                             *")
##        print("7.  Modificar si el producto pertenece a la canasta básica *")
##        print("8.  Consultar un Precio                                    *")
##        print("9.  Consultar Si un Producto es de la canasta              *")
##        print("10. Consultar el % impuesto de un producto(monitor)        *")
##        print("11. Consultar el precio de un producto (monitor)           *")
##        print("12. Facturar                                               *")
##        print("13. Revisar Góndolas                                       *")
##        print("14. Verificar Inventario                                   *")
##        print("15. Reportes administrativos                               *")
##        print("16. EXIT                                                   *")
##        print("*"*60)
##        print("La lista de clientes en cola:",str(cola_de_pagar))
##        opcion = input("   Digite la opcion y presione ENTER -->")
##        if opcion == "1" :
##            abcd = 'parado'
##            if Administrador('2')==True:
##                return insertar_pasillo(cola_de_espera,cola_de_pagar)
##        elif opcion == "2":
##            abcd = 'parado'
##            if Administrador('2')==True:
##                return insertar_Producto_Pasillo(cola_de_espera,cola_de_pagar)
##        elif opcion == "3" :
##            abcd = 'parado'
##            if Administrador('2')==True:
##                return insertar_Marca(cola_de_espera,cola_de_pagar)
##        elif opcion == "4" :
##            abcd = 'parado'
##            if Administrador('2')==True:
##                return insertar_cliente(cola_de_espera,cola_de_pagar)
##        elif opcion == "5" :
##            abcd = 'parado'
##            if Administrador('2')==True:
##                return modificarPrecio (cola_de_espera,cola_de_pagar)
##        elif opcion == "6":
##            abcd = 'parado'
##            if Administrador('2')==True:
##                return modificarPorcentaje (cola_de_espera,cola_de_pagar)
##        elif opcion == "7" :
##            abcd = 'parado'
##            if Administrador('2')==True:
##                return modificarCanasta (cola_de_espera,cola_de_pagar)
##        elif opcion == "8" :
##            if Administrador('2')==False:
##                return consultarTodosPrecios(cola_de_espera,cola_de_pagar)
##        elif opcion == "9" :
##            if Administrador('2')==False:
##                return consultarCanasta(cola_de_espera,cola_de_pagar)
##        elif opcion == "10":
##            if Administrador('2')==False:
##                return consultarCanasta1(cola_de_espera,cola_de_pagar)
##        elif opcion == "11" :
##            if Administrador('2')==False:
##                return consultarPrecio(cola_de_espera,cola_de_pagar)
##        elif opcion == "12" :
##            if Administrador('1')==True:
##                return cancelar(cola_de_espera,cola_de_pagar)
##        elif opcion == "13" :
##            abcd = 'parado'
##            if Administrador('2')==True:
##                return revisar_gondolas(cola_de_espera,cola_de_pagar)
##        elif opcion == "14" :
##            abcd = 'parado'
##            if Administrador('2')==True:
##                return revisar_inventario(cola_de_espera,cola_de_pagar)
##        elif opcion == "15" :
##            if Administrador('4')==True:
##                print(reportes_conexion)
##                return menu(cola_de_espera,cola_de_pagar)
##            else:
##                return menu(cola_de_espera,cola_de_pagar)
##        elif opcion == "16" :
##            return "fin"
##        elif opcion == "":
##            return menu(cola_de_espera,cola_de_pagar)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
def buscarMarca(codigo):
    listaNueva = leer_marcas
    for i in range(len(listaNueva)):
        if str(codigo) == listaNueva[i][2]:
            return i

def cambiarAdministrador(ventana):
    menuVentana = ventana
    menuVentana.withdraw()
    cambio = Tk()
    cambio.geometry('1080x720')
    l = Label(cambio, text='Ingrese de nuevo: ')
    l.pack()
    cedulaNueva = Entry(cambio)
    cedulaNueva.pack()
    volver = Button(cambio,text='Iniciar',command = lambda: volverMenuCambio(cambio,cedulaNueva.get()))
    volver.pack()

def volverMenuCambio(ventana,cedula):
    consultar = ventana
    consultar.withdraw()
    cedula1 = cedula
    if Administrador('5')==True:
        return menu_digital(cedula1)

def salir(ventana):
    menuVentana = ventana
    menuVentana.withdraw()
    salir = Tk()
    salir.geometry('1080x720')
    l = Label(salir,text='Gracias por preferirnos!')
    l.pack()

#-------------------------------------------------------------------------------------------------------

def volverMenu(ventana):
    consultar = ventana
    consultar.withdraw()
    if Administrador('5')==True:
        return menu_digital()  


def menu_digital():
    global reportes_conexion
    global abcd
    abcd = ''
    if Administrador('2')==False and Administrador('1')==True and Administrador('0')==True:#reefr
        menuVentana = Tk()
        menuVentana.configure(bg="white")
        menuVentana.geometry("1280x720")
        if cola_de_pagar == []:
            l = Label(menuVentana,text='No hay clientes en la fila. ').place(x=10,y=100)
        else:
            def myfunction(event):
                canvas.configure(scrollregion=canvas.bbox("all"),width=200,height=200)

            myframe=Frame(menuVentana,relief=GROOVE,width=100,height=500,bd=1)
            myframe.place(x=10,y=10)

            canvas=Canvas(myframe)
            frame=Frame(canvas)
            myscrollbar=Scrollbar(myframe,orient="vertical",command=canvas.yview)
            canvas.configure(yscrollcommand=myscrollbar.set)

            myscrollbar.pack(side="right",fill="y")
            canvas.pack(side="right")
            canvas.create_window((0,0),window=frame,anchor='nw')
            frame.bind("<Configure>",myfunction)

            
            #h = Label(ventanaExtra,text='La lista de espera es: ')
            #h.pack()
            cont = 1
            for i in  range(len(cola_de_pagar)):
                Label(frame,text=('La lista de espera es : ')).grid(row=i,column=0)
                Label(frame,text=(cola_de_pagar[i][0])).grid(row=i,column=1)
                #l = Label(ventanaExtra,text=(str(cont) + '. ' + cola_de_pagar[i][0]))
                #l.pack()
                cont += 1
        menuLista = ['1.     Insertar Pasillo','2.     Insertar ProductoPasillo','3.     Insertar Marca','4.     Insertar Cliente','5.     Modificar el Precio','6.     Modificar el % de impuesto','7.     Modificar si el producto pertenece a la canasta basica','8.     Eliminar Productos','9.     Eliminar Pasillos','10.     Eliminar Marca','11.     Eliminar Cliente','12.     Consultar un precio','13.     Consultar si un producto es de la canasta basica','14.     Consultar el % de un producto','15.     Consultar el precio de un producto','16.     Facturar','17.     Revisar Gondolas','18.     Verificar el Inventario','19.     Reportes Administrativos','20.     Salir']
        boton1 = Button(menuVentana,text=menuLista[0],command = lambda: InsertarPasillo(menuVentana))
        boton1.pack()
        boton2 = Button(menuVentana,text=menuLista[1],command = lambda: InsertarProducto(menuVentana))
        boton2.pack()
        boton3 = Button(menuVentana,text=menuLista[2],command = lambda: InsertarMarca(menuVentana))
        boton3.pack()
        boton4 = Button(menuVentana,text=menuLista[3],command = lambda: InsertarCliente(menuVentana))
        boton4.pack()
        boton5 = Button(menuVentana,text=menuLista[4],command = lambda: ModificarPrecio(menuVentana))
        boton5.pack()
        boton6 = Button(menuVentana,text=menuLista[5],command = lambda: ModificarImpuesto(menuVentana))
        boton6.pack()
        boton7 = Button(menuVentana,text=menuLista[6],command = lambda: ModificarProductoCanastaBasica(menuVentana))
        boton7.pack()
        boton8 = Button(menuVentana,text=menuLista[7],command = lambda: EliminarProductos(menuVentana))
        boton8.pack()
        boton9 = Button(menuVentana,text=menuLista[8],command = lambda: EliminarPasillos(menuVentana))
        boton9.pack()
        boton10 = Button(menuVentana,text=menuLista[9],command = lambda: EliminarMarca(menuVentana))
        boton10.pack()
        boton11 = Button(menuVentana,text=menuLista[10],command = lambda: EliminarCliente(menuVentana))
        boton11.pack()
        boton12 = Button(menuVentana,text=menuLista[11],command = lambda: ConsultarPrecio(menuVentana))
        boton12.pack()
        boton13 = Button(menuVentana,text=menuLista[12],command = lambda: ConsultarProductoCanasta(menuVentana))
        boton13.pack()
        boton14 = Button(menuVentana,text=menuLista[13],command = lambda: ConsultarImpuestoProducto(menuVentana))
        boton14.pack()
        boton15 = Button(menuVentana,text=menuLista[14],command = lambda: ConsultarPrecioProducto(menuVentana))
        boton15.pack()
        boton16 = Button(menuVentana,text=menuLista[15],command = lambda: Facturar())
        boton16.pack()
        boton17 = Button(menuVentana,text=menuLista[16],command = lambda: RevisarGondolas(menuVentana))
        boton17.pack()
        boton18 = Button(menuVentana,text=menuLista[17],command = lambda: VerificarInventario(menuVentana))
        boton18.pack()
        boton19 = Button(menuVentana,text=menuLista[18],command = lambda: ReportesAdministrativos(menuVentana))
        boton19.pack()
        boton20 = Button(menuVentana,text=menuLista[19],command = lambda: salir(menuVentana))
        boton20.pack()
        
#1 REVISADA & CORREGIDA
def InsertarPasillo(ventana):
    global abcd
    abcd = 'parado'
    if Administrador('2')==True:
        menuVentana=ventana
        menuVentana.withdraw()
        insertar = Tk()
        insertar.geometry('1080x720')
        if verificarCampoPasillos():
            l = Label(insertar, text='Por favor indique la siguiente informacion: ')
            l.pack()
            b = Label(insertar, text='Nombre del pasillo: ')
            b.pack()
            nombrePasillo = Entry(insertar)
            nombrePasillo.pack()
            c = Label(insertar, text='Codigo del pasillo: ')
            c.pack()
            codPasillo = Entry(insertar)
            codPasillo.pack()
            confirmar = Button(insertar,text='confirmar',command=lambda:InsertarPasillo_aux(insertar,str(nombrePasillo.get()),str(codPasillo.get())))
            confirmar.pack()
            volver = Button(insertar,text='volver al menu',command = lambda: volverMenu(insertar))
            volver.pack()
        else:
            l = Label(insertar, text='No se encuentran pasillos disponibles. Desea eliminar uno?')
            l.pack()
            eliminar = Button(insertar,text='eliminar', command=lambda:EliminarPasillos(insertar))
            eliminar.pack()
            volver = Button(insertar,text='volver al menu',command = lambda: volverMenu(insertar))
            volver.pack()
def InsertarPasillo_aux(ventana,nombre,codigo):
    ventana.withdraw()
    busqueda = Tk()
    busqueda.geometry('1080x720')
    for i in range(len(leer_pasillos)):
        if leer_pasillos[i][0] == '00':
            leer_pasillos[i][0] = codigo
            leer_pasillos[i][1] = nombre
    l = Label(busqueda, text='El pasillo deseado se ha agregado al supermercado.')
    l.pack()
    volver = Button(busqueda,text='volver al menu',command = lambda: volverMenu(busqueda))
    volver.pack()
def verificarCampoPasillos():
    listaPasillos = leer_pasillos
    for i in range (len(listaPasillos)):
        if listaPasillos[i][0] == '00':
            return True
    return False

#2 REVISADA & HECHA DE NUEVO
def InsertarProducto(ventana):
    global abcd
    abcd = 'parado'
    if Administrador('2')==True:
        menuVentana=ventana
        menuVentana.withdraw()
        insertar = Tk()
        insertar.geometry('1080x720')
        l = Label(insertar, text='Por favor ingrese el pasillo al que desea agregar productos: ')
        l.pack()
        b = Label(insertar, text='Nombre del pasillo: ')
        b.pack()
        nombrePasillo = Entry(insertar)
        nombrePasillo.pack()
        c = Label(insertar, text='Codigo del pasillo: ')
        c.pack()
        codPasillo = Entry(insertar)
        codPasillo.pack()
        busqueda = Button(insertar,text='buscar',command=lambda: InsertarProducto_aux(insertar,str(nombrePasillo.get()),str(codPasillo.get())))
        busqueda.pack()
        volver = Button(insertar,text='volver al menu',command = lambda: volverMenu(insertar))
        volver.pack()
def InsertarProducto_aux(ventana,nombre,codigo):
    busqueda = ventana
    busqueda.withdraw()
    busqueda2 = Tk()
    busqueda2.geometry('1080x720')
    if validarInputPasillo(nombre,codigo):
        h = Label (busqueda2, text='Pasillo confirmado.')
        h.pack()
        l = Label (busqueda2, text='Por favor indique la siguiente informacion adicional: ')
        l.pack()
        a = Label(busqueda2, text='Nombre del producto: ')
        a.pack()
        nombreProducto = Entry(busqueda2)
        nombreProducto.pack()
        b = Label(busqueda2, text='Codigo del producto: ')
        b.pack()
        codProducto = Entry(busqueda2)
        codProducto.pack()
        confirmar = Button(busqueda2,text='confirmar',command=lambda: InsertarProducto_aux2(busqueda2,codigo,str(nombreProducto.get()),str(codProducto.get())))
        confirmar.pack()
        volver = Button(busqueda2,text='volver al menu',command = lambda: volverMenu(busqueda2))
        volver.pack()
    else:
        l = Label(busqueda2, text='El pasillo que busca no existe. Desea crearlo?')
        l.pack()
        crear = Button(busqueda2, text='crear',command = lambda: InsertarPasillo(busqueda2))
        crear.pack()
        intentar = Button(busqueda2,text='intentar de nuevo',command = lambda: InsertarProducto(busqueda2))
        intentar.pack()
        volver = Button (busqueda2,text='volver al menu',command = lambda: volverMenu(busqueda2))
        volver.pack()
def InsertarProducto_aux2(ventana,pasillo,nombre,codigo):
    busqueda = ventana
    busqueda.withdraw()
    confirmar = Tk()
    confirmar.geometry('1080x720')
    if siExisteProducto(pasillo,nombre,codigo) == False and nombre != '' and codigo != '':
        leer_productos.append([pasillo,codigo,nombre])
        l = Label(confirmar, text = 'El producto deseado se ha agregado al supermercado.')
        l.pack()
        cont = 1
        for i in range(len(leer_pasillos)):
            if leer_pasillos[i][0] == pasillo:
                h = Label(confirmar, text='Los nuevos productos del pasillo ' + leer_pasillos[i][1].lower()+' son: ')
                h.pack()
                for i in range(len(leer_productos)):
                    if leer_productos[i][0] == pasillo:
                        k = Label(confirmar,text=(str(cont) + '. ' + 'producto: ' + leer_productos[i][2]+" | Codigo: "+leer_productos[i][1]))
                        k.pack()
                        cont+=1
                break
        volver = Button(confirmar,text='volver al menu',command = lambda: volverMenu(confirmar))
        volver.pack()
    else:
        l = Label(confirmar, text='El producto deseado ya existe.')
        l.pack()
        volver = Button(confirmar,text='volver al menu',command = lambda: volverMenu(confirmar))
        volver.pack()
def siExisteProducto(pasillo,nombre,codigo):
    listaProductos = leer_productos
    for i in range(len(listaProductos)):
        if listaProductos[i][0] == pasillo:
            if listaProductos[i][1] == codigo or listaProductos[i][2].upper() == nombre.upper():
                return True
    return False

#3 HECHA DE NUEVO
def InsertarMarca(ventana):
    global abcd 
    abcd = 'parado'
    if Administrador('2')==True:
        menuVentana = ventana
        menuVentana.withdraw()
        insertar = Tk()
        insertar.geometry('1080x720')
        l = Label(insertar, text='Por favor ingrese el pasillo al que desea agregar productos: ')
        l.pack()
        b = Label(insertar, text='Nombre del pasillo: ')
        b.pack()
        nombrePasillo = Entry(insertar)
        nombrePasillo.pack()
        c = Label(insertar, text='Codigo del pasillo: ')
        c.pack()
        codPasillo = Entry(insertar)
        codPasillo.pack()
        busqueda = Button(insertar,text='buscar',command=lambda: InsertarMarca_aux(insertar,str(nombrePasillo.get()),str(codPasillo.get())))
        busqueda.pack()
        volver = Button(insertar,text='volver al menu',command = lambda: volverMenu(insertar))
        volver.pack()
def InsertarMarca_aux(ventana,nombre,codigo):
    eliminar = ventana
    eliminar.withdraw()
    busqueda = Tk()
    busqueda.geometry('1080x720')
    if validarInputPasillo(nombre,codigo):
        h = Label (busqueda, text='Pasillo confirmado.')
        h.pack()
        l = Label (busqueda, text='Por favor indique la siguiente informacion adicional: ')
        l.pack()
        a = Label(busqueda, text='Nombre del producto: ')
        a.pack()
        nombreProducto = Entry(busqueda)
        nombreProducto.pack()
        b = Label(busqueda, text='Codigo del producto: ')
        b.pack()
        codProducto = Entry(busqueda)
        codProducto.pack()
        buscar = Button(busqueda,text='buscar',command=lambda: InsertarMarca_aux1(busqueda,codigo,str(nombreProducto.get()),str(codProducto.get())))
        buscar.pack()
        volver = Button(busqueda,text='volver al menu',command = lambda: volverMenu(busqueda))
        volver.pack()
    else:
        l = Label(busqueda, text='El pasillo que busca no existe. Desea crearlo?')
        l.pack()
        crear = Button(busqueda, text='crear',command = lambda: InsertarPasillo(busqueda))
        crear.pack()
        intentar = Button(busqueda,text='intentar de nuevo',command = lambda:InsertarMarca(busqueda))
        intentar.pack()
        volver = Button(busqueda,text='volver al menu',command = lambda: volverMenu(busqueda))
        volver.pack()
def InsertarMarca_aux1(ventana,pasillo,nombre,codigo):
    busqueda = ventana
    busqueda.withdraw()
    busqueda2 = Tk()
    busqueda2.geometry('1080x720')
    if validarInputProducto(pasillo,nombre,codigo):
        h = Label (busqueda2, text='Producto confirmado.')
        h.pack()
        l = Label (busqueda2, text='Por favor indique la siguiente informacion adicional: ')
        l.pack()
        a = Label(busqueda2, text='Nombre de la marca: ')
        a.pack()
        nombreMarca = Entry(busqueda2)
        nombreMarca.pack()
        b = Label(busqueda2, text='Codigo de la marca: ')
        b.pack()
        codMarca = Entry(busqueda2)
        codMarca.pack()
        buscar = Button(busqueda2,text='buscar',command=lambda: InsertarMarca_aux2(busqueda2,pasillo,codigo,str(nombreMarca.get()),str(codMarca.get())))
        buscar.pack()
        volver = Button(busqueda2,text='volver al menu',command = lambda: volverMenu(busqueda2))
        volver.pack()
    else:
        l = Label(busqueda2, text='El producto que busca no existe. Desea crearlo?')
        l.pack()
        crear = Button(busqueda2, text='crear',command = lambda: InsertarProducto(busqueda2))
        crear.pack()
        intentar = Button(busqueda2, text='intentar de nuevo',command=lambda:InsertarMarca(busqueda2))
        intentar.pack()
        volver = Button(busqueda2,text='volver al menu',command = lambda: volverMenu(busqueda2))
        volver.pack()
def InsertarMarca_aux2(ventana,pasillo,producto,nombre,codigo):
    busqueda2 = ventana
    busqueda2.withdraw()
    busqueda3 = Tk()
    busqueda3.geometry('1080x720')
    if siExisteMarca(pasillo,producto,nombre,codigo) == False and nombre != '' and codigo != '':
        l = Label(busqueda3, text='Exito. Por favor ingrese la informacion restante para terminar el proceso: ')
        l.pack
        a = Label(busqueda3, text='Cantidad en gondolas: ')
        a.pack()
        cantGondolas = Entry(busqueda3)
        cantGondolas.pack()
        b = Label(busqueda3, text='Precio unitario: ')
        b.pack()
        precio = Entry(busqueda3)
        precio.pack()
        c = Label(busqueda3, text='Cantidad en inventario: ')
        c.pack()
        cantInventario = Entry(busqueda3)
        cantInventario.pack()
        d = Label(busqueda3, text='Codigo de canasta basica e impuesto (1 o 0): ')
        d.pack()
        codCanasta = Entry(busqueda3)
        codCanasta.pack()
        confirmar = Button(busqueda3,text='confirmar',command=lambda: InsertarMarca_aux3(busqueda3,pasillo,producto,nombre,codigo,str(cantGondolas.get()),str(precio.get()),str(cantInventario.get()),str(codCanasta.get())))
        confirmar.pack()
        volver = Button(busqueda3,text='volver al menu',command = lambda: volverMenu(busqueda3))
        volver.pack()
    else:
        l = Label(busqueda3, text='La marca deseada ya existe.')
        l.pack()
        volver = Button(busqueda3,text='volver al menu',command = lambda: volverMenu(busqueda3))
        volver.pack()
def InsertarMarca_aux3(ventana,pasillo,producto,nombre,codigo,gondola,precio,inventario,canasta):
    busqueda3 = ventana
    busqueda3.withdraw()
    confirmar = Tk()
    confirmar.geometry('1080x720')
    if (canasta == '0' or canasta == '1') and (codigo != '' and gondola != '' and precio != '' and inventario != '' and canasta != ''):
        leer_marcas.append([pasillo,producto,codigo,nombre,gondola,precio])
        leer_inventario.append([pasillo,producto,codigo,nombre,inventario,canasta])
        l = Label(confirmar, text = 'La marca deseada se ha agregado al supermercado.')
        l.pack()
        cont = 1
        for i in range(len(leer_productos)):
            if leer_productos[i][1] == producto:
                h = Label(confirmar, text='Las nuevas marcas del producto ' + leer_productos[i][2].lower()+' son: ')
                h.pack()
                for i in range(len(leer_marcas)):
                    if leer_marcas[i][0] == pasillo:
                        if leer_marcas[i][1] == producto:
                            k = Label(confirmar,text=(str(cont) + '. ' + 'marca: ' + leer_marcas[i][3]+" | Codigo: "+leer_marcas[i][2])+" | Cant. Gondolas: "+leer_marcas[i][4]+" | precio: "+leer_marcas[i][5]+" | Cant. Inventario: "+leer_inventario[i][4]+" | Codigo: "+leer_inventario[i][5])
                            k.pack()
                            cont+=1
        volver = Button(confirmar,text='volver al menu',command = lambda: volverMenu(confirmar))
        volver.pack()
    else:
        l = Label(confirmar, text='Debe ingresar valores validos. Intente de nuevo.')
        l.pack()
        intentar = Button(confirmar, text='intentar de nuevo',command=lambda:InsertarMarca(confirmar))
        intentar.pack()
def siExisteMarca(pasillo,producto,nombre,codigo):
    listaMarcas = leer_marcas
    for i in range(len(listaMarcas)):
        if listaMarcas[i][0] == pasillo:
            if listaMarcas[i][1] == producto:
                if listaMarcas[i][2] == codigo and listaMarcas[i][3].upper() == nombre.upper():
                    return True
    return False
    
#4 HECHA DE NUEVO
def InsertarCliente(ventana):
    global abcd
    abcd = 'parado'
    if Administrador('2')==True:
        menuVentana=ventana
        menuVentana.withdraw()
        insertar = Tk()
        insertar.geometry('1080x720')
        l = Label(insertar,text='Por favor ingrese la informacion requerida: ')
        l.pack()
        a = Label(insertar,text='ID del cliente: ')
        a.pack()
        ID = Entry(insertar)
        ID.pack()
        b = Label(insertar,text='Nombre completo: ')
        b.pack()
        nombreCliente = Entry(insertar)
        nombreCliente.pack()
        c = Label(insertar,text='Codigo de ciudad: ')
        c.pack()
        codCiudad = Entry(insertar)
        codCiudad.pack()
        d = Label(insertar,text='Numero telefonico: ')
        d.pack()
        numeroCliente = Entry(insertar)
        numeroCliente.pack()
        e = Label(insertar,text='E-mail: ')
        e.pack()
        correoCliente = Entry(insertar)
        correoCliente.pack()
        confirmar = Button(insertar,text='confirmar',command = lambda: InsertarCliente_aux(insertar,str(ID.get()),str(nombreCliente.get()),str(codCiudad.get()),str(numeroCliente.get()),str(correoCliente.get())))
        confirmar.pack()
        volver = Button(insertar,text='volver al menu',command = lambda: volverMenu(insertar))
        volver.pack()
def InsertarCliente_aux(ventana,ID,nombre,ciudad,numero,correo):
    insertar = ventana
    insertar.withdraw()
    confirmar = Tk()
    confirmar.geometry('1080x720')
    if siExisteCliente(ID,nombre) == False:
        leer_clientes.append([ID,nombre,ciudad,numero,correo])
        l = Label(confirmar, text = 'El cliente se ha agregado al supermercado.')
        l.pack()
        cont = 1
        h = Label(confirmar, text='El nuevo cliente del supermercado es: ')
        h.pack()
        for i in range(len(leer_clientes)):
            if leer_clientes[i][0] == ID:
                k = Label(confirmar,text=('cliente: ' + leer_clientes[i][1]+" | cedula: "+leer_clientes[i][0]+" | Codigo de ciudad: "+leer_clientes[i][2]+" | Numero: "+leer_clientes[i][3]+" | Correo: "+leer_clientes[i][4]))
                k.pack()
                break
        volver = Button(confirmar,text='volver al menu',command = lambda: volverMenu(confirmar))
        volver.pack()
    else:
        l = Label(confirmar, text='El cliente ya existe.')
        l.pack()
        volver = Button(confirmar,text='volver al menu',command = lambda: volverMenu(confirmar))
        volver.pack()
def siExisteCliente(ID,nombre):
    listaClientes = leer_clientes
    for i in range(len(listaClientes)):
        if listaClientes[i][0]==ID or listaClientes[i][1].upper()==nombre.upper():
            return True
    return False

#5 REVISADA & CORREGIDA
def ModificarPrecio(ventana):
    global abcd
    abcd = 'parado'
    if Administrador('2')==True:
        menuVentana=ventana
        menuVentana.withdraw()
        modificar = Tk()
        modificar.geometry('1080x720')
        l = Label(modificar, text='Por favor indique la siguiente informacion: ')
        l.pack()
        b = Label(modificar, text='Codigo de marca: ')
        b.pack()
        codigoMarca = Entry(modificar)
        codigoMarca.pack()
        c= Label(modificar, text='Precio nuevo: ')
        c.pack()
        precioNuevo = Entry(modificar)
        precioNuevo.pack()
        confirmar = Button(modificar,text='confirmar',command=lambda:ModificarPrecio_aux(modificar,str(codigoMarca.get()),str(precioNuevo.get())))
        confirmar.pack()
        volver = Button(modificar,text='volver al menu',command=lambda:volverMenu(modificar))
        volver.pack()
def ModificarPrecio_aux(ventana,codigo,precio):
    modificar = ventana
    modificar.withdraw()
    busqueda = Tk()
    busqueda.geometry('1080x720')
    if precio.isdigit() == False:
        l = Label(busqueda, text='Debe ingresar un precio valido.')
        l.pack()
        volver = Button(busqueda,text='volver al menu',command = lambda: volverMenu(busqueda))
        volver.pack() 
    else:
        for i in range(len(leer_marcas)):
            if codigo == leer_marcas[i][2]:
                leer_marcas[i][5] = precio
                break
        l = Label(busqueda,text='El precio ha sido modificado.')
        l.pack()
        volver = Button(busqueda,text='volver al menu',command = lambda: volverMenu(busqueda))
        volver.pack()

#6 NUEVA
def ModificarImpuesto(ventana):
    global abcd
    abcd = 'parado'
    if Administrador('2')==True:
        menuVentana=ventana
        menuVentana.withdraw()
        modificar = Tk()
        modificar.geometry('1080x720')
        l = Label(modificar, text='Por favor indique la siguiente informacion: ')
        l.pack()
        b = Label(modificar, text='Codigo que desea cambiar (1 o 0): ')
        b.pack()
        codCanasta = Entry(modificar)
        codCanasta.pack()
        c= Label(modificar, text='Impuesto: ')
        c.pack()
        impuestoNuevo = Entry(modificar)
        impuestoNuevo.pack()
        confirmar = Button(modificar,text='confirmar',command=lambda:ModificarImpuesto_aux(modificar,str(codCanasta.get()),str(impuestoNuevo.get())))
        confirmar.pack()
        volver = Button(modificar,text='Volver al menu',command=lambda:volverMenu(modificar))
        volver.pack()
def ModificarImpuesto_aux(ventana,codigo,impuesto):
    modificar = ventana
    modificar.withdraw()
    busqueda = Tk()
    busqueda.geometry('1080x720')
    if impuesto.isdigit() == False:
        l = Label(busqueda, text='Debe ingresar un impuesto valido.')
        l.pack()
        volver = Button(busqueda,text='volver al menu',command = lambda: volverMenu(busqueda))
        volver.pack()
    else:
        #Variables locales CAMBIAR ANTES DE ENTREGAR#ya lo hice
        global impuestoCanasta1
        global impuestoCanasta0
        #------------------------------------------
        if codigo == '1':
            impuestoCanasta1 = impuesto
            l = Label(busqueda,text='El porcentaje para el codigo '+codigo+"es de: "+impuesto)
            l.pack()
            volver = Button(busqueda,text='volver al menu',command = lambda: volverMenu(busqueda))
            volver.pack()
        elif codigo == '0':
            impuestoCanasta0 = codigo
            l = Label(busqueda,text='El porcentaje para el codigo '+codigo+'es de:'+impuesto)
            l.pack()
            volver = Button(busqueda,text='volver al menu',command = lambda: volverMenu(busqueda))
            volver.pack()
        else:
            l = Label(busqueda, text='Debe ingresar un impuesto valido.')
            l.pack()
            volver = Button(busqueda,text='volver al menu',command = lambda: volverMenu(busqueda))
            volver.pack()

#7 NUEVA
def ModificarProductoCanastaBasica(ventana):
    global abcd
    abcd = 'parado'
    if Administrador('2')==True:
        menuVentana=ventana
        menuVentana.withdraw()
        modificar = Tk()
        modificar.geometry('1080x720')
        l = Label(modificar, text='Por favor indique la siguiente informacion: ')
        l.pack()
        b = Label(modificar, text='Codigo de marca: ')
        b.pack()
        codigoMarca = Entry(modificar)
        codigoMarca.pack()
        c= Label(modificar, text='Codigo de canasta nuevo (1 o 0): ')
        c.pack()
        canastaNueva = Entry(modificar)
        canastaNueva.pack()
        confirmar = Button(modificar,text='confirmar',command=lambda:ModificarCanasta_aux(modificar,str(codigoMarca.get()),str(canastaNueva.get())))
        confirmar.pack()
        volver = Button(modificar,text='volver al menu',command=lambda:volverMenu(modificar))
        volver.pack()
def ModificarCanasta_aux(ventana,codigo,canasta):
    modificar = ventana
    modificar.withdraw()
    busqueda = Tk()
    busqueda.geometry('1080x720')
    if canasta.isdigit() == False:
        l = Label(busqueda, text='Debe ingresar un precio valido.')
        l.pack()
        volver = Button(busqueda,text='volver al menu',command = lambda: volverMenu(busqueda))
        volver.pack()
    else:
        if canasta == '1' or canasta == '0':   
            for i in range(len(leer_inventario)):
                if codigo == leer_marcas[i][2]:
                    leer_inventario[i][5] = canasta
                    break
            l = Label(busqueda,text='El codigo de porcentaje ha sido modificado.')
            l.pack()
            volver = Button(busqueda,text='volver al menu',command = lambda: volverMenu(busqueda))
            volver.pack()
        else:
            l = Label(busqueda, text='Debe ingresar un precio valido.')
            l.pack()
            volver = Button(busqueda,text='volver al menu',command = lambda: volverMenu(busqueda))
            volver.pack()
    
#8 REVISADA & CORREGIDA
def EliminarProductos(ventana):
    global abcd
    abcd = 'parado'
    if Administrador('2')==True:
        menuVentana=ventana
        menuVentana.withdraw()
        eliminar = Tk()
        eliminar.geometry('1080x720')
        l = Label(eliminar, text='Por favor indique la siguiente informacion: ')
        l.pack()
        a = Label(eliminar, text='Codigo del pasillo: ')
        a.pack()
        codigoPasillo = Entry(eliminar)
        codigoPasillo.pack()
        b = Label(eliminar, text='Nombre del producto: ')
        b.pack()
        nombreProducto = Entry(eliminar)
        nombreProducto.pack()
        c = Label(eliminar, text='Codigo del producto: ')
        c.pack()
        codProducto = Entry(eliminar)
        codProducto.pack()
        busqueda = Button(eliminar,text='buscar',command=lambda: EliminarProductos_aux(eliminar,str(codigoPasillo.get()),str(nombreProducto.get()),str(codProducto.get())))
        busqueda.pack()
def EliminarProductos_aux(ventana,pasillo,nombre,codigo):
    eliminar = ventana
    eliminar.withdraw()
    busqueda = Tk()
    busqueda.geometry('1080x720')
    if validarInputProducto(pasillo,nombre,codigo):
        cont = contarProductos(leer_productos,codigo)
        for j in range(cont):
            for i in range(len(leer_productos)):
                if leer_productos[i][1] == codigo:
                    del leer_productos[i]
                    break
        cont = contarProductos(leer_marcas,codigo)
        for j in range(cont):
            for i in range(len(leer_marcas)):
                if leer_marcas[i][1] == codigo:
                    del leer_marcas[i]
                    break
        cont = contarProductos(leer_inventario,codigo)
        for j in range(cont):
            for i in range(len(leer_inventario)):
                if leer_inventario[i][1] == codigo:
                    del leer_inventario[i]
                    break
        l = Label(busqueda, text='El producto deseado se ha eliminado del supermercado.')
        l.pack()
        volver = Button(busqueda,text='volver al menu',command = lambda: volverMenu(busqueda))
        volver.pack()
    else:
        l = Label(busqueda, text='Los valores no son correctos o no coinciden entre si.')
        l.pack()
        volver = Button(busqueda,text='volver al menu',command = lambda: volverMenu(busqueda))
        volver.pack()
def validarInputProducto(pasillo,nombre,codigo):
    listaProductos = leer_productos
    for i in range (len(listaProductos)):
        if listaProductos[i][0] == pasillo and listaProductos[i][1] == codigo and listaProductos[i][2].upper() == nombre.upper():
            return True
    return False
def contarProductos(lista,codigo):
    cont = 0
    for i in range(len(lista)):
        if lista[i][1] == str(codigo):
            cont += 1
    return cont

#9 REVISADA & CORREGIDA
def EliminarPasillos(ventana):
    global abcd
    abcd = 'parado'
    if Administrador('2')==True:
        menuVentana=ventana
        menuVentana.withdraw()
        eliminar = Tk()
        eliminar.geometry('1080x720')
        l = Label(eliminar, text='Por favor indique la siguiente informacion: ')
        l.pack()
        b = Label(eliminar, text='Nombre del pasillo: ')
        b.pack()
        nombrePasillo = Entry(eliminar)
        nombrePasillo.pack()
        c = Label(eliminar, text='Codigo del pasillo: ')
        c.pack()
        codPasillo = Entry(eliminar)
        codPasillo.pack()
        busqueda = Button(eliminar,text='buscar',command=lambda: EliminarPasillos_aux(eliminar,str(nombrePasillo.get()),str(codPasillo.get())))
        busqueda.pack()
def EliminarPasillos_aux(ventana,nombre,codigo):
    eliminar = ventana
    eliminar.withdraw()
    busqueda = Tk()
    busqueda.geometry('1080x720')
    if validarInputPasillo(nombre,codigo):
        for i in range(len(leer_pasillos)):
            if leer_pasillos[i][0] == codigo:
                leer_pasillos[i] = ['00','vacio']
        cont = contarPasillos(leer_productos,codigo)
        for j in range(cont):
            for i in range(len(leer_productos)):
                if leer_productos[i][0] == codigo:
                    del leer_productos[i]
                    break
        cont = contarPasillos(leer_marcas,codigo)
        for j in range(cont):
            for i in range(len(leer_marcas)):
                if leer_marcas[i][0] == codigo:
                    del leer_marcas[i]
                    break
        cont = contarPasillos(leer_inventario,codigo)
        for j in range(cont):
            for i in range(len(leer_inventario)):
                if leer_inventario[i][0] == codigo:
                    del leer_inventario[i]
                    break
        l = Label(busqueda, text='El pasillo deseado se ha eliminado del supermercado.')
        l.pack()
        volver = Button(busqueda,text='volver al menu',command = lambda: volverMenu(busqueda))
        volver.pack()
    else:
        l = Label(busqueda, text='Los valores no son correctos o no coinciden entre si.')
        l.pack()
        volver = Button(busqueda,text='volver al menu',command = lambda: volverMenu(busqueda))
        volver.pack()
def validarInputPasillo(nombre,codigo):
    listaPasillos = leer_pasillos
    for i in range (len(listaPasillos)):
        if listaPasillos[i][0] == codigo and listaPasillos[i][1].upper() == nombre.upper():
            return True
    return False
def contarPasillos(lista,codigo):
    cont = 0
    for i in range(len(lista)):
        if lista[i][0] == str(codigo):
            cont += 1
    return cont

    
#10 NUEVA
def EliminarMarca(ventana):
    global abcd
    abcd = 'parado'
    if Administrador('2')==True:
        menuVentana=ventana
        menuVentana.withdraw()
        eliminar = Tk()
        eliminar.geometry('1080x720')
        l = Label(eliminar, text = 'Por favor indique la siguiente informacion: ')
        l.pack()
        a = Label(eliminar, text='codigo del pasillo: ')
        a.pack()
        codigoPasillo = Entry(eliminar)
        codigoPasillo.pack()
        b = Label(eliminar, text='codigo del producto: ')
        b.pack()
        codProducto = Entry(eliminar)
        codProducto.pack()
        c = Label(eliminar, text='nombre de la marca: ')
        c.pack()
        nombreMarca = Entry(eliminar)
        nombreMarca.pack()
        d = Label(eliminar, text='codigo de la marca: ')
        d.pack()
        codMarca = Entry(eliminar)
        codMarca.pack()
        busqueda = Button(eliminar,text='buscar',command=lambda: EliminarMarca_aux(eliminar,str(codigoPasillo.get()),str(codProducto.get()),str(nombreMarca.get()),str(codMarca.get())))
        busqueda.pack()
def EliminarMarca_aux(ventana,pasillo,producto,nombre,codigo):
    eliminar = ventana
    eliminar.withdraw()
    busqueda = Tk()
    busqueda.geometry('1080x720')
    if validarInputMarcas(pasillo,producto,nombre,codigo):
        cont = contarMarcas(leer_marcas,codigo)
        for j in range(cont):
            for i in range(len(leer_marcas)):
                if leer_marcas[i][2] == codigo:
                    del leer_marcas[i]
                    break
        cont = contarMarcas(leer_inventario,codigo)
        for j in range(cont):
            for i in range(len(leer_inventario)):
                if leer_inventario[i][2] == codigo:
                    del leer_inventario[i]
                    break
        l = Label(busqueda, text='La marca deseada se ha eliminado del supermercado.')
        l.pack()
        volver = Button(busqueda,text='volver al menu',command = lambda: volverMenu(busqueda))
        volver.pack()
    else:
        l = Label(busqueda, text='Los valores no son correctos o no coinciden entre si.')
        l.pack()
        volver = Button(busqueda,text='volver al menu',command = lambda: volverMenu(busqueda))
        volver.pack()
def validarInputMarca(pasillo,producto,nombre,codigo):
    listaMarcas = leer_marcas
    for i in range(len(listaMarcas)):
        if listaMarcas[i][0] == pasillo and listaMarcas[i][1] == producto and listaMarcas[i][2] == codigo and listaMarcas[i][3].upper() == nombre.upper():
            return True
    return False
def contarMarcas(lista,codigo):
    cont = 0
    for i in range(len(lista)):
        if lista[i][2] == str(codigo):
            cont += 1
    return cont

#11 NUEVA
def EliminarCliente(ventana):
    global abcd
    abcd = 'parado'
    if Administrador('2')==True:
        menuVentana=ventana
        menuVentana.withdraw()
        eliminar = Tk()
        eliminar.geometry('1080x720')
        l = Label(eliminar, text='Por favor indique la siguiente informacion: ')
        l.pack()
        a = Label(eliminar, text='la identificacion del cliente: ')
        a.pack()
        IDcliente = Entry(eliminar)
        IDcliente.pack()
        busqueda = Button(eliminar,text='buscar',command=lambda: EliminarCliente_aux(eliminar,str(IDcliente.get())))
        busqueda.pack()
def EliminarCliente_aux(ventana,ID):
    eliminar = ventana
    eliminar.withdraw()
    busqueda = Tk()
    busqueda.geometry('1080x720')
    if validarInputUsuario(ID):
        for i in range(len(leer_clientes)):
            if leer_clientes[i][0] == ID:
                del leer_clientes[i]
        l = Label(busqueda, text='El cliente deseado se ha eliminado del supermercado.')
        l.pack()
        volver = Button(busqueda,text='volver al menu',command = lambda: volverMenu(busqueda))
        volver.pack()
    else:
        l = Label(busqueda, text='Los valores no son correctos o no coinciden entre si.')
        l.pack()
        volver = Button(busqueda,text='volver al menu',command = lambda: volverMenu(busqueda))
        volver.pack()
def validarInputUsuario(codigo):
    listaClientes = leer_clientes
    for i in range(len(listaClientes)):
        if listaClientes[i][0] == codigo:
            return True
    return False
    
#12 REVISADA & CORREGIDA
def ConsultarPrecio(ventana):
    global abcd
    if Administrador('2')==False:
        menuVentana = ventana
        menuVentana.withdraw()
        consultar = Tk()
        consultar.geometry('1080x720')
        l = Label(consultar, text='La lista de productos con precios: ')
        l.pack()
        listaNueva = leer_marcas

        def myfunction(event):
            canvas.configure(scrollregion=canvas.bbox("all"))

        myframe=Frame(consultar,relief=GROOVE,width=100,height=500,bd=1)
        myframe.place(x=350,y=200)

        canvas=Canvas(myframe)
        frame=Frame(canvas)
        myscrollbar=Scrollbar(myframe,orient="vertical",command=canvas.yview)
        canvas.configure(yscrollcommand=myscrollbar.set)

        myscrollbar.pack(side="right",fill="y")
        canvas.pack(side="right")
        canvas.create_window((0,0),window=frame,anchor='nw')
        frame.bind("<Configure>",myfunction)
    
    cont = 1
    for i in range (len(listaNueva)):
        Label(frame,text=(str(cont) + ". " +"Codigo de marca:"+listaNueva[i][2]+"||"+ "Producto: " + listaNueva[i][3] + " | Precio: " + listaNueva[i][5])).grid(row=i,column=1)
        cont += 1
    volver = Button(consultar,text='volver al menu',command = lambda: volverMenu(consultar))
    volver.pack()
    
#13 REVISADA & CORREGIDA
def ConsultarProductoCanasta(ventana):
    global abcd
    if Administrador('2')==False:
        menuVentana = ventana
        menuVentana.withdraw()
        consultar = Tk()
        consultar.geometry('1080x720')
        h = Label(consultar,text='indique el codigo de Marca que desea consultar: ')
        h.pack()
        entrada = Entry(consultar)
        entrada.pack()
        buscar = Button(consultar,text='buscar',command= lambda: ConsultarCanasta_aux(entrada.get(),consultar))
        buscar.pack()
        l = Label(consultar, text='La lista de productos con precios: ')
        l.pack()

        def myfunction(event):
            canvas.configure(scrollregion=canvas.bbox("all"))
        
        myframe=Frame(consultar,relief=GROOVE,width=50,height=100,bd=1)
        myframe.place(x=350,y=200)

        canvas=Canvas(myframe)
        frame=Frame(canvas)
        myscrollbar=Scrollbar(myframe,orient="vertical",command=canvas.yview)
        canvas.configure(yscrollcommand=myscrollbar.set)

        myscrollbar.pack(side="right",fill="y")
        canvas.pack(side="left")
        canvas.create_window((0,0),window=frame,anchor='nw')
        frame.bind("<Configure>",myfunction)
        
        listaNueva = leer_marcas
        cont = 1
        
        for i in range (len(listaNueva)):
            Label(frame,text=(str(cont) + ". " +"Codigo de marca:"+listaNueva[i][2]+"||"+ "Producto: " + listaNueva[i][3] + " | Precio: " + listaNueva[i][5])).grid(row=i,column=1)
            cont += 1
def ConsultarCanasta_aux(Input,ventana):
    consultar = ventana
    listaNueva = leer_inventario
    indice = buscarMarca(Input)
    if indice > -1:
        if listaNueva[indice][5] == '1':
            l = Label(consultar, text=('El producto '+listaNueva[indice][3]+' pertenece a la canasta basica.'))
            l.pack()
        else:
            l = Label(consultar, text=('El producto: '+listaNueva[indice][3]+' no pertenece a la canasta basica.'))
            l.pack()
    else:
        k = Label(consultar,text='ERROR: la marca que busca no existe.')
        k.pack()
    volver = Button(consultar,text='volver al menu',command = lambda: volverMenu(consultar))
    volver.pack()

#14 REVISADA & CORREGIDA
def ConsultarImpuestoProducto(ventana):
    global abcd
    if Administrador('2')==False:
        menuVentana = ventana
        menuVentana.withdraw()
        consultar = Tk()
        consultar.geometry('1080x720')
        h = Label(consultar,text='indique el codigo de producto que desea consultar: ')
        h.pack()
        entrada = Entry(consultar)
        entrada.pack()
        buscar = Button(consultar,text='buscar',command= lambda: consultarImpuesto_aux(entrada.get(),consultar))
        buscar.pack()
        l = Label(consultar, text='La lista de productos con precios: ')
        l.pack()
        listaNueva = leer_marcas

        def myfunction(event):
            canvas.configure(scrollregion=canvas.bbox("all"))
        
        myframe=Frame(consultar,relief=GROOVE,width=50,height=100,bd=1)
        myframe.place(x=350,y=200)

        canvas=Canvas(myframe)
        frame=Frame(canvas)
        myscrollbar=Scrollbar(myframe,orient="vertical",command=canvas.yview)
        canvas.configure(yscrollcommand=myscrollbar.set)

        myscrollbar.pack(side="right",fill="y")
        canvas.pack(side="left")
        canvas.create_window((0,0),window=frame,anchor='nw')
        frame.bind("<Configure>",myfunction)
        
        cont = 1
        for i in range (len(listaNueva)):
            Label(frame,text=(str(cont) + ". " +"Codigo de marca:"+listaNueva[i][2]+"||"+ "Producto: " + listaNueva[i][3] + " | Precio: " + listaNueva[i][5])).grid(row=i,column=1)
            cont += 1
def consultarImpuesto_aux(Input,ventana):
    global impuestoCanasta0
    global impuestoCanasta1
    consultar = ventana
    listaNueva = leer_inventario
    indice = buscarMarca(Input)
    if indice > -1:
        if listaNueva[indice][5] == '1':
            l = Label(consultar, text=('El producto '+listaNueva[indice][3]+' tiene un impuesto de: '+str(impuestoCanasta1)))
            l.pack()
        else:
            l = Label(consultar, text=('El producto: '+listaNueva[indice][3]+' tiene un impuesto de: '+str(impuestoCanasta0)))
            l.pack()
    else:
        k = Label(consultar,text='ERROR: la marca que busca no existe.')
        k.pack()
    volver = Button(consultar,text='volver al menu',command = lambda: volverMenu(consultar))
    volver.pack()

#15 REVISADA & CORREGIDA
def ConsultarPrecioProducto(ventana):
    global abcd
    if Administrador('2')==False:
        menuVentana = ventana
        menuVentana.withdraw()
        consultar = Tk()
        consultar.geometry('1080x720')
        h = Label(consultar,text='indique el codigo de Marca que desea consultar: ')
        h.pack()
        entrada = Entry(consultar)
        entrada.pack()
        buscar = Button(consultar,text='buscar',command= lambda: ConsultarPrecio_aux(entrada.get(),consultar))
        buscar.pack()

        def myfunction(event):
            canvas.configure(scrollregion=canvas.bbox("all"))
        
        myframe=Frame(consultar,relief=GROOVE,width=50,height=100,bd=1)
        myframe.place(x=350,y=200)

        canvas=Canvas(myframe)
        frame=Frame(canvas)
        myscrollbar=Scrollbar(myframe,orient="vertical",command=canvas.yview)
        canvas.configure(yscrollcommand=myscrollbar.set)

        myscrollbar.pack(side="right",fill="y")
        canvas.pack(side="left")
        canvas.create_window((0,0),window=frame,anchor='nw')
        frame.bind("<Configure>",myfunction)

        listaNueva=leer_marcas        
        cont = 1
        for i in range (len(listaNueva)):
            Label(frame,text=(str(cont) + ". " +"Codigo de marca:"+listaNueva[i][2]+"||"+ "Producto: " + listaNueva[i][3] + " | Precio: " + listaNueva[i][5])).grid(row=i,column=1)
            cont += 1        
        
def ConsultarPrecio_aux(Input,ventana):
    consultar = ventana
    listaNueva = leer_marcas
    indice = buscarMarca(Input)
    if indice > -1:
        l = Label(consultar, text='El producto ' + listaNueva[indice][3] +' tiene un precio de: ' + listaNueva[indice][5])
        l.pack()
    else:
        k = Label(consultar,text='ERROR: la marca que busca no existe.')
        k.pack()
    volver = Button(consultar,text='volver al menu',command = lambda: volverMenu(consultar))
    volver.pack()

#16
def Facturar():
    if Administrador('1')==True:
        global cola_de_pagar
        global reportes_conexion
        if cola_de_pagar == []:
            pass
        else:
            i = 0
            persona = cola_de_pagar[0][0]
            lista_productos = cola_de_pagar[0][1:]
            cola_de_pagar = cola_de_pagar[1:]
            global lista_ordenada
            lista_ordenada += [persona]+ordenamientoBurbuja(lista_productos)
            i=0
            while(i<=len(lista_productos)-1):
                global lista__1
                lista__1+=[lista_productos[i][0]]
                global lista__2
                lista__2+=[[lista_productos[i][0],lista_productos[i][1],lista_productos[i][3]]]
                global lista__3
                lista__3+=[[lista_productos[i][2],lista_productos[i][4],lista_productos[i][5]]]
                global lista__4
                lista__4+=[[persona,lista_productos[i][6]]]
                i+=1
            global ordenada
            ordenada = man([lista_ordenada])
            global string1
            string1 = ";".join(lista__1)
            global string2
            for i in range(0,len(lista__2)):
                string2 += ";".join(lista__2[i]) +"+"
            global string3
            for i in range(0,len(lista__3)):
                string3 += ";".join(lista__3[i]) + "+"
            global string4
            for i in range(0,len(lista__4)):
                string4 += ";".join(lista__4[i]) + "+"
            if Administrador('3')==True:
                lista_ordenada = []
                lista__1 = []
                lista__2 = []
                lista__3 = []
                lista__4 = []
                return "LISTO FACTURADO"

def man(listaC):
    if listaC==[]:
        return ''
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


def ordenamientoBurbuja(lista):
    i=0
    while(i<=len(lista)-1):
        j=0
        while(j+1<=len(lista)-1):
            if(int(lista[j][5]) < int(lista[j+1][5])):
                k = lista[j+1]
                lista[j+1] = lista[j]
                lista[j] = k
            else:
                j+=1
        i+=1
    return lista
            

    

def RevisarGondolas(ventana):
    global abcd
    abcd = 'parado'
    if Administrador('2')==True:
        menuVentana = ventana
        menuVentana.withdraw()
        revisar = Tk()
        revisar.geometry('1080x720')
        listaMarcas = leer_marcas
        cont = 0
        h = Label(revisar,text='Lista de productos completa para revision de gondolas.')
        h.pack()

        def myfunction(event):
            canvas.configure(scrollregion=canvas.bbox("all"))
        
        myframe=Frame(revisar,relief=GROOVE,width=50,height=100,bd=1)
        myframe.place(x=350,y=150)

        canvas=Canvas(myframe)
        frame=Frame(canvas)
        myscrollbar=Scrollbar(myframe,orient="vertical",command=canvas.yview)
        canvas.configure(yscrollcommand=myscrollbar.set)

        myscrollbar.pack(side="right",fill="y")
        canvas.pack(side="left")
        canvas.create_window((0,0),window=frame,anchor='nw')
        frame.bind("<Configure>",myfunction)
        
        for i in range(len(listaMarcas)):
            Label(frame,text=(str(cont) + '. Producto: ' + listaMarcas[i][3] + ' || ' + 'Cantidad: ' + listaMarcas[i][4])).grid(row=i,column=1)
            cont += 1
        l = Label(revisar,text='Seleccione el producto que tiene poca cantidad ( <= 2): ')
        l.pack()
        codMarca = Entry(revisar)
        codMarca.pack()
        busqueda = Button(revisar,text='buscar',command = lambda: RevisarGondolas_aux(revisar,str(codMarca.get())))
        busqueda.pack()
        volver = Button(revisar,text='volver al menu',command = lambda: volverMenu(revisar))
        volver.pack()
def RevisarGondolas_aux(ventana,marca):
    global lista_gon
    revisar = ventana
    revisar.withdraw()
    gondolas = Tk()
    gondolas.geometry('1080x720')
    listaMarcas = leer_marcas
    print(listaMarcas)
    if int(marca) <= len(listaMarcas):
        print([listaMarcas[int(marca)][3]])
        lista_gon += [listaMarcas[int(marca)][3]]
        if int(listaMarcas[int(marca)][4]) <= 2:
            a = Label(gondolas,text='Ingrese la cantidad de productos que desea colocar en el estante: ')
            a.pack()
            cant = Entry(gondolas)
            cant.pack()
            siguiente = Button(gondolas,text='siguiente',command = lambda: RevisarGondolas_aux1(gondolas,marca,str(cant.get())))
            siguiente.pack()
        else:
            k = Label(gondolas,text='Se producio un errror. Por favor intente de nuevo.')
            k.pack()
            intentar = Button(revisar,text='intentar de nuevo',command = lambda: RevisarGondolas(revisar))
            intentar.pack()
    else:
        k = Label(gondolas,text='Se producio un errror. Por favor intente de nuevo.')
        k.pack()
        intentar = Button(revisar,text='intentar de nuevo',command = lambda: RevisarGondolas(revisar))
        intentar.pack()
def RevisarGondolas_aux1(ventana,marca,cant):
    gondolas = ventana
    gondolas.withdraw()
    siguiente = Tk()
    siguiente.geometry('1080x720')
    listaInventario = leer_inventario
    listaMarcas = leer_marcas
    if cant.isdigit() == False:
        h = Label(siguiente,text='Se producio un errror. Por favor intente de nuevo.')
        h.pack()
        intentar = Button(siguiente,text='intentar de nuevo',command = lambda: RevisarGondolas(siguiente))
        intentar.pack()
    else:
        for i in range(len(leer_inventario)):
            lista1 = [leer_marcas[int(marca)][0]]+[leer_marcas[int(marca)][1]]+[leer_marcas[int(marca)][2]]
            lista2 = [leer_inventario[i][0]]+[leer_inventario[i][1]]+[leer_inventario[i][2]]
            if lista1 == lista2:
                resta = int(leer_inventario[i][4]) - int(cant)
                if resta < 20:
                    l = Label(siguiente,text='Hay muy pocos productos en el inventario. Por favor reviselo.')
                    l.pack()
                    intentar = Button(siguiente,text='intentar de nuevo',command = lambda: RevisarGondolas(siguiente))
                    intentar.pack()
                else:
                    leer_marcas[int(marca)][4] = str(cant)
                    leer_inventario[i][4] = str(resta)
        h = Label(siguiente,text='Se ha producido el cambio.')
        h.pack()
        volver = Button(siguiente,text='volver al menu',command = lambda: volverMenu(siguiente))
        volver.pack()

#18 NUEVA
def VerificarInventario(ventana):
    global abcd
    abcd = 'parado'
    if Administrador('2')==True:
        menuVentana = ventana
        menuVentana.withdraw()
        revisar = Tk()
        revisar.geometry('1080x720')
        listaInventario = leer_inventario
        cont = 0
        h = Label(revisar,text='Lista de inventario completa para revision.')
        h.pack()

        def myfunction(event):
            canvas.configure(scrollregion=canvas.bbox("all"))
        
        myframe=Frame(revisar,relief=GROOVE,width=50,height=100,bd=1)
        myframe.place(x=350,y=150)

        canvas=Canvas(myframe)
        frame=Frame(canvas)
        myscrollbar=Scrollbar(myframe,orient="vertical",command=canvas.yview)
        canvas.configure(yscrollcommand=myscrollbar.set)

        myscrollbar.pack(side="right",fill="y")
        canvas.pack(side="left")
        canvas.create_window((0,0),window=frame,anchor='nw')
        frame.bind("<Configure>",myfunction)
        
        for i in range(len(listaInventario)):
            Label(frame,text=(str(cont) + '. Producto: ' + listaInventario[i][3] + ' || ' + 'Cantidad: ' + listaInventario[i][4])).grid(row=i,column=1)
            cont += 1
        k = Label(revisar,text='Seleccione el producto que contiene 20 o menos unidades: ')
        k.pack()
        codMarca = Entry(revisar)
        codMarca.pack()
        busqueda = Button(revisar,text='buscar',command = lambda: VerificarInventario_aux(revisar,str(codMarca.get())))
        busqueda.pack()
        volver = Button(revisar,text='volver al menu',command = lambda: volverMenu(revisar))
        volver.pack()
def VerificarInventario_aux(ventana,marca):
    revisar = ventana
    revisar.withdraw()
    inventarioV = Tk()
    inventarioV.geometry('1080x720')
    listaInventario = leer_inventario
    if int(marca) <= len(listaInventario):
        l = Label(inventarioV,text='Ingrese la cantidad de productos que desea agregar: ')
        l.pack()
        cant = Entry(inventarioV)
        cant.pack()
        siguiente = Button(inventarioV,text='siguiente',command=lambda: VerificarInventario_aux1(inventarioV,marca,str(cant.get())))
        siguiente.pack()
    else:
        k = Label(inventarioV,text='Se producio un errror. Por favor intente de nuevo.')
        k.pack()
        intentar = Button(inventarioV,text='intentar de nuevo',command = lambda: RevisarGondolas(inventarioV))
        intentar.pack()
def VerificarInventario_aux1(ventana,marca,cant):
    inventarioV = ventana
    inventarioV.withdraw()
    siguiente = Tk()
    siguiente.geometry('1080x720')
    if cant.isdigit() == False:
        h = Label(siguiente,text='Se producio un errror. Por favor intente de nuevo.')
        h.pack()
        intentar = Button(siguiente,text='intentar de nuevo',command = lambda: RevisarGondolas(siguiente))
        intentar.pack()
    else:
        if int(leer_inventario[int(marca)][4]) <= 20:
            suma = int(leer_inventario[int(marca)][4]) + int(cant)
            leer_inventario[int(marca)][4] = str(suma)
            h = Label(siguiente,text='Se ha producido el cambio.')
            h.pack()
            volver = Button(siguiente,text='volver al menu',command = lambda: volverMenu(siguiente))
            volver.pack()


#19(FALTA)
def ReportesAdministrativos(ventana):
    ventana.withdraw()
    ventana2 = Toplevel(ventana)
    ventana2.configure(bg = "white")
    ventana2.geometry("1280x720")
    global repo
    if Administrador('4')==True:
        h = Label(ventana2, text = repo,bg="White", fg = 'Black',font = ("Serif", 13))
        h.pack()
        l = Button(ventana2,text = "SALIR",command=lambda:volverMenu(ventana2))
        l.pack()
        ventana2.mainloop()
    






#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------





#######HASTA AQUI##################

def recibir(string):
    global todo
    todo = string
    string = string.split('+')
    global leer_ciudades 
    global leer_clientes 
    global leer_inventario 
    global leer_marcas 
    global leer_pasillos 
    global leer_productos
    global leer_administrador
    global actualizador
    leer_ciudades = desparsear(string[0])
    leer_clientes = desparsear(string[1])
    leer_inventario = desparsear(string[2])
    leer_marcas = desparsear(string[3])
    leer_pasillos = desparsear(string[4])
    leer_productos = desparsear(string[5])
    leer_administrador = desparsear(string[6])
    if actualizador == 1:
        return True
    else:
        actualizador = 1
        return validar_administrador()

def desparsear(string):
    string = string.split('-')
    for i in range(0,len(string)):
        string[i] = string[i].split(';')
    return string

def validar_administrador():
    ventana = Tk()
    ventana.configure(bg="Black")
    ventana.geometry("600x600")
    cedula = Entry(ventana)
    cedula.pack()
    titulo = Label(ventana, text = "SUPERMERCADO SANCHEZE",bg="White", fg = 'Black',font = ("Serif", 30)).place(x=0,y=300)
    ingresar = Button(ventana,text = "-->",font = ("Serif", 15),bg = "White",height="2",width="20",command=lambda:validar_administrador_aux(cedula.get(),ventana)).place(x=0,y=500)
    ventana.mainloop()

    
def validar_administrador_aux(entrada,ventana):
    ventana.withdraw()
    listaAdmins = leer_administrador
    global cola_de_pagar
    global cola_de_espera
    for i in range(len(listaAdmins)):
        if str(entrada) == listaAdmins[i][0]:
            return inicio()
    return validar_administrador()
    
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

def parsear_Ciudades():
    global leer_ciudades
    lista = leer_ciudades
    for i in range(0,len(lista)):
        lista[i]=';'.join(lista[i])
    lista='-'.join(lista)
    return lista

def parsear_Clientes():
    global leer_clientes
    lista = leer_clientes
    for i in range(0,len(lista)):
        lista[i]=';'.join(lista[i])
    lista='-'.join(lista)
    return lista


def parsear_Inventario():
    global leer_inventario
    lista = leer_inventario
    for i in range(0,len(lista)):
        lista[i]=';'.join(lista[i])
    lista='-'.join(lista)
    return lista

def parsear_MarcasProductos():
    global leer_marcas
    lista = leer_marcas
    for i in range(0,len(lista)):
        lista[i]=';'.join(lista[i])
    lista='-'.join(lista)
    return lista

def parsear_Pasillos():
    global leer_pasillos
    lista = leer_pasillos
    for i in range(0,len(lista)):
        lista[i]=';'.join(lista[i])
    lista='-'.join(lista)
    return lista

def parsear_ProductosPasillos():
    global leer_productos
    lista = leer_productos
    for i in range(0,len(lista)):
        lista[i]=';'.join(lista[i])
    lista='-'.join(lista)
    return lista

def parsear_administrador():
    global leer_administrador
    lista = leer_administrador
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
    lista6 = parsear_ProductosPasillos()
    listafinal = lista1+lista2+lista3+lista4+lista5+lista6
    return listafinal

import socket
def Administrador(x):
    global cola_de_pagar
    global cola_de_espera
    global abcd
    global ordenada
    global string1
    global string2
    global string3
    global string4
    global reportes_conexion
    HOST = 'localhost'  # The server's hostname or IP address
    PORT = 65432        # The port used by the server
    message='conectado'
    admi_socket= socket.socket()
    admi_socket.connect_ex((HOST,PORT))
    while message.lower().strip()!='Bye':
        if x=='0':
            data ='abrir_menu'
            admi_socket.send(data.encode())
            data=admi_socket.recv(100000).decode()
            return recibir(data)
        elif x=='1':
            data = 'cola'
            admi_socket.send(data.encode())
            data=admi_socket.recv(100000).decode()
            if data=='p':
                return True
            else:
                cola_de_pagar+=nam(data)
                cola_de_espera = nam(data)
                return True
        elif x=='2':
            if abcd == 'parado':
                data = 'hilo'
                admi_socket.send(data.encode())
                return True
            else:
                data = 'nohilo'
                admi_socket.send(data.encode())
                return False###aqui
        elif x=='3':
            stringa = '87'+ordenada + '*' + string1 + '*' + string2 + '*' + string3 + '*' + string4
            data = stringa
            admi_socket.send(data.encode())
            data=admi_socket.recv(100000).decode()
            reportes_conexion  = data
            return True
        elif x=='4':
            global repo
            data = 'genere'
            admi_socket.send(data.encode())
            data=admi_socket.recv(100000).decode()
            repo  = data
            return True
        elif x=='5':
            data = "!"+parsear_todo()
            admi_socket.send(data.encode())
            data=admi_socket.recv(100000).decode()
            if data == 'yeah':
                return True
            
            
            
Administrador('0')

##from tkinter import *
##master = Tk()
##master.geometry('1080x720')
##l = Label(master, text=('Bienvenido al supermercado!' + '\n' + 'Por favor ingrese su codigo de administrador: '))
##l.pack()
##cedula = Entry()
##cedula.pack()
##botonInicio = Button(master,text='Iniciar',command = lambda: menu_digital(cedula.get()))
##botonInicio.pack()
##master.mainloop()


