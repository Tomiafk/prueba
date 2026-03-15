# Zona de comandos

# git init  =  iniciar programa
# git status  =  ver los status / sincronizacion
# git add  =  añadir archivo al repositorio
# git commit -m, "algo"  =  agregar al la nube de github con comentario
# git push  =  actualizar en la nube
# git pull = agarrar lo actualizado de la nube
# git revert  = revertir cambios de commit
import tkinter as tk

root = tk.Tk()

logo = tk.PhotoImage(file="tigre_logo.png")

label = tk.Label(root,image=logo)
label.pack()

root.mainloop()