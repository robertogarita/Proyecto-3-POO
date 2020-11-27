from tkinter import *
lista_ciudades = []
lista_clientes = []
lista_inventario = []
lista_marcas = []
lista_pasillos = []
lista_productos = []
impuestoCanasta1 = 13
impuestoCanasta0 = 1
cola_de_espera = []
cola_de_pagar = []
todo = ''
todo1 = ''
cedula_vieja = ''
factura = ''


 
def menu(x,cedula,ventana):
    global cola_de_espera
    global cola_de_pagar
    cola_de_espera = []
    cola_de_pagar = []
    ventana.withdraw()
    ventana3 = Toplevel(ventana)
    ventana3.geometry("800x800")
    ventana3.configure(bg = "Black")
    titulo = Label(ventana3, text = "MENU PRINCIPAL",bg="Black", fg = 'White',font = ("Serif", 15)).place(x=10,y=10)
    boton1 = Button(ventana3, text = "1.     Ver Todos Los precio (monitor) " , bg="White", fg = 'Black',font = ("Serif", 15),command=lambda:consultarTodosPrecios(cola_de_espera,cola_de_pagar,x,cedula,ventana3)).place(x=20,y=200)
    boton2 = Button(ventana3, text = "2.     Consultar si un producto es de la canasta (monitor)" , bg="White", fg = 'Black',font = ("Serif", 15),command=lambda:consultarCanasta(cola_de_espera,cola_de_pagar,x,cedula,ventana3)).place(x=20,y=250)
    boton3 = Button(ventana3, text = "3.     Consultar el % impuesto de un producto(monitor)" , bg="White", fg = 'Black',font = ("Serif", 15),command=lambda:consultarImpuesto(cola_de_espera,cola_de_pagar,x,cedula,ventana3)).place(x=20,y=300)
    boton4 = Button(ventana3, text = "4.     Consultar el precio de un producto (monitor)" , bg="White", fg = 'Black',font = ("Serif", 15),command=lambda:consultarPrecio(cola_de_espera,cola_de_pagar,x,cedula,ventana3)).place(x=20,y=350)
    global lista_clientes
    boton6 = Button(ventana3, text = "6.     Ingresar cedula" , bg="White", fg = 'Black',font = ("Serif", 15),command=lambda:validar_2(ventana3,lista_clientes)).place(x=20,y=450)
    boton8 = Button(ventana3, text = "9.     Salir " , bg="White", fg = 'Black',font = ("Serif", 15),command=lambda:ventana3.destroy()).place(x=20,y=600)
    if x == 0:
        boton5 = Button(ventana3, text = "5.     COMPRAR" , bg="White", fg = 'Black',font = ("Serif", 15),command=lambda:mostrar_pasillos(cola_de_espera,cola_de_pagar,cedula,ventana3)).place(x=20,y=400)
        boton7 = Button(ventana3, text = "7.     Ver reporte TXT " , bg="White", fg = 'Black',font = ("Serif", 15),command=lambda:reporteP(x,cedula,ventana3)).place(x=20,y=500)
        boton9 = Button(ventana3, text = "8.     Ver Factura " , bg="White", fg = 'Black',font = ("Serif", 15),command=lambda:ver_factura(x,cedula,ventana3)).place(x=20,y=550)
#1
def consultarTodosPrecios(cola_de_espera,cola_de_pagar,x,cedula,ventana3):
    ventana3.withdraw()
    consultar = Tk()
    consultar.geometry('1280x720')
    if cliente ('verificar')==False:
        return consultarTodosPrecios(cola_de_espera,cola_de_pagar,x,cedula,consultar)
    else:
        l = Label(consultar, text='La lista de productos con precios: ')
        l.pack()
        
        def myfunction(event):
            canvas.configure(scrollregion=canvas.bbox("all"))
        
        myframe=Frame(consultar,relief=GROOVE,width=50,height=100,bd=1)
        myframe.place(x=450,y=60)

        canvas=Canvas(myframe)
        frame=Frame(canvas)
        myscrollbar=Scrollbar(myframe,orient="vertical",command=canvas.yview)
        canvas.configure(yscrollcommand=myscrollbar.set)

        myscrollbar.pack(side="right",fill="y")
        canvas.pack(side="left")
        canvas.create_window((0,0),window=frame,anchor='nw')
        frame.bind("<Configure>",myfunction)
        
        listaNueva = lista_marcas
        cont = 1
        for i in range (len(listaNueva)):
            Label(frame,text=(str(cont) + ". " +"Codigo de marca:"+listaNueva[i][2]+"||"+ "Producto: " + listaNueva[i][3] + " | Precio: " + listaNueva[i][5])).grid(row=i,column=1)
            cont += 1
        volver = Button(consultar,text='volver',bg = 'Black',fg = 'White',font = ("Serif", 15),command = lambda: menu(x,cedula,consultar)).place(x=0,y=0)
#2
def consultarCanasta(cola_de_espera,cola_de_pagar,x,cedula,ventana):
    ventana.withdraw()
    consultar = Tk()
    consultar.geometry('1280x720')
    if cliente ('verificar')==False:
        pare = Label(consultar,text='Mantenimiento',font = ("Serif", 30))
        pare.pack()
        return consultarCanasta(cola_de_espera,cola_de_pagar,x,cedula,consultar)
    else:
        h = Label(consultar,text='indique el codigo de MARCA que desea consultar: ')
        h.pack()
        entrada = Entry(consultar)
        entrada.pack()
        buscar = Button(consultar,text='buscar',command= lambda: consultarCanasta_aux(entrada.get(),consultar,x,cedula))
        buscar.pack()
        l = Label(consultar, text='La lista de productos con precios: ')
        l.pack()
        
        def myfunction(event):
            canvas.configure(scrollregion=canvas.bbox("all"))
        
        myframe=Frame(consultar,relief=GROOVE,width=50,height=100,bd=1)
        myframe.place(x=450,y=100)

        canvas=Canvas(myframe)
        frame=Frame(canvas)
        myscrollbar=Scrollbar(myframe,orient="vertical",command=canvas.yview)
        canvas.configure(yscrollcommand=myscrollbar.set)

        myscrollbar.pack(side="right",fill="y")
        canvas.pack(side="left")
        canvas.create_window((0,0),window=frame,anchor='nw')
        frame.bind("<Configure>",myfunction)
        
        listaNueva = lista_marcas
        cont = 1
        for i in range (len(listaNueva)):
            Label(frame,text=(str(cont) + ". " +"Codigo de marca:"+listaNueva[i][2]+"||"+ "Producto: " + listaNueva[i][3] + " | Precio: " + listaNueva[i][5])).grid(row=i,column=1)
            cont += 1

def consultarCanasta_aux(Input,ventana,x,cedula):
    consultar = ventana
    listaNueva = lista_inventario
    indice = buscarMarca(Input)
    volver = Button(consultar,text='volver',bg = 'Black',fg = 'White',font = ("Serif", 15),command = lambda: menu(x,cedula,consultar)).place(x=0,y=0)
    if indice > -1:
        if listaNueva[indice][5] == '1':
            l = Label(consultar, text=('El producto '+listaNueva[indice][3]+' pertenece a la canasta basica.'),fg='Red').place(x=100,y=250)
        else:
            l = Label(consultar, text=('El producto: '+listaNueva[indice][3]+' no pertenece a la canasta basica.'),fg='Red').place(x=100,y=250)
    else:
        k = Label(consultar,text='ERROR: la marca que busca no existe.',fg='Black').place(x=100,y=250)
    

def buscarMarca(codigo):
    listaNueva = lista_marcas
    for i in range(len(listaNueva)):
        if str(codigo) == listaNueva[i][2]:
            return i
    return -1
##        if cliente ('verificar')==False:
##            return consultarCanasta(cola_de_espera,cola_de_pagar,x,cedula)
##        else:
##            print("\n")
##            listaNueva = lista_inventario
##            cont = 1
##            for i in range (0,len(listaNueva)):
##                print ("\n" + str(cont) + ". " + "codigo de marca: "+listaNueva[i][2]+"||"+ "Producto: " + listaNueva[i][3])
##                cont += 1
##            prod = input ("\n" + "Por favor ingrese el codigo de marca del producto que quiere consultar y presione ENTER --> ")
##            for i in range (0,len(listaNueva)):
##                if prod == listaNueva[i][2]:
##                    if listaNueva[i][5] == str(0):
##                        print ("\n" + "el producto " + listaNueva[i][3] + " no es parte de la canasta basica.")
##                        print("\n")
##                    else:
##                        print ("\n" + "el producto " + listaNueva[i][3] + " si es parte de la canasta basica.")
##                        print("\n")
##                    break
##            return menu(x,cedula)


#3
def consultarImpuesto(cola_de_espera,cola_de_pagar,x,cedula,ventana3):
    ventana3.withdraw()
    consultar = Tk()
    consultar.geometry('1280x720')
    if cliente ('verificar')==False:
        pare = Label(consultar,text='Mantenimiento',font = ("Serif", 30))
        pare.pack()
        return consultarImpuesto(cola_de_espera,cola_de_pagar,x,cedula,consultar)
    else:
        h = Label(consultar,text='indique el codigo de Marca que desea consultar: ')
        h.pack()
        entrada = Entry(consultar)
        entrada.pack()
        buscar = Button(consultar,text='buscar',command= lambda: consultarImpuesto_aux(entrada.get(),consultar,x,cedula))
        buscar.pack()
        l = Label(consultar, text='La lista de productos con precios: ')
        l.pack()

        def myfunction(event):
            canvas.configure(scrollregion=canvas.bbox("all"))
        
        myframe=Frame(consultar,relief=GROOVE,width=50,height=100,bd=1)
        myframe.place(x=450,y=100)

        canvas=Canvas(myframe)
        frame=Frame(canvas)
        myscrollbar=Scrollbar(myframe,orient="vertical",command=canvas.yview)
        canvas.configure(yscrollcommand=myscrollbar.set)

        myscrollbar.pack(side="right",fill="y")
        canvas.pack(side="left")
        canvas.create_window((0,0),window=frame,anchor='nw')
        frame.bind("<Configure>",myfunction)
        
        listaNueva = lista_marcas
        cont = 1
        for i in range (len(listaNueva)):
            Label(frame,text=(str(cont) + ". " +"Codigo de marca:"+listaNueva[i][2]+"||"+ "Producto: " + listaNueva[i][3] + " | Precio: " + listaNueva[i][5])).grid(row=i,column=1)
            cont += 1


    def consultarImpuesto_aux(Input,ventana,x,cedula):
        consultar = ventana
        listaNueva = lista_inventario
        indice = buscarMarca(Input)
        volver = Button(consultar,text='volver',command = lambda: menu(x,cedula,consultar)).place(x=0,y=0)
        if indice > -1:
            if listaNueva[indice][5] == '1':
                l = Label(consultar, text=('El producto '+listaNueva[indice][3]+' tiene un impuesto de: 1'),fg='Red').place(x=100,y=250)
            else:
                l = Label(consultar, text=('El producto: '+listaNueva[indice][3]+' tiene un impuesto de: 0'),fg='Red').place(x=100,y=250)
        else:
            k = Label(consultar,text='ERROR: la marca que busca no existe.',fg='Black').place(x=100,y=250)
        

##def consultarCanasta1(cola_de_espera,cola_de_pagar,x,cedula):
##    if cliente ('verificar')==False:
##        return consultarCanasta1(cola_de_espera,cola_de_pagar,x,cedula)
##    else:
##        print("\n")
##        global impuestoCanasta0
##        global impuestoCanasta1
##        listaNueva = lista_inventario
##        cont = 1
##        for i in range (0,len(listaNueva)):
##            print ("\n" + str(cont) + ". " + "Codigo de marca: "+listaNueva[i][2]+"||"+"Producto: " + listaNueva[i][3])
##            cont += 1
##        prod = input ("\n" + "Por favor ingrese el codigo de marca del producto que quiera consultar y presione ENTER --> ")
##        for i in range (0,len(listaNueva)):
##            if prod == listaNueva[i][2]:
##                if listaNueva[i][5] == str(0):
##                    print ("\n" + "el producto " + listaNueva[i][3] + " tiene un porcentaje de impuesto " + str(impuestoCanasta0))
##                else:
##                    print ("\n" + "el producto " + listaNueva[i][3] + " tiene un porcentaje de impuesto " + str(impuestoCanasta1))
##                break
##        return menu(x,cedula)

#4

def consultarPrecio(cola_de_espera,cola_de_pagar,x,cedula,ventana3):
    ventana3.withdraw()
    consultar = Tk()
    consultar.geometry('1280x720')
    if cliente ('verificar')==False:
        pare = Label(consultar,text='Mantenimiento',font = ("Serif", 30))
        pare.pack()
        return consultarPrecio(cola_de_espera,cola_de_pagar,x,cedula,consultar)
    h = Label(consultar,text='indique el codigo de marca del producto que desea consultar: ')
    h.pack()
    entrada = Entry(consultar)
    entrada.pack()
    buscar = Button(consultar,text='buscar',command= lambda: consultarPrecio_aux(entrada.get(),consultar,x,cedula))
    buscar.pack()

    def myfunction(event):
            canvas.configure(scrollregion=canvas.bbox("all"))
        
    myframe=Frame(consultar,relief=GROOVE,width=50,height=100,bd=1)
    myframe.place(x=450,y=100)

    canvas=Canvas(myframe)
    frame=Frame(canvas)
    myscrollbar=Scrollbar(myframe,orient="vertical",command=canvas.yview)
    canvas.configure(yscrollcommand=myscrollbar.set)

    myscrollbar.pack(side="right",fill="y")
    canvas.pack(side="left")
    canvas.create_window((0,0),window=frame,anchor='nw')
    frame.bind("<Configure>",myfunction)
    
    listaNueva = lista_marcas
    cont = 1
    for i in range (len(listaNueva)):
        Label(frame,text=(str(cont) + ". " +"Codigo de marca:"+listaNueva[i][2]+"||"+ "Producto: " + listaNueva[i][3])).grid(row=i,column=1)
        cont += 1

def consultarPrecio_aux(Input,ventana,x,cedula):
    consultar = ventana
    listaNueva = lista_marcas
    indice = buscarMarca(Input)
    volver = Button(consultar,text='volver',command = lambda: menu(x,cedula,consultar)).place(x=0,y=0)
    if indice > -1:
        l = Label(consultar, text='El codigo de marca: '+listaNueva[indice][2]+'||'+ 'Tipo: '+listaNueva[indice][3]+'||'+' tiene un precio de: ',bg="Red").place(x=0,y=220)
        A = Label(consultar,text=listaNueva[indice][5],bg="Blue").place(x=0,y=250)
    else:
        k = Label(consultar,text='ERROR: la marca que busca no existe.--------',bg='Red').place(x=100,y=220)
        m = Label(consultar,text='ERROR: la marca que busca no existe.--------',bg='Blue').place(x=100,y=250)
        
    
            
##def consultarPrecio(cola_de_espera,cola_de_pagar,x,cedula):
##    if cliente ('verificar')==False:
##        return consultarPrecio(cola_de_espera,cola_de_pagar,x,cedula)
##    else:
##        print("\n")
##        listaNueva = lista_marcas
##        prod = input ("\n" + "Por favor ingrese el codigo de marca del producto que quiera consultar (Si no lo sabe, consulte la lista completa): ")
##        for i in range (0,len(listaNueva)):
##            if prod == listaNueva[i][2]:
##                print ("\n" + "El precio del producto " + listaNueva[i][3] + " tiene un precio de " + listaNueva[i][5])
##                break
##        return menu(x,cedula)
##    






def mostrar_pasillos(cola_de_espera,cola_de_pagar,cedula,ventana3):
    if cliente ('verificar')==False:
        pare = Label(ventana3,text='Mantenimiento',font = ("Serif", 30))
        pare.pack()
        return menu(0,cedula,ventana3)
    else:
        if cliente('5')==True:
            ventana3.withdraw()
            consultar = Tk()
            consultar.geometry('1280x720')
            listaNueva = lista_pasillos
            h = Label(consultar,text='INDIQUE EL CODIGO DE PASILLO DEL PRODUCTO QUE DESEA COMPRAR: ')
            h.pack()
            entrada = Entry(consultar)
            entrada.pack()
            buscar = Button(consultar,text='-->',command= lambda: mostrar_productos(entrada.get(),cola_de_espera,cola_de_pagar,cedula,consultar))
            buscar.pack()
            l = Label(consultar, text='La lista de Pasillos: ',fg='Cyan',bg='Black')
            l.pack()

            def myfunction(event):
                canvas.configure(scrollregion=canvas.bbox("all"))
            
            myframe=Frame(consultar,relief=GROOVE,width=50,height=100,bd=1)
            myframe.place(x=450,y=100)

            canvas=Canvas(myframe)
            frame=Frame(canvas)
            myscrollbar=Scrollbar(myframe,orient="vertical",command=canvas.yview)
            canvas.configure(yscrollcommand=myscrollbar.set)

            myscrollbar.pack(side="right",fill="y")
            canvas.pack(side="left")
            canvas.create_window((0,0),window=frame,anchor='nw')
            frame.bind("<Configure>",myfunction)
            
            listaNueva = lista_pasillos
            for i in range (len(listaNueva)):
                listaNueva[i] = listaNueva[i].split(';')
                if listaNueva[i][0] != '00':
                    Label(frame,text=(". " +"Codigo de pasillo:"+listaNueva[i][0]+"||"+ "Nombre: " + listaNueva[i][1])).grid(row=i,column=1)
            
        
##    else:
##        print("\n")
##        listaNueva = lista_pasillos
##        i=0
##        while(i<=len(listaNueva)-1):
##            print("Pasillo:",listaNueva[i][0],"||","Tipo:",listaNueva[i][1])
##            i+=1
##        i=0
##        print("\n")
##        opcion = input("Ingrese el PASILLO al que desea ir---->")
##        print("\n")
##        while(i<=len(listaNueva)-1):
##            if opcion == listaNueva[i][0]:
##                return mostrar_productos(opcion,cola_de_espera,cola_de_pagar,cedula)
##            i+=1
##        print("\n")
##        print("*"*27)
##        print("*Ingrese una opción valida*")
##        print("*"*27)
##        print("\n")
##        return mostrar_pasillos(cola_de_espera,cola_de_pagar,cedula)

  
#2
            
def mostrar_productos(opcion,cola_de_espera,cola_de_pagar,cedula,ventana):
    var = 0
    for i in range(0,len(lista_pasillos)):
        if opcion ==  lista_pasillos[i][0]:
            ventana.withdraw()
            consultar = Tk()
            consultar.geometry("1280x720")
            if cliente ('verificar')==False:
                pare = Label(consultar,text='Mantenimiento',font = ("Serif", 30))
                pare.pack()
                return mostrar_productos(opcion,cola_de_espera,cola_de_pagar,cedula,consultar)
            else:
                h = Label(consultar,text='indique el codigo de Producto que desea Comprar: ')
                h.pack()
                entrada = Entry(consultar)
                entrada.pack()
                buscar = Button(consultar,text='---->',command= lambda:mostrar_marcas(entrada.get(),cola_de_espera,cola_de_pagar,cedula,consultar,opcion))#listaNueva[i][2]tipo
                buscar.pack()

                def myfunction(event):
                    canvas.configure(scrollregion=canvas.bbox("all"))
        
                myframe=Frame(consultar,relief=GROOVE,width=50,height=100,bd=1)
                myframe.place(x=450,y=100)

                canvas=Canvas(myframe)
                frame=Frame(canvas)
                myscrollbar=Scrollbar(myframe,orient="vertical",command=canvas.yview)
                canvas.configure(yscrollcommand=myscrollbar.set)

                myscrollbar.pack(side="right",fill="y")
                canvas.pack(side="left")
                canvas.create_window((0,0),window=frame,anchor='nw')
                frame.bind("<Configure>",myfunction)
                
                var = 1
                listaNueva = lista_productos
                for i in range(0,len(listaNueva)):
                    if opcion==listaNueva[i][0]:
                        Label(frame,text=("Pasillo:"+listaNueva[i][0]+"||"+"Codigo del Producto:"+listaNueva[i][1]+"||"+"Tipo:"+listaNueva[i][2])).grid(row=i,column=1)
                        
    if var == 0:
        return mostrar_pasillos(cola_de_espera,cola_de_pagar,cedula,ventana)
    
        
    
    
        


def mostrar_marcas(opcion2,cola_de_espera,cola_de_pagar,cedula,ventana,opcion):
    var = 0
    for i in range(0,len(lista_productos)):
        if opcion == lista_productos[i][0] and opcion2 == lista_productos[i][1]:
            tipo = lista_productos[i][2]
            ventana.withdraw()
            consultar = Tk()
            consultar.geometry("1280x720")
            if cliente ('verificar')==False:
                pare = Label(consultar,text='Mantenimiento',font = ("Serif", 30))
                pare.pack()
                return mostrar_marcas(opcion2,cola_de_espera,cola_de_pagar,cedula,consultar,opcion)
            else:
                h = Label(consultar,text='indique el codigo de Marca del producto que desea Comprar: ')
                h.pack()
                entrada = Entry(consultar)
                entrada.pack()
                h = Label(consultar,text='indique la CANTIDAD que desea Comprar: ')
                h.pack()
                entrada2 = Entry(consultar)
                entrada2.pack()
                buscar = Button(consultar,text='---->',command= lambda:meter(entrada.get(),entrada2.get(),cola_de_espera,cola_de_pagar,cedula,consultar,tipo,opcion,opcion2))#listaNueva[i][2]tipo
                buscar.pack()

                def myfunction(event):
                    canvas.configure(scrollregion=canvas.bbox("all"),width=600,height=200)
        
                myframe=Frame(consultar,relief=GROOVE,width=50,height=100,bd=1)
                myframe.place(x=350,y=110)

                canvas=Canvas(myframe)
                frame=Frame(canvas)
                myscrollbar=Scrollbar(myframe,orient="vertical",command=canvas.yview)
                canvas.configure(yscrollcommand=myscrollbar.set)

                myscrollbar.pack(side="right",fill="y")
                canvas.pack(side="left")
                canvas.create_window((0,0),window=frame,anchor='nw')
                frame.bind("<Configure>",myfunction)
                
                global lista_marcas
                listaNueva = lista_marcas
                var =1
                for i in range(0,len(listaNueva)):
                    if opcion2==listaNueva[i][1]:
                        Label(frame,text=("Pasillo:"+listaNueva[i][0]+"||"+"Codigo del Producto:"+listaNueva[i][1]+"||"+"Código de marca:"+listaNueva[i][2]+"||"+"Marca:"+listaNueva[i][3]+"||"+"Cantidad de Gondola:"+listaNueva[i][4]+"||"+"Precio: "+listaNueva[i][5]+"$")+str(i)).grid(row=i,column=1)

    if var == 0:
        return mostrar_pasillos(cola_de_espera,cola_de_pagar,cedula,ventana)
    
    
       

def meter(opcion4,cantidad,cola_de_espera,cola_de_pagar,cedula,ventana,tipo,opcion,opcion2):
    if cantidad=='':
        return mostrar_pasillos(cola_de_espera,cola_de_pagar,cedula,ventana)
    else:
        global lista_marcas
        listaNueva = lista_marcas
        res = 0
        lis =[]
        lis2 =[]
        for i in range(0,len(listaNueva)):
            if opcion4 == lista_marcas[i][2] and opcion == lista_marcas[i][0] and opcion2 == lista_marcas[i][1]:
                ventana.withdraw()
                consultar = Tk()
                consultar.geometry("1280x720")
                if cliente ('verificar')==False:
                    pare = Label(consultar,text='Mantenimiento',font = ("Serif", 30))
                    pare.pack()
                    return  meter(opcion4,cantidad,cola_de_espera,cola_de_pagar,cedula,consultar,tipo)
                else:
                    if int(listaNueva[i][4])>0 and (int(cantidad) <= int(listaNueva[i][4])-2) and (int(cantidad) != 0) :
                        res = int(listaNueva[i][4])-int(cantidad)
                        lis+=[listaNueva[i][0]]+[listaNueva[i][1]]+[listaNueva[i][2]]+[tipo]+[listaNueva[i][3]]+[str(cantidad)]+[listaNueva[i][5]]
                        lis2+=[[listaNueva[i][0]]+[listaNueva[i][1]]+[listaNueva[i][2]]+[listaNueva[i][3]]+[str(res)]+[listaNueva[i][5]]]
                    else:
                        return mostrar_pasillos(cola_de_espera,cola_de_pagar,cedula,consultar)
            else:
                lis2+=[[listaNueva[i][0]]+[listaNueva[i][1]]+[listaNueva[i][2]]+[listaNueva[i][3]]+[listaNueva[i][4]]+[listaNueva[i][5]]]
              
        if lis==[]:
            return mostrar_pasillos(cola_de_espera,cola_de_pagar,cedula,ventana)
        else:
            lista_marcas = lis2
            cola_de_espera+=[lis]
            lis= []
            h = Label(consultar,text="Desea realizar otra compra?")
            h.pack()
            si = Button(consultar,text="SI",command=lambda:mostrar_pasillos(cola_de_espera,cola_de_pagar,cedula,consultar))
            si.pack()
            no = Button(consultar,text="NO",command=lambda:landing(opcion4,cantidad,cola_de_espera,cola_de_pagar,cedula,consultar,tipo))
            no.pack()

def landing (opcion4,cantidad,cola_de_espera,cola_de_pagar,cedula,ventana,tipo):
    ventana.withdraw()
    consultar = Tk()
    consultar.geometry("700x700")
    l = Label(consultar, text= 'Desea eliminar un producto de su canasta antes de pasar a la caja?')
    l.pack()
    si = Button(consultar,text="SI",command=lambda:eliminar_producto(opcion4,cantidad,cola_de_espera,cola_de_pagar,cedula,ventana,tipo))
    si.pack()
    no = Button(consultar,text="NO",command=lambda:meter_aux(opcion4,cantidad,cola_de_espera,cola_de_pagar,cedula,consultar,tipo))
    no.pack()
def eliminar_producto(opcion4,cantidad,cola_de_espera,cola_de_pagar,cedula,ventana,tipo):
    ventana.withdraw()
    consultar = Tk()
    consultar.geometry("700x700")
    l = Label(consultar,text= 'Ingrese el codigo de marca del producto que desea eliminar')
    l.pack()
    resp = Entry(consultar)
    resp.pack()
    eliminar = Button(consultar,text='eliminar',command=lambda:eliminar_producto_aux(opcion4,cantidad,cola_de_espera,cola_de_pagar,cedula,ventana,tipo,str(resp.get())))
    eliminar.pack()
    volver = Button(consultar,text='volver al menu',command = lambda: menu(x,cedula,consultar))
    volver.pack()
def eliminar_producto_aux(opcion4,cantidad,cola_de_espera,cola_de_pagar,cedula,ventana,tipo,respuesta):
    ventana.withdraw()
    consultar = Tk()
    consultar.geometry("700x700")
    if respuesta.isdigit():
        for i in range(len(cola_de_espera)):
            if respuesta == cola_de_espera[i][2]:
                del cola_de_espera[i]
                break
        l = Label(consultar, text = 'El producto se ha eliminado. Desea eliminar otro producto?')
        l.pack()
        si = Button(consultar,text="SI",command=lambda:eliminar_producto(opcion4,cantidad,cola_de_espera,cola_de_pagar,cedula,ventana,tipo))
        si.pack()
        no = Button(consultar,text="NO, PASAR A CAJA",command=lambda:meter_aux(opcion4,cantidad,cola_de_espera,cola_de_pagar,cedula,consultar,tipo))
        no.pack()
    else:
        l = Label(consultar,text='Debe ingresar una respuesta valida.')
        l.pack()
        volver = Button(consultar,text='volver al menu',command = lambda: menu(x,cedula,consultar)).place(x=0,y=0)
        volver.pack()
        

def meter_aux(opcion4,cantidad,cola_de_espera,cola_de_pagar,cedula,ventana,tipo):
    ventana.withdraw()
    consultar = Tk()
    consultar.geometry("700x700")
    cola_de_espera[:0]+=[cedula]
    cola_de_pagar+=[cola_de_espera]
    h = Label(consultar,text = "LISTA ACTUAL : "+str(cola_de_espera))
    h.pack()
    cola_de_espera = []
    i=0
    string=''
    while(i<=len(cola_de_pagar)-1):
        j=0
        while(j<=len(cola_de_pagar[0])-1):
            if j==0:
                string+=cola_de_pagar[i][j]+'-'
            else:
                string+=';'.join(cola_de_pagar[i][j])+'-'
            j+=1
        i+=1
    cola_de_pagar = []
    global cedula_vieja
    if cliente("factura")==True:
        texto = ".txt"
        global todo1
        todo1 = todo1.split("#")
        f = open(cedula_vieja+"USUARIO"+texto,"w")
        f.write(todo1[0])
        f.close()
        global impuestoCanasta1 
        global impuestoCanasta0
        impuestoCanasta1 = todo1[1]
        impuestoCanasta0 = todo1[2]
        cedula_vieja = cedula
        if cliente('5')==True:
            return cliente('00'+string)
    else:
        if cliente('5')==True:
            return cliente('00'+string)

def ver_factura(x,cedula,ventana3):
    global factura
    if cliente('10')==True:
        ventana3.withdraw()
        ventana = Toplevel(ventana3)
        ventana.configure(bg="white")
        ventana.geometry("1280x720")
        h = Label(ventana, text = factura,bg="White", fg = 'Black',font = ("Serif", 13)).place(x=0,y=0)
        factura = ''
        l = Button(ventana,text = "SALIR",command=lambda:menu(x,cedula,ventana))
        l.pack()
        ventana.mainloop()
    
    
    
    
###############################################################################################
#______________________________________________________________________________________________
#*(*(*(*(**((*
    

def recibir(string):
    global todo
    todo = string
    string = string.split('+')
    global lista_ciudades 
    global lista_clientes 
    global lista_inventario 
    global lista_marcas 
    global lista_pasillos 
    global lista_productos
    lista_ciudades = desparsear(string[0])
    lista_clientes = desparsear(string[1])
    lista_inventario = desparsear(string[2])
    lista_marcas = desparsear(string[3])
    lista_pasillos = desparsear(string[4])
    lista_productos = desparsear(string[5])
    return menu_inicial(lista_clientes)
        
        
        
def desparsear(string):
    string = string.split('-')
    for i in range(0,len(string)):
        string[i] = string[i].split(';')
    return string



##def validar_cliente(lista):
##    if cliente ('verificar')==False:
##        return validar_cliente(lista)
##    else:
##        try:
##            cedula = int(input("ingrese su cedula---->"))
##            i = 0
##            while(i<=len(lista)-1):
##                if str(cedula) == lista[i][0]:
##                    return menu(0,lista[i][0])
##                else:
##                    i+=1
##            print("Usted no es un usuario del mercado")
##            print("\n")
##            return menu(1,'')
##        except ValueError:
##            print("ingrese un valor entero")
##            return validar_cliente(lista)

#___________________INTERFAZ_________________________

def menu_inicial(lista_clientes):#Menu con el ranking y iniciar juego
    ventana = Tk()
    ventana.configure(bg="white")
    ventana.geometry("600x600")
    titulo = Label(ventana, text = "SUPERMERCADO SANCHEZE",bg="White", fg = 'Black',font = ("Serif", 30)).place(x=10,y=10)
    Boton_I = Button(ventana,text = "INGRESAR A COMPRAR",font = ("Serif", 15),bg = "White",height="2",width="20",command=lambda:validar_2(ventana,lista_clientes)).place(x=160,y=300)
    ventana.mainloop()

def validar_2(ventana,lista_clientes):
    ventana.withdraw()
    ventana2 = Toplevel(ventana)
    ventana2.geometry("700x700")
    ventana2.configure(bg = "Black")
    titulo = Label(ventana2, text = "INGRESE LA CEDULA",bg="Black", fg = 'White',font = ("Serif", 15)).place(x=10,y=10)
    cedula = Entry(ventana2,width=63,bg="white")
    cedula.place(x=10,y=40)
    boton2 = Button(ventana2, text = "Entrar" , bg="White", fg = 'Black',font = ("Serif", 15),command=lambda:validar_cliente(ventana2,lista_clientes,cedula.get())).place(x=20,y=200)
    ventana2.mainloop()

def validar_cliente(ventana2,lista_clientes,entrada):
    if entrada=='':
        return menu(1,'ffffffff',ventana2)
    else:
        if cliente ('verificar')==False:
            ventana2.withdraw()
            ventana3 = Toplevel(ventana2)
            ventana3.geometry("100x100")
            ventana3.configure(bg = "Black")
            titulo = Label(ventana3, text = "MANTENIMIENTO",bg="Black", fg = 'White',font = ("Serif", 15)).place(x=10,y=10)
            return validar_cliente(ventana3,lista_clientes,entrada)
        else:
            i = 0
            while(i<=len(lista_clientes)-1):
                if entrada == lista_clientes[i][0]:
                    return menu(0,lista_clientes[i][0],ventana2)
                else:
                    i+=1
            return menu(1,'ffffffff',ventana2)
        
                        


#____________________________________________________
def reporteP(x,cedula,ventana3):
    ventana3 = ventana3
    ventana3.withdraw()
    reporteInicio = Tk()
    reporteInicio.geometry('1280x720')
    l = Label(reporteInicio,text='Para algunos reportes se requiere de informacion adicional.')
    l.pack(side=TOP)
    for i in range(2):
        campo = Label(reporteInicio,text='')
        campo.pack()
    h = Label(reporteInicio,text='Para marcas de un producto: ')
    h.pack()
    for i in range(2):
        campo = Label(reporteInicio,text='')
        campo.pack()
    a = Label(reporteInicio,text='Ingrese el codigo del pasillo: ')
    a.pack()
    pasillo = Entry(reporteInicio)
    pasillo.pack()
    b = Label(reporteInicio,text='Ingrese el codigo de producto: ')
    b.pack()
    producto = Entry(reporteInicio)
    producto.pack()
    for i in range(2):
        campo = Label(reporteInicio,text='')
        campo.pack()
    siguiente = Button(reporteInicio,text='siguiente',command = lambda: reporteP_aux(x,cedula,reporteInicio,str(pasillo.get()),str(producto.get())))
    siguiente.pack()
    volver = Button(reporteInicio,text='volver al menu',command = lambda: menu(x,cedula,reporteInicio))
    volver.pack()
def reporteP_aux(x,cedula,ventana,pasillo1,producto):
    reporteInicio = ventana
    reporteInicio.withdraw()
    reporte1 = Tk()
    reporte1.geometry('1280x720')
    if verificarInputReporte(pasillo1,producto):
        listaMarcas = lista_marcas
        var = '\n'
        for i in range(len(listaMarcas)):
            if listaMarcas[i][0] == pasillo1:
                if listaMarcas[i][1] == producto:
                    var += listaMarcas[i][3]
                    var += '\n'
        if var == '\n':
            var = 'No hay marcas'
        h = Label(reporte1,text='Para productos de un pasillo: ')
        h.pack()
        for i in range(2):
            campo = Label(reporte1,text='')
            campo.pack()
        a = Label(reporte1,text='Ingrese el codigo del pasillo: ')
        a.pack()
        pasillo = Entry(reporte1)
        pasillo.pack()
        for i in range(2):
            campo = Label(reporte1,text='')
            campo.pack()
        siguiente = Button(reporte1,text='siguiente',command = lambda: reporteP_aux1(x,cedula,reporte1,pasillo1,producto,str(pasillo.get()),var))
        siguiente.pack()
        volver = Button(reporte1,text='volver al menu',command = lambda: menu(x,cedula,reporte1))
        volver.pack()
    else:
        l = Label(reporte1,text='Los valores ingresados son incorretos o no coinciden entre ellos.')
        l.pack()
        volver = Button(reporte1,text='volver al menu',command = lambda: menu(x,cedula,reporte1))
        volver.pack()
def reporteP_aux1(x,cedula,ventana,pasillo1,producto,pasillo2,respuesta1):
    reporte1 = ventana
    reporte1.withdraw()
    reporte2 = Tk()
    reporte2.geometry('1280x720')
    if verificarInputReporte(pasillo2,''):
        listaProductos = lista_productos
        var = '\n'
        for i in range(len(listaProductos)):
            if listaProductos[i][0] == pasillo2:
                var += listaProductos[i][2]
                var += '\n'
        if var == '\n':
            var = 'No hay productos'
        l = Label(reporte2,text='Sus respuestas se han guardado. Por favor confirme para completar la factura.')
        l.pack(side=TOP)
        confirmar = Button(reporte2,text='confirmar',command = lambda: reporteFinal(x,cedula,ventana,respuesta1,var))
        confirmar.pack()
        volver = Button(reporte2,text='volver al menu',command = lambda: menu(x,cedula,reporte2))
        volver.pack()
    else:
        l = Label(reporte2,text='Los valores ingresados son incorretos o no coinciden entre ellos.')
        l.pack()
        volver = Button(reporte2,text='volver al menu',command = lambda: menu(x,cedula,reporte2))
        volver.pack()
def verificarInputReporte(pasillo,producto):
    global lista_pasillos
    global lista_productos
    listaPasillos = lista_pasillos
    listaProductos = lista_productos
    var = ''
    if producto == '':
        for i in range(len(listaPasillos)):
            if listaPasillos[i][0] == pasillo:
                var += '1'
        if var == '':
            return False
        else:
            return True
    else:
        for i in range(len(listaPasillos)):
            if listaPasillos[i][0] == pasillo:
                var += '1'
        if var == '':
            var += '0'
        for i in range(len(listaProductos)):
            if listaProductos[i][1] == producto:
                var += '1'
        if len(var) == 1:
            var += '0'
        if var == '11':
            return True
        else:
            return False

def reporteFinal(x,cedula,ventana,respuesta1,respuesta2):
    ventanaAnte = ventana
    ventanaAnte.withdraw()
    vReporte = Tk()
    vReporte.geometry('1280x720')

    def myfunction(event):
        canvas.configure(scrollregion=canvas.bbox("all"))
        
    myframe=Frame(vReporte,relief=GROOVE,width=10,height=100,bd=1)
    myframe.place(x=800,y=400)

    canvas=Canvas(myframe)
    frame=Frame(canvas)
    myscrollbar=Scrollbar(myframe,orient="vertical",command=canvas.yview)
    canvas.configure(yscrollcommand=myscrollbar.set)

    myscrollbar.pack(side="right",fill="y")
    canvas.pack(side="left")
    canvas.create_window((0,0),window=frame,anchor='nw')
    frame.bind("<Configure>",myfunction)
    
    listaImpresion = ['*********************************************','','-----------SUPER MERCADO SANCHEZE------------','','-------------------REPORTE--------------------','','']
    for i in range(7):
        if listaImpresion[i] == '':
            l = Label(vReporte,text='')
            l.pack()
        else:
            l = Label(vReporte,text=listaImpresion[i])
            l.pack()
    for i in range(2):
        campo = Label(vReporte,text='')
        campo.pack()
    h = Label(vReporte,text='Marcas de un producto son: '+respuesta1)
    h.pack()
    for i in range(2):
        campo = Label(vReporte,text='')
        campo.pack()
    k = Label(vReporte,text='Productos de un pasillo son: '+respuesta2)
    k.pack()
    for i in range(2):
        campo = Label(vReporte,text='')
        campo.pack()
    j = Label(vReporte,text='Pasillos del supermercado: ')
    j.pack()
    listaPasillos = lista_pasillos
    for i in range(len(listaPasillos)):
        Label(frame,text=(str(listaPasillos[i]))).grid(row=i,column=1)
        #p = Label(vReporte,text=str(listaPasillos[i]))
        #p.pack()
    for i in range(2):
        campo = Label(vReporte,text='')
        campo.pack()
    o = Label(vReporte,text='*********************************************')
    o.pack()
    f = open("REPORTES_USUARIO.txt","w")
    f.write("*********************************************")
    f.write("\n")
    f.write("-----------SUPER MERCADO SANCHEZE------------")
    f.write("\n")
    f.write("-------------------REPORTE--------------------")
    f.write("\n")
    f.write("\n")
    f.write("Marcas de un producto son: ")
    f.write(respuesta1)
    f.write("\n")
    f.write("\n")
    f.write("Productos de un pasillo son: ")
    f.write(respuesta2)
    f.write("\n")
    f.write("\n")
    f.write("Pasillos del supermercado:")
    listaPasillos = lista_pasillos
    for i in range(len(listaPasillos)):
        f.write('\n' + listaPasillos[i][0] + ', ' + listaPasillos[i][1])
    f.write("\n")
    f.write("\n")
    f.write("*********************************************")
    f.close()
    volver = Button(vReporte,text='volver al menu',command = lambda: menu(x,cedula,vReporte))
    volver.pack()

##def reporte(x,cedula):
##    f = open("REPORTES_USUARIO.txt","w")
##    f.write("*********************************************")
##    f.write("\n")
##    f.write("-----------SUPER MERCADO SANCHEZE------------")
##    f.write("\n")
##    f.write("-------------------REPORTE--------------------")
##    f.write("\n")
##    f.write("\n")
##    f.write("Marcas de un producto: Son las ")
##    f.write(repor_6())
##    f.write("\n")
##    f.write("\n")
##    f.write("Productos de un pasillo: son los ")
##    f.write(repor_4())
##    f.write("\n")
##    f.write("\n")
##    f.write("Pasillos del supermercado:")
##    global lista_pasillos
##    f.write(str(lista_pasillos))
##    f.write("\n")
##    f.write("\n")
##    f.write("*********************************************")
##    f.close()
##    return menu(x,cedula)
##
##
##
##def repor_6():
##    print("\n")
##    print("•Marcas de un producto: Indica el pasillo, indica el producto pasillo, imprime todas las marcas de un producto")
##    op1=int(input("ingrese un pasillo---->"))
##    op2=int(input("ingrese codigo producto pasillo---->"))
##    global lista_marcas
##    marcas = lista_marcas
##    i=0
##    var=''
##    while(i<=len(marcas)-1):
##        if int(marcas[i][0])==op1:
##            if int(marcas[i][1])==op2:
##                var += marcas[i][3]
##                var+=";"
##        i+=1
##    if len(var)==0:
##        var = "No hay marcas"
##        return var
##    else:
##        return var
##
##
##
##def repor_4():
##    print("\n")
##    print("número de ese pasillo, se imprimen todos los productos del pasillo")
##    op1=int(input("ingrese un pasillo---->"))
##    global lista_productos
##    productos = lista_productos
##    i=0
##    var=''
##    while(i<=len(productos)-1):
##        if int(productos[i][0])==op1:
##            var += productos[i][2]
##            var+=";"
##        i+=1
##    if len(var)==0:
##        var = "No hay marcas"
##        return var
##    else:
##        return var


def parsear_Ciudades():
    global lista_ciudades
    lista = lista_ciudades
    for i in range(0,len(lista)):
        lista[i]=';'.join(lista[i])
    lista='-'.join(lista)
    return lista

def parsear_Clientes():
    global lista_clientes
    lista = lista_clientes
    for i in range(0,len(lista)):
        lista[i]=';'.join(lista[i])
    lista='-'.join(lista)
    return lista


def parsear_Inventario():
    global lista_inventario
    lista = lista_inventario
    for i in range(0,len(lista)):
        lista[i]=';'.join(lista[i])
    lista='-'.join(lista)
    return lista

def parsear_MarcasProductos():
    global lista_marcas
    lista = lista_marcas
    for i in range(0,len(lista)):
        lista[i]=';'.join(lista[i])
    lista='-'.join(lista)
    return lista

def parsear_Pasillos():
    global lista_pasillos
    lista = lista_pasillos
    for i in range(0,len(lista)):
        lista[i]=';'.join(lista[i])
    lista='-'.join(lista)
    return lista

def parsear_ProductosPasillos():
    global lista_productos
    lista = lista_productos
    for i in range(0,len(lista)):
        lista[i]=';'.join(lista[i])
    lista='-'.join(lista)
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
import time
#time.sleep(1)
def cliente (x):
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
            if data=='parado':
                for m in range(0,3):
                    time.sleep(1)
                    print("Modificando el server")
                return cliente('0')
            else:
                return recibir(data)
        elif x[0:2]=='00':
            data = x
            admi_socket.send(data.encode())
            data=admi_socket.recv(100000).decode()
            if data == '01':
                return cliente('01')
            elif data=='parado':
                for m in range(0,3):
                    time.sleep(1)
                    print("Modificando el server")
                return cliente(x)
            else:
                return cliente(x)
        elif x=='01':
            data = '01'
            admi_socket.send(data.encode())
            data=admi_socket.recv(100000).decode()
            if data=='parado':
                for m in range(0,3):
                    time.sleep(1)
                    print("Modificando el server")
                return cliente(x)
            else:
                return recibir(data)
        elif x=='verificar':
            data = 'verificando'
            admi_socket.send(data.encode())
            data=admi_socket.recv(100000).decode()
            if data=='parado':
                for m in range(0,3):
                    time.sleep(1)
                    print("Modificando el server")
                return False
            else:
                global todo
                todo = data
                data = data.split('+')
                global lista_ciudades 
                global lista_clientes 
                global lista_inventario 
                global lista_marcas 
                global lista_pasillos 
                global lista_productos
                lista_ciudades = desparsear(data[0])
                lista_clientes = desparsear(data[1])
                lista_inventario = desparsear(data[2])
                lista_marcas = desparsear(data[3])
                lista_pasillos = desparsear(data[4])
                lista_productos = desparsear(data[5])
                return True

        elif x=="factura":
            data = "factura"
            admi_socket.send(data.encode())
            data=admi_socket.recv(100000).decode()
            if data=="no":
                return False
            else:
                global todo1
                todo1 = data
                return True
        elif x=='5':
            data = "!"+parsear_todo()
            admi_socket.send(data.encode())
            data=admi_socket.recv(100000).decode()
            print(data)
            if data=="yeah":
                return True
        elif x == '10':
            data = '879'
            admi_socket.send(data.encode())
            data=admi_socket.recv(100000).decode()
            global factura
            factura = data
            return True
            
                
    cliente.close()


cliente('0')
    
    




