import tkinter  
ventana=tkinter.Tk()  
ventana.geometry("400x300")   
label=tkinter.Label(ventana,text="hola MUNDO", bg = "blue")  
label.pack(fill=tkinter.BOTH, expand=True) 

ventana.mainloop()

