import tkinter as tk
from PIL import Image, ImageTk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Prueba de imagen")

# Cargar la imagen

imagen = Image.open("app_login/imagenes/candado_pillow.jpg")
imagen_tk = ImageTk.PhotoImage(imagen)

# Crear y mostrar el label con imagen

label_imagen = tk.Label(ventana, image=imagen_tk)
label_imagen.pack()

# Ejecutar la ventana

ventana.mainloop()