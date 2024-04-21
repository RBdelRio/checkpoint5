# Ejemplo 1

nums = [1, 2, 3, 4, 5]
numeros_dobles = []

for num in nums:
	numeros_dobles.append(num*2)

print(numeros_dobles) #Output: [1, 4, 6, 8,10]


# Ejemplo 2

nums = [1, 2, 3, 4, 5]

numeros_dobles = [num*2 for num in nums] # indicamos que cada elemento de la lista se multiplique por dos. 

print(numeros_dobles) #Output: [1, 4, 6, 8,10]


# Ejemplo 3

numeros_impares = []
for num in range(10):
    if num % 2 != 0: # si el resto de la división del número entre 2 es distinto a cero entonces el número es impar
    	numeros_impares.append(num) 

print(numeros_impares) # Output: [1, 3, 5, 7, 9]


# Ejemplo 4

numeros_impares = [num for num in range(10) if num % 2 != 0]

print(numeros_impares) # Output: [1, 3, 5, 7, 9]
