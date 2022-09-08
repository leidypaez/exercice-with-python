number1 = int(input("Introduce un numero para definir el intervalo menor: "))

number2 = int(input("Introduce un numero para definir el intervalo mayor: "))
 
if (number2 < number1): 
  print("!!ERROR¡¡, A ocurrido un error en el sistema, no se puede operar")
 
else:
  for i in range(number1, number2 + 1,  ):
  
    print(i)