# 🖥️ Identificación con Tkinter

Este proyecto es una interfaz gráfica simple creada con **Tkinter**, la biblioteca estándar de Python para crear interfaces gráficas de usuario (GUI). El propósito de esta aplicación es solicitar al usuario que ingrese su nombre de usuario y contraseña en una ventana amigable y bien organizada.

## 📋 Descripción del Proyecto

La aplicación muestra una ventana titulada **"Identificate"** con los siguientes elementos:

- Un campo para ingresar el **nombre de usuario**
- Un campo para ingresar la **contraseña** (oculta con asteriscos)
- Un botón de **"Aceptar"** para confirmar los datos ingresados

La interfaz está diseñada con márgenes internos y espaciado entre los elementos para mejorar la legibilidad y la estética.

## 🧱 Estructura del Código

El código está organizado de la siguiente manera:

### 1. **Importación de la biblioteca**
```python
from tkinter import *
```
Se importa todo el módulo `tkinter` para utilizar sus componentes.

### 2. **Configuración de la ventana principal**
```python
ventana_principal = Tk()
ventana_principal.title("Identificate")
ventana_principal.minsize(width=300, height=400)
ventana_principal.config(padx=35, pady=35)
```
- Se crea la ventana principal.
- Se asigna un título.
- Se define un tamaño mínimo.
- Se agregan márgenes internos.

### 3. **Elementos de la interfaz**
- **Etiqueta para el nombre de usuario**
- **Campo de entrada para el nombre de usuario**
- **Etiqueta para la contraseña**
- **Campo de entrada para la contraseña** (con `show="*"` para ocultar el texto)
- **Botón "Aceptar"**

Cada elemento se posiciona usando el método `.grid()` para organizar la interfaz en filas y columnas.

### 4. **Espaciado**
Se utilizan etiquetas vacías (`Label(text="")`) para generar espacio entre los elementos y mejorar la presentación visual.

### 5. **Bucle principal**
```python
ventana_principal.mainloop()
```
Este bucle mantiene la ventana abierta y activa hasta que el usuario la cierre.

## 🚀 Cómo ejecutar el programa

1. Asegúrate de tener Python instalado en tu sistema.
2. Guarda el código en un archivo con extensión `.py`, por ejemplo: `identificacion.py`
3. Ejecuta el archivo desde tu terminal o entorno de desarrollo:
```bash
python identificacion.py
```

## 🛠️ Posibles mejoras

Aquí tienes algunas ideas para expandir el proyecto:

- Validar los datos ingresados y mostrar un mensaje de éxito o error.
- Conectar con una base de datos para verificar credenciales.
- Añadir estilos personalizados con `ttk` o temas.
- Implementar navegación a otra ventana tras el inicio de sesión.

## 📌 Requisitos

- Python 3.x
- Tkinter (incluido por defecto en la mayoría de instalaciones de Python)
