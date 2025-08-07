import customtkinter as ct

ct.set_appearance_mode("light")  # Modo inicial

ventana = ct.CTk()
ventana.geometry("600x400+250+200")
ventana.title("Dark Mode")

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
switch.pack(
    pady=150  # ajusta la altura vertical
)
ventana.mainloop()