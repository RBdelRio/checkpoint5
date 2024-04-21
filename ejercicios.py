# 1 Bucle for
# bucle for sencillo: lista
nums = [4, 78, 9, 84]
for num in nums:
    print(num)

# bucle for en range
for num in range(4, 10):
  print(num)

# bucle for en diccionario
capitales_de_paises = {"España": "Madrid", "Francia": "Paris", "Italia": "Roma"}
for pais, capital in capitales_de_paises.items():
  print(pais+":", capital)

for pais in capitales_de_paises:
  print(pais)

for capital in capitales_de_paises.values():
  print(capital)


# 2 función suma
def suma(v_uno, v_dos, v_tres):
  resultado = v_uno + v_dos + v_tres
  return resultado

resultado_suma = suma(1, 2, 3) 
print("La suma es:", resultado_suma) 


# 3 función suma con lambda
suma = lambda v_1, v_2, v_3: v_1+v_2+v_3 
resultado = suma(1, 2, 3) 
print(f"la suma es:", resultado) 

# 4 for...in
nombre = "Enrique"
lista_nombre = ["Jessica", "Paul", "George", "Henry", "Adán"]

#método for...in con break
for item in lista_nombre:
    if item == nombre:
      print(f"{nombre} está en la lista.") # nos dice que sí está.
      break # el bucle se terminaría ahí
    else:
      print(f"Buenos días {item}.") # cada elemento de la lista que no sea igual a nombre

#método for...in con continue
for item in lista_nombre:
  if item == nombre:
    print(f"Buenos díás {item}.") # nos dice que sí está.
    continue # el bucle continuaría con los siguientes elementos
  else:
    print(f"{nombre} no está en la lista pero {item} sí.") # cada elemento de la lista que no sea igual a nombre
