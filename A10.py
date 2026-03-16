#import tkinter
#from tkinter import * -para importar todo lo de la libreria

#ventana = tkinter.Tk() #contenedor de los elementos graficos
#ventana.geometry("300x300") #tamanio de ventana

#etiqueta = tkinter.Label(ventana, text = "hola mundo", bg = "blue")
#etiqueta.pack(side= tkinter.BOTTOM)#para poner texto en pantalla, () si no tiene ordenes siempre se mantendra en el centro, 
#(side = tkinter.BOTTOM) es abajo(RIGHT)es derecha
#etiqueta.pack(fill= tkinter.X)#para estirar, (fill= tkinter.X) es todo el ejeX,(fill= tkinter.Y, expand = True(or 1)) es para el ejeY vertical
#fill= tkinter.BOTH, expand = True(or 1) es toda la ventana
#def saludo ():
    #print("Hola")
    
#boton1 = tkinter.Button(ventana, text = "Presiona", padx = 40, pady = 50, comand = lambda: print("python"))#(en donde va estar, nombre ), (padx = 40, pady = 50) estirar ancho y largo
##(command =) llamar a la funcion sin parentesis en la funcion. #(comand = lambda: saludo() definir parametro
#boton1.pack()
#ventana.mainloop() #registro de todo

#cajaTexto = tkinter.Entry(ventana, font = "Helvetica 20" ) #introducir texto con teclado #tkinter.Entry(font = "Helvetica 50") funte y tamanio
#cajaTexto.pack()

#etiqueta = tkinter.Label(ventana)#despegar texto para etiqueta
#etiqueta.pack()

#def textodecaja():
 #   text2 = cajaTexto.get()
    #print(text2)
  #  etiqueta["text"] = text2
 
#boton1 = tkinter.Button(ventana, text = "click", command= textodecaja)
#boton1.pack()

#el metodo grot divide las ventanas en columnas y filas, Colum Row 0
#boton1 = tkinter.Button(ventana, text = "boton1", width = 20, height= 10)
#boton2 = tkinter.Button(ventana, text = "boton2")
#boton3 = tkinter.Button(ventana, text = "boton3")
#boton1.grid(row = 0, column = 0)#esquina superior
#boton1.grid(row = 1, column = 2)#centro
#ventana.mainloop() #registro de todo 

from tkinter import tk 
#wigets son bloques u elementos predifinidos
app = tk.Tk() #ventana principal de la aplicacion
palabra = tk.StrinVar(app)#guardar datos mapear a un widgetde la aplicacionasignar
entrada = tk.StringVar 
app.geometry("300x600")#dimensiones ancho x alto
app.configure(background = "black")#elegir color
tk.Wm.wm_title(app,"hola crack")#titulo

#def saludar():
 #   print("Hola")
def cambiode_palabre():
    palabra.set("Susurro" + entrada.get())#actualiza su valor
tk.Buttom(app,text = "Click me", font=("Coursier",14),bg = "blue", fg="white", command = cambiode_palabre, relief = "flat").pack(fill=tk.BOTH, expand = True)#saludar) #app es el widget donde se encrusta, (command =) requiere funcion
#pack empaquetar el boton dentro de la app, relief = "flat"sin borde, .get es para recuperar texto, command = lambda: print("hola" + entrada.get())
tk.Label(app, text = "etiqueta", textvariable = palabra , fg = "blue", bg = "white", justify = "center").pack(fill=tk.BOTH, expand = True)#contiene texto
tk.Entry(app, fg = "blue", bg = "white", justify = "center").pack(fill=tk.BOTH, expand = True, textvariable = entrada) #escribir texto dentro
app.mainloop() #actualiza la aplicacion