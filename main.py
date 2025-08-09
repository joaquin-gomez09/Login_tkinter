from tkinter import * # Importamos la libreria "Tkinter"
from tkinter import messagebox # messagebox para dar mensajes de alerta o avisos al usuario
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Credenciales
USUARIO_CORRECTO = "root"
CLAVE_USUARIO = "123"

# Contador

intentos = 0

# Colores según intentos
colores_intentos = {
    0: "#555555",  # gris oscuro (sin errores)
    1: "#FF9900",  # naranja (primer error)
    2: "#FF3300",  # rojo fuerte (segundo error)
    3: "#CC0000"   # rojo oscuro (bloqueado)
}

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
        ventana_secundaria = tk.Toplevel()
        
        def cerrar_ventanas():
            ventana_secundaria.destroy()
            ventana_principal.destroy()

        ventana_secundaria.title("Bienvenido")
        ventana_secundaria.config(width=400, height=320)
        ventana_secundaria.iconbitmap("app_login/imagenes/icono.ico")
        ventana_secundaria.focus()
        ventana_secundaria.grab_set()

        imagen = Image.open("app_login/imagenes/construccion.jpg")
        imagen_tk = ImageTk.PhotoImage(imagen)

        label_imagen = tk.Label(ventana_secundaria, image=imagen_tk)
        label_imagen.image = imagen_tk  # ← Esto evita que la imagen se borre
        label_imagen.pack()

        boton_cerrar = ttk.Button(ventana_secundaria,text="Salir", command=cerrar_ventanas)
        boton_cerrar.place(relx=0.5, rely=0.9, anchor="center")


    else:
        intentos += 1 # 3️⃣ Falló el login: sumamos un intento
        intentos_restantes = 3 - intentos

        mensaje_label.config(text="❌ Usuario o contraseña incorrectos", fg="red") # Cambiamos el mensaje principal a rojo

        if intentos < 3: # Cambiamos el label de intentos
            intentos_label.config(text=f"Te quedan {intentos_restantes} intentos", fg=colores_intentos[intentos])
        else:
            intentos_label.config(text="🚨 Demasiados intentos. Bloqueado.", fg=colores_intentos[3]) # Si ya falló 3 veces, bloqueamos
            boton_1.config(state="disabled")
            ventana_principal.after(2000, ventana_principal.destroy)

def toggle_password():
    if char_field_2.cget('show') == '*':
        char_field_2.config(show='')
        boton_toggle.config(text="Ocultar")
    else:
        char_field_2.config(show='*')
        boton_toggle.config(text="Mostrar")

ventana_principal = Tk()
ventana_principal.title("Iniciar sesion")
ventana_principal.minsize(width=300, height=400)
ventana_principal.config(padx=35, pady=35)
ventana_principal.iconbitmap("app_login/imagenes/icono.ico")

canvas = Canvas(width=256, height=200)
foto_logo = PhotoImage(file="app_login/imagenes/candado.png")
canvas.create_image(128, 100, image=foto_logo)
canvas.image = foto_logo
canvas.grid(column=0, row=0)

# Objeto de estilos
style = ttk.Style()
style.theme_use(style.theme_use())  # Mantiene el tema del sistema

style.configure("Custom.TLabel", font=("Arial", 14))
style.configure("Custom.TEntry", font=("Arial", 14))
style.configure("Custom.TButton", font=("Arial", 12), padding=6)

label_1 = ttk.Label(text="Escribe tu nombre de usuario", style="Custom.TLabel")
label_1.grid(column=0, row=1)

Label(text="").grid(column=0, row=2)

char_field_1 = ttk.Entry(width=40, style="Custom.TEntry")
char_field_1.grid(column=0, row=3)

Label(text="").grid(column=0, row=4)

label_2 = ttk.Label(text="Escribe tu contraseña", style="Custom.TLabel")
label_2.grid(column=0, row=5)

char_field_2 = ttk.Entry(width=40, style="Custom.TEntry", show="*")
char_field_2.grid(column=0, row=6)

Label(text="").grid(column=0, row=8)

boton_toggle = ttk.Button(text="Mostrar", style="Custom.TButton", command=toggle_password)
boton_toggle.grid(column=0, row=9)

Label(text="").grid(column=0, row=10)

boton_1 = ttk.Button(text="Aceptar", style="Custom.TButton", command=verificar_login)
boton_1.grid(column=0, row=12)

mensaje_label = Label(text="", font=("Arial", 12))
mensaje_label.grid(column=0, row=13)

intentos_label = tk.Label(text="Tienes 3 intentos", font=("Arial", 12), foreground=colores_intentos[0])
intentos_label.grid(column=0, row=14)

ventana_principal.mainloop()