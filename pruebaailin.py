import tkinter   

 
#import 
#create a main window 
#Changing window properties 
#-title- size- 
#labels ()
#
ventana=tkinter.Tk()  
ventana.geometry("400x300")   
label=tkinter.Label(ventana,text="cajero", bg = "red")  
label.pack(fill=tkinter.BOTH, expand=True) 
ventana.mainloop()

