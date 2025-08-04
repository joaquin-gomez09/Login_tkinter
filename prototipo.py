from tkinter import * # Importamos la libreria "Tkinter"

# Credenciales

USUARIO_CORRECTO = "Guido"
CLAVE_USUARIO = "python123"

ventana_principal = Tk()
ventana_principal.title("Iniciar sesion")
ventana_principal.minsize(width=300, height=400)
ventana_principal.config(padx=35, pady=35)

label_1 = Label(text="Escribe tu nombre de usuario", font=("Arial", 14))
label_1.grid(column=0, row=1)

espacio = Label(text="")
espacio.grid(column=0, row=2)

char_field_1 = Entry(width=20, font=("Arial", 14))
char_field_1.grid(column=0, row=3)

espacio = Label(text="")
espacio.grid(column=0, row=4)

label_2 = Label(text="Escribe tu contraseña", font=("Arial", 14)) # Creamos una segunda linea de texto y otro campo de texto
label_2.grid(column=0, row=5)

char_field_2 = Entry(width=20, font=("Arial", 14), show="*")
char_field_2.grid(column=0, row=6)

espacio = Label(text="")
espacio.grid(column=0, row=7)

mensaje_label = Label(text="", font=("Arial", 12))
mensaje_label.grid(column=0, row=10)

def verificar_login():

    usuario = char_field_1.get()
    contraseña = char_field_2.get()

    if usuario == USUARIO_CORRECTO and contraseña == CLAVE_USUARIO:
        mensaje_label.config(text=f"✅ Bienvenido {usuario}!", fg="green")
    else:
        mensaje_label.config(text="❌ Usuario o contraseña incorrectos", fg="red")

boton_1 = Button(text="Aceptar", font=("Arial", 14), command=verificar_login)
boton_1.grid(column=0, row=8)

ventana_principal.mainloop()