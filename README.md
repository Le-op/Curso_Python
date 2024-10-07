# Curso de Python

MODULO 2.

EJERCICIO 1:

Me encantaría explicar cómo escribi el verificar_longitud_palabra()función.

Resumen Su función, verificar_longitud_palabra(), toma una frase de usuario y comprueba su longitud. A continuación, imprime un mensaje indicando si la frase es válida (es decir, entre 4 y 8 caracteres de largo) o no.

Desglose paso a paso

    Entrada de usuario: Usted le pide al usuario que introduzca una frase usando input("Ingrese una frase: "). Esto almacena la entrada en el palabravariable.
    Calcular longitud de frase : Utiliciendo el incorporado len()función para calcular la longitud de la frase de entrada y almacenarla en el .

EJERCICIO 2:

Resumen Su función, identificar_cuadrante(), toma las coordenadas de entrada al usuario (x, y) y determina en qué cuadrante caen.

Desglose paso a paso

    Obtenga entrada de usuario: Instólese al usuario en introducir coordenadas x y y usando input()funciones, almacenándolos x,y e variables, respectivamente.
    Validar coordenadas: Utiliza un whilebucle para asegurarse de que ni x ni y es 0. Si cualquiera de las coordenadas es 0, imprime un mensaje de error y inste al usuario a volver a entrar en las coordenadas.
    Determinar el cuadrante: Una vez que tiene coordenadas válidas, usted utiliza unif-elif-elsedeclaración para determinar en qué cuadrante cae el punto basado en los signos de x y:
        Si x 0 e 0, el punto está en el cuadrante I.
        Si x x 0 e 0, el punto está en Quadrant II.
        Si x 0 e 0, el punto está en el cuadrante III.
        De lo contrario, el punto está en el Cuadrante IV.

Mediante el uso de esta lógica, la función identifica correctamente el cuadrante para cualquier conjunto de coordenadas dadas.
