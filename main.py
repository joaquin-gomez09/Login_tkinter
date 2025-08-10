import customtkinter as ctk
from tkinter import messagebox
from tkinter import Toplevel  # Importar Toplevel de tkinter
from PIL import Image
import os

# Configuración inicial de CustomTkinter
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

# Credenciales
USUARIO_CORRECTO = "root"
CLAVE_USUARIO = "123"

# Contador
intentos = 0

# Colores según intentos
colores_intentos = {
    0: "#555555",
    1: "#FF9900",
    2: "#FF3300",
    3: "#CC0000"
}

# Función para verificar Login
def verificar_login():
    global intentos
    usuario = char_field_1.get()
    contraseña = char_field_2.get()

    if not usuario or not contraseña:
        messagebox.showwarning("Campos vacíos", "Por favor completa todos los campos.")
        return

    if usuario == USUARIO_CORRECTO and contraseña == CLAVE_USUARIO:
        mensaje_label.configure(text=f"✅ Bienvenido {usuario}!", text_color="green")

        # Crear ventana secundaria con tkinter
        ventana_secundaria = Toplevel()
        ventana_secundaria.title("App")
        ventana_secundaria.geometry("800x600")

        # Ruta absoluta del ícono
        ruta_icono = os.path.abspath("app_login/imagenes/icono.ico")
        ventana_secundaria.iconbitmap(ruta_icono)
        #print(ruta_icono)

        ventana_secundaria.focus()
        ventana_secundaria.grab_set()

        def cerrar_ventanas():
            ventana_secundaria.destroy()
            ventana_principal.destroy()

        # Frame CTk dentro de la ventana secundaria
        frame_secundario = ctk.CTkFrame(master=ventana_secundaria, fg_color="black")
        frame_secundario.pack(fill="both", expand=True)

        # Imagen en ventana secundaria
        imagen_ctk = ctk.CTkImage(light_image=Image.open("app_login/imagenes/construccion.jpg"), size=(700, 550))
        label_imagen = ctk.CTkLabel(frame_secundario, image=imagen_ctk, text="")
        label_imagen.pack()

        # Botón cerrar
        boton_cerrar = ctk.CTkButton(frame_secundario, text="Salir", command=cerrar_ventanas)
        boton_cerrar.pack(pady=10)

    else:
        intentos += 1
        intentos_restantes = 3 - intentos

        mensaje_label.configure(text="❌ Usuario o contraseña incorrectos", text_color="red")

        if intentos < 3:
            intentos_label.configure(text=f"Te quedan {intentos_restantes} intentos", text_color=colores_intentos[intentos])
        else:
            intentos_label.configure(text="🚨 Demasiados intentos. Bloqueado.", text_color=colores_intentos[3])
            boton_1.configure(state="disabled")
            ventana_principal.after(2000, ventana_principal.destroy)

def toggle_password():
    if char_field_2.cget('show') == '*':
        char_field_2.configure(show='')
        boton_toggle.configure(text="Ocultar")
    else:
        char_field_2.configure(show='*')
        boton_toggle.configure(text="Mostrar")

# Ventana principal
ventana_principal = ctk.CTk()
ventana_principal.title("Iniciar sesión")
ventana_principal.minsize(width=300, height=400)
ventana_principal.geometry("450x480")
ventana_principal.iconbitmap("app_login/imagenes/icono.ico")
ventana_principal.grid_columnconfigure(0, weight=1)

# Logo principal
logo_image = ctk.CTkImage(light_image=Image.open("app_login/imagenes/candado.png"), size=(130, 130))
canvas = ctk.CTkLabel(ventana_principal, image=logo_image, text="")
canvas.grid(row=0, column=0)

# Widgets
ctk.CTkLabel(ventana_principal, text="").grid(row=1, column=0)

label_1 = ctk.CTkLabel(ventana_principal, text="Escribe tu nombre de usuario", font=("Arial", 14))
label_1.grid(row=2, column=0)

char_field_1 = ctk.CTkEntry(ventana_principal, width=240, font=("Arial", 14))
char_field_1.grid(row=3, column=0)

ctk.CTkLabel(ventana_principal, text="").grid(row=4, column=0)

label_2 = ctk.CTkLabel(ventana_principal, text="Escribe tu contraseña", font=("Arial", 14))
label_2.grid(row=5, column=0)

char_field_2 = ctk.CTkEntry(ventana_principal, width=240, font=("Arial", 14), show="*")
char_field_2.grid(row=6, column=0)

ctk.CTkLabel(ventana_principal, text="").grid(row=8, column=0)

boton_toggle = ctk.CTkButton(ventana_principal, text="Mostrar", font=("Arial", 12), command=toggle_password)
boton_toggle.grid(row=9, column=0)

ctk.CTkLabel(ventana_principal, text="").grid(row=10, column=0)

boton_1 = ctk.CTkButton(ventana_principal, text="Aceptar", font=("Arial", 12), command=verificar_login)
boton_1.grid(row=12, column=0)

mensaje_label = ctk.CTkLabel(ventana_principal, text="", font=("Arial", 12))
mensaje_label.grid(row=13, column=0)

intentos_label = ctk.CTkLabel(ventana_principal, text="Tienes 3 intentos", font=("Arial", 12), text_color=colores_intentos[0])
intentos_label.grid(row=14, column=0)

ventana_principal.mainloop()