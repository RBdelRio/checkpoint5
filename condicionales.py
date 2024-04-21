#ejemplo 1

edad = 13 # variable que queremos comprobar

if edad < 16: # condición
	print("Eres menor y no puedes entrar") # acción si la condición es cierta


# ejemplo 2

edad = 25 # variable que queremos comprobar

if edad < 16: # condición
	print("Eres menor y no puedes entrar") # acción si la condición es cierta
else:
	print("¡Bienvenido!") # acción para el resto de los casos  


# ejemplo 3
    
edad = 30

if edad < 18: # condición
  print("Eres menor y no puedes entrar.") # acción si la condición es cierta
elif edad >= 18 and edad <=30 :  # segunda condición
      print("Si eres estudiante puedes beneficiarte del descuento.") # acción 
elif edad >= 65:  # tercera condición
      print("Si estás jubilado puedes beneficiarte del descuento.") # acción 
else:
  print("¡Bienvenido!") # acción para el resto de los casos  


# ejemplo 4

edad = 66 # variable que queremos comprobar

if edad < 18: # condición
  print("Eres menor y no puedes entrar.") # acción si la condición es cierta
else:
  if  edad >= 18 and edad  <=30:  # tercera condición
      print("Si eres estudiante puedes beneficiarte del descuento.") # acción 
  else:
    if edad >= 65:  # cuarta condición
      print("Si estás jubilado puedes beneficiarte del descuento.") # acción 
    else:
        print("¡Bienvenido!") # acción para el resto de los casos  


# ejemplo 5

edad = 13 

mensaje = "Eres menor y no puedes trabajar" if edad < 16 else "¡Bienvenido!" 

print(mensaje)


