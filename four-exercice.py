key = "panda"
password = input("Introduce la contraseña: ")
if key == password.lower():
    print("Ha ingresado con exito")
else:
  while True:
    entrada = input("La contraseña es incorrecta,vuelva a intentarlo o escriba ´exit´para salir ")
    if (entrada == "contraseña"):
      print("Ha ingresado con exito")
      break
    elif (entrada == "exit"):
        print("Ha salido con exito")
        break