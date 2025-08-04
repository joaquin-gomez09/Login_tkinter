from tkinter import * # Importamos la libreria "Tkinter"

ventana_principal = Tk() # Creamos la ventana principal donde se vera el contenido
ventana_principal.title("Identificate") # Asignamos un titulo
ventana_principal.minsize(width=300, height=400) # ajustamos el ancho y el alto
ventana_principal.config(padx=35, pady=35) # Generamos un margen interno

# Lienzo de 256x200 píxeles para mostrar la imagen
canvas = Canvas(width=256, height=200)

# Carga de imagen PNG desde la ruta especificada
foto_logo = PhotoImage(file="app_login/imagenes/candado_1.png")

# Inserta la imagen en el centro del canvas
canvas.create_image(128, 100, image=foto_logo)

# Mantiene la referencia para evitar que la imagen se borre
canvas.image = foto_logo

# Posiciona el canvas en la ventana (columna 0, fila 0)
canvas.grid(column=0, row=0)

label_1 = Label(text="Escribe tu nombre de usuario", font=("Arial", 14)) # Creamos un texto descriptivo y selecionamos el tipo de fuente y el tamaño
label_1.grid(column=0, row=1) # Ubicamos la linea de texto en la columna 0 y en la fila 1

espacio = Label(text="")
espacio.grid(column=0, row=2)

char_field_1 = Entry(width=20, font=("Arial", 14))
char_field_1.grid(column=0, row=3)

espacio = Label(text="")
espacio.grid(column=0, row=4)

label_2 = Label(text="Escribe tu contraseña", font=("Arial", 14)) # Creamos una segunda linea de texto y otro campo de texto
label_2.grid(column=0, row=5)

espacio = Label(text="")
espacio.grid(column=0, row=6)

char_field_2 = Entry(width=20, font=("Arial",14), show = "*") # Creamos una entrada ajustando el tamaño y la fuente
char_field_2.grid(column=0, row=7) # También un metodo de seguridad para que la contraseña no sea visible

espacio = Label(text="")
espacio.grid(column=0, row=8)

boton_1 = Button(text="Aceptar", font=("Arial", 14))
boton_1.grid(column=0, row=9)

ventana_principal.mainloop() # Creamos un bucle para mostrar la ventana indefinidamente