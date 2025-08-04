usuario_correcto = "root"
contraseña_correcta = "123"

for intento in range(3):
    usuario = input("Ingresar nombre de usuario: ").lower()
    
    if usuario == "guido":
            print("")
            print("👤✅ Usuario correcto\n")
            break
    else:
        print("")
        print("👤❌ Usuario incorrecto\n")
else:
    print("Demasiados intentos\n")
    exit()

for intento in range(3):
    contraseña = input("Ingresar contraseña: ")
    if contraseña == "python123":
            print("")
            print("🔓 Acceso concedido\n")
            print(f"Bienvenido {usuario}! \n")
            break
    else:
        print("")
        print("🔒 contraseña incorrecta\n")
else:
    print("")
    print("Demasiados intentos\n")

