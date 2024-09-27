# EJERCICIO 1°


def verificar_longitud_palabra():
    palabra = input("Ingrese una frase: ") # Solictamos al usururio que ingrese su frase mayor a 4 letras y menor a 8
    longitud = len(palabra) # La funcion len calcula la longitud de la palabra.

    if 4 <= longitud <= 8: # Aqui colocamos la condicion del rango de la frase mayor a 4 y menor a 8. La frase es correcta.
        print("La palabra es correcta.")
    elif longitud < 4: # De lo contrario si es menor a 4, solicitamos mas letras.
        print(f"Hacen falta letras. Solo tiene {longitud} letras.")
    else: # Si es mayor a 8, indicar que sobran letras.
        print(f"Sobran letras. Tiene {longitud} letras.")

verificar_longitud_palabra()


#############################################################################################################################################################################################################################


# EJERCICIO 2°

def identificar_cuadrante(): 
    x = int(input("Ingrese coordenada X: ")) # Solicitamos al usuario las coordenadas X e Y.
    y = int(input("Ingrese coordenada Y: "))

    while x == 0 or y == 0: # Utilice un bucle while para asegurar que ninguna coordenada sea CERO, de lo contrario muestra un mensaje de error.
        print("Ninguna coordenada puede ser 0.")
        x = int(input("Ingrese coordenada X: "))
        y = int(input("Ingrese coordenada Y: "))

    if x > 0 and y > 0: # Usando las funciones if, elif y els para determinar el cuadrnate segun los signos X e Y.
        print("El punto se encuentra en el cuadrante I.")
    elif x < 0 and y > 0:
        print("El punto se encuentra en el cuadrante II.")
    elif x < 0 and y < 0:
        print("El punto se encuentra en el cuadrante III.")
    else:
        print("El punto se encuentra en el cuadrante IV.")

identificar_cuadrante()
