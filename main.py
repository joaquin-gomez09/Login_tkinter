from tkinter import * # Importamos la libreria "Tkinter"
from tkinter import messagebox # messagebox para dar mensajes de alerta o avisos al usuario

# Credenciales
USUARIO_CORRECTO = "guido"
CLAVE_USUARIO = "python123"

# Contador

intentos = 0

# Función para verificar Login

def verificar_login():
    global intentos
    usuario = char_field_1.get()
    contraseña = char_field_2.get()

    if not usuario or not contraseña:
        messagebox.showwarning("Campos vacíos", "Por favor completa todos los campos.") # El primer parametro es el titulo
        return

    if usuario == USUARIO_CORRECTO and contraseña == CLAVE_USUARIO:
        mensaje_label.config(text=f"✅ Bienvenido {usuario}!", fg="green")
        ventana_principal.after(2000, ventana_principal.destroy)
    else:
        intentos += 1
        if intentos >= 3:
            mensaje_label.config(text="❌ Demasiados intentos.\nPor motivos de seguridad esta ventana sera bloqueada", fg="red")
            boton_1.config(state="disabled")
            ventana_principal.after(2000, ventana_principal.destroy)
        else:
            mensaje_label.config(text="❌ Usuario o contraseña incorrectos", fg="red")

ventana_principal = Tk()
ventana_principal.title("Iniciar sesion")
ventana_principal.minsize(width=300, height=400)
ventana_principal.config(padx=35, pady=35)
# ventana_principal.configure(bg="#000000") (cambio de color, por el momento no)
canvas = Canvas(width=256, height=200)
foto_logo = PhotoImage(file="app_login/imagenes/candado_1.png")
canvas.create_image(128, 100, image=foto_logo)
canvas.image = foto_logo
canvas.grid(column=0, row=0)

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

boton_1 = Button(text="Aceptar", font=("Arial", 14), command=verificar_login)
boton_1.grid(column=0, row=8)

ventana_principal.mainloop()