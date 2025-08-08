import customtkinter as ct
import tkinter

ct.set_appearance_mode("light")  # Modo inicial

ventana = ct.CTk()
ventana.geometry("600x400+250+200")
ventana.title("Dark Mode")
ventana.iconbitmap("app_login/imagenes/icono.ico")

def cambiar_modo():
    val = switch.get()
    if val:
        ct.set_appearance_mode("dark")
    else:
        ct.set_appearance_mode("light")

switch = ct.CTkSwitch(ventana, text="Dark Mode",
                      onvalue=1,
                      offvalue=0,
                      command=cambiar_modo)

switch.place(
    relx=0.1,      # 50% del ancho
    rely=0.1,      # 50% de la altura
    anchor=tkinter.N)

# Línea divisoria vertical
linea = ct.CTkFrame(ventana, width=2, height=350, fg_color="gray")
linea.place(
    relx=0.25,  # Ajusta la posición horizontal
    rely=0.05,  # Ajusta la posición vertical
    anchor=tkinter.NW
)

def boton():
    print("¡Boton oprimido!")

boton_1 = ct.CTkButton(ventana, text="Boton",
                     command=boton)

boton_1.place(
    relx=0.5,
    rely=0.5,
    anchor=tkinter.CENTER)

ventana.mainloop()

#switch.pack(
#    pady=150           # ajusta la altura vertical
#)