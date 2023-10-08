import os
import time
import subprocess
import tkinter as tk
from tkinter import filedialog

def adjuntar_01():
    archivo_1 = filedialog.askopenfilename()
    if archivo_1:
        label_archivo1.config(text="Archivo adjuntado: " + archivo_1)
        adjuntar_archivos.append(archivo_1)    
def adjuntar_02():
    archivo_2 = filedialog.askopenfilename()
    if archivo_2:
        label_archivo2.config(text="Archivo adjuntado" + archivo_2)
        adjuntar_archivos.append(archivo_2)
def ejecutar_commando():
    if len(adjuntar_archivos) == 2:
        print(adjuntar_archivos)
        commando = "cat " + adjuntar_archivos[0]+" "+adjuntar_archivos[1]+" > musica.mp3"
        os.system(f"{commando}")
        print("Guardado como musica.mp3 en la carpeta actual")
        label_comando.config(text="guardado en la ruta actual como musica.mp3")
    else:
        label_resultado.config(text="archivo generado con exito")      

ventana = tk.Tk()
ventana.title("FileCloak_Soundwave")
ventana.geometry("500x500")
ventana.configure(bg="black")
adjuntar_archivos = []

label_archivo1 = tk.Label(ventana, text="")
label_archivo1.pack()

boton_adjuntar1 = tk.Button(ventana, text="Adjuntar musica o imagen", command=adjuntar_01)
boton_adjuntar1.pack()

label_archivo2 = tk.Label(ventana, text="")
label_archivo2.pack()

boton_adjuntar2 = tk.Button(ventana, text="adjuntar zip comprimido", command=adjuntar_02)
boton_adjuntar2.pack()

boton_ejecutar = tk.Button(ventana, text="GUARDAR", command=ejecutar_commando)
boton_ejecutar.pack()

label_resultado = tk.Label(ventana, text="")

label_comando = tk.Label(ventana, text="")

imagen = tk.PhotoImage(file="mygif.gif")
label_imagen = tk.Label(ventana, image=imagen)
label_imagen.pack()

ventana.mainloop()