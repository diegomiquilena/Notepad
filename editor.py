from tkinter import *
from tkinter import filedialog as FileDialog
from io import open

ruta = "" # La utilizaremos para almacenar la ruta de un fichero

def nuevo():
    global ruta
    mensaje.set("Nuevo fichero")
    ruta = ""
    texto.delete(1.0, "end")
    root.title("Mi Editor de Texto")

def abrir():
    global ruta
    mensaje.set("Abrir fichero")
    ruta = FileDialog.askopenfilename(initialdir='.', 
        filetype=(("Ficheros de texto", "*.txt"),),
        title="Abrir un fichero de texto")

    # Abrimos el condicional para que la ruta sea distinta a Nada, y ahí que nos abra el fichero.
    if ruta != "":
        fichero = open(ruta, 'r')
        contenido = fichero.read()
        texto.delete(1.0,"end")
        texto.insert("insert", contenido)
        fichero.close()
        root.title(ruta + " - Mi Editor de Texto")


def guardar():
    mensaje.set("Guardar fichero")
    if ruta != "":
        contenido = texto.get(1.0,'end-1c') # 'end-1c' es que recupere todo menos el último caracter.
        fichero = open(ruta, 'w+')
        fichero.write(contenido)
        fichero.close()
        mensaje.set("Fichero guardado correctamente.")

    else:
        guardar_como()

def guardar_como():
    global ruta
    mensaje.set("Guardar fichero como")
    fichero = FileDialog.asksaveasfile(title="Guardar fichero", mode="w", defaultextension=".txt")
    if fichero is not None:
        ruta = fichero.name # Obtenemos la ruta de fichero con este método.
        contenido = texto.get(1.0,'end-1c') # 'end-1c' es que recupere todo menos el último caracter.
        fichero = open(ruta, 'w+')
        fichero.write(contenido)
        fichero.close()
        mensaje.set("Fichero guardado correctamente.")
    else:
        mensaje.set("Guardado cancelado")
        ruta = ""


#Configuración de la raíz

root = Tk()

# Título del programa
root.title("Mi Editor de Texto")

# Menú Superior
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0) # Este es el primer menú en cascada
filemenu.add_command(label="Nuevo", command=nuevo) 
filemenu.add_command(label="Abrir", command=abrir)
filemenu.add_command(label="Guardar", command=guardar)
filemenu.add_command(label="Guardar como...", command=guardar_como)
filemenu.add_separator()
filemenu.add_command(label="Salir", command=root.quit)
menubar.add_cascade(menu=filemenu, label="Archivo") # Aquí estamos insertando el Filemenu en el Menu grande

# Caja de texto central

texto = Text(root)
texto.pack(fill="both", expand=1)
texto.config(bd=0, padx=6,pady=4, font=("Consolas",12), selectbackground="green")

# Monitor Inferior
mensaje = StringVar()
mensaje.set("Bienvenido a mi Editor de Texto")
monitor = Label(root, textvar=mensaje, justify="left")
monitor.pack(side="left")

#Configurar el Menú dentro del programa
root.config(menu=menubar)

#Bucle de la app
root.mainloop()