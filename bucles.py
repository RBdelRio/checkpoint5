# Ejemplo 1
numeros = [1, 2, 3, 4, 5] 

for num in numeros: # para (for) cada elemento (num) en el objeto iterable (la lista numeros)
	print(num) #acción a realizar. Se imprimirá cada número en la lista.



#Ejemplo 2

numeros = [1, 2, 3, 4, 5] 

for num in numeros: # para (for) cada elemento (num) en el objeto iterable (la lista numeros)
	calc = num*2 - (num-1)*(num+1) # cálculo
	print(calc) #acción

# Ejemplo 3

capitales_de_paises = {"España": "Madrid", "Francia": "Paris", "Italia": "Roma"}

for pais in capitales_de_paises:
	print(pais)


# Ejemplo 4

capitales_de_paises = {"España": "Madrid", "Francia": "Paris", "Italia": "Roma"}

for capital in capitales_de_paises.values():
	print(capital)


# Ejemplo 5

capitales_de_paises = {"España": "Madrid", "Francia": "Paris", "Italia": "Roma"}

for pais, capital in capitales_de_paises.items():
	print(pais+":", capital)


#Ejemplo 6

for num in range(10):
	print (num) # imprimirá los números desde el 0 al 9.


#Ejemplo 7

for num in range(4,10):
	print (num) # imprimirá los números desde el 4 al 9.


#Ejemplo 8

for num in range(1,10, 2):
	print (num) # imprimirá los números del 1 al 9, cada dos números (es decir, sólo los números impares)


#Ejemplo 9

nombre = "Enrique"
lista_nombre = ["Jessica", "Paul", "George", "Henry", "Adán"]

for item in lista_nombre:
	if item == nombre: # condición
		print(f"{nombre} está en la lista.") # acción si condición es True
		break # si condición es True el bucle se termina y se sale de él.
	else:
     		print(f"Buenos días {item}.") # acción si condición es False


#Ejemplo 10

nombre = "Enrique"
lista_nombre = ["Jessica", "Paul", "George", "Henry", "Adán"]

for item in lista_nombre:
	if item == nombre: # condición
		print(f"{nombre} está en la lista.") # acción si condición es True
		continue # el bucle pasa al siguiente elemento.
	else:
     		print(f"Buenos días {item}.") # acción si condición es False


#Ejemplo 11

numeros = [1, 2, 3, 4, 5]
contador = 0

while contador < 5: # la condición que se evalúa en cada iteración del bucle. Mientras la condición sea True, la acción o acciones se realizarán.
	print(contador) # acción 
	contador += 1  # acción

#Ejemplo 12

lista_nombre = ["Jessica", "Paul", "George", "Henry", "Adam"]

contador = 0

while contador < len(lista_nombre): # primera condición
	nombre = lista_nombre[contador] 
	if nombre == "Enrique":  # segunda condición
		print(f'{nombre} ha sido encontrado en la posición número {contador+1}')
		break # el bucle se termina si esta segunda condición es True
	else: # en caso de que esta segunda condición sea False
      		contador += 1
else: # en caso de que la primera condición sea False
    print(f"Enrique no se encuentra en la lista.")
