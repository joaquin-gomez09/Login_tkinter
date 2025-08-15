
---

🖥️ Identificación con Tkinter

Una interfaz gráfica sencilla desarrollada en Python usando Tkinter, diseñada para solicitar usuario y contraseña de forma amigable y ordenada.

📋 Descripción

La aplicación abre una ventana titulada "Identificate" que incluye:

Campo para nombre de usuario

Campo para contraseña (oculto con asteriscos)

Botón "Aceptar" para confirmar los datos ingresados


Diseñada con espaciado y márgenes para mejorar legibilidad y estética.


---

🧱 Estructura del Código

1. Importación

from tkinter import *

2. Configuración de la ventana principal

ventana_principal = Tk()
ventana_principal.title("Identificate")
ventana_principal.minsize(width=300, height=400)
ventana_principal.config(padx=35, pady=35)

3. Elementos de la interfaz

Label y Entry para usuario

Label y Entry para contraseña (show="*")

Botón para enviar datos

Espaciado con Label vacío

Posicionamiento con .grid()


4. Bucle principal

ventana_principal.mainloop()


---

🚀 Ejecución

1. Instalar Python 3.x


2. Guardar el código como identificacion.py


3. Ejecutar:



python identificacion.py


---

🛠️ Mejoras Implementadas / Pendientes

[ ] Validar datos y mostrar mensajes de éxito/error

[ ] Conexión con base de datos para verificar credenciales

[ ] Estilos personalizados con ttk o temas

[ ] Redirección a otra ventana tras inicio de sesión

[ ] Migración a una GUI más moderna con CustomTkinter



---

📦 Requisitos

Python 3.x

Tkinter (incluido en la mayoría de instalaciones de Python)



---

💡 Próximamente: autenticación real con base de datos y versión en CustomTkinter para una interfaz más moderna.

