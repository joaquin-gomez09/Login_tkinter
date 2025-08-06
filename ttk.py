import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.title("Prueba de ttk")
ventana.geometry("800x600")

# Crear un objeto "Style"
# style = ttk.Style()
# style.theme_use("nombre-x")

etiqueta = ttk.Label(ventana,
                     text="Hola mundo",
                     font=("Helvetica", 15))
etiqueta.pack(pady=10)

boton = ttk.Button(ventana, text="Aceptar")
boton.pack(pady=250)

ventana.mainloop()