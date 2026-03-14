import tkinter   

 
#import 
#create a main window 
#Changing window properties 
#-title- size- 
#labels ()
#
ventana=tkinter.Tk()  
ventana.geometry("1200x800")   
label=tkinter.Label(ventana,text="cajero", bg = "gray", font = ("Arial", 20))
label.place(x = 100, y = 50)
label.pack(fill=tkinter.BOTH, expand=True)
#ventana.pack(label)
ventana.mainloop()