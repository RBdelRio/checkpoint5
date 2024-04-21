# Ejemplo 1

def suma(a, b): 
 return a + b 

resultado = suma(3, 5) # 3 se asigna a a y 5 se asigna a b 
print(resultado) 


# Ejemplo 2

def saludar(nombre, saludo): 
	return f"{saludo}, {nombre}:" 

mensaje = saludar(saludo="Hola", nombre="Juan") 
print(mensaje) 


# Ejemplo 3

def saludar(nombre, saludo="Hola"):
    return f"{saludo}, {nombre}." 

mensaje = saludar("Sara") 
print(mensaje) 


# Ejemplo 4

def promedio(*numeros): 
	return sum(numeros) / len(numeros) # se suman los valores de los argumentos y se dividen entre el número de argumentos

resultado = promedio(5, 10, 15) # se definen los valores de los argumentos. Se especifican tantos como se desee.
print(resultado) 


# Ejemplo 5

def detalles(**info): 
	for key, value in info.items(): # formato elementos de un diccionario
   		print(f"{key}: {value}") 

detalles(nombre="Ana", edad=30, ciudad="Madrid") # los valores para cada elemento del diccionario. 


