#importar  Tkinter
import tkinter

from tkinter import messagebox

messagebox.askokcancel("Python","Would you like to save the data?")
messagebox.askokcancel("Título", "La aplicación se cerrará") # Opción messagebox
messagebox.askyesno("Título", "¿Desea guardar?" ) # Inténtalo de nuevo messagebox
messagebox.askretrycancel("Título" , " Error de instalación, ¿volver a intentarlo?" )
