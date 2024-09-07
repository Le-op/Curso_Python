
tablas = ( "MENOR A 18.9=PESO BAJO", "18 A 24.99=PESO NORMAL","25.00 A 29.99=SOBREPESO", "30 A 39=OBESIDAD LEVE", "35 A 39.99=OBESIDAD MEDIA","MAYOR A 40=OBERSIDAD MORBIDA")

while True:

 print("\n--- ||TABLA DEL IMC|| ---")

 for i, tabla in enumerate(tablas):
  print(f"{i + 1}. {tabla}")

 nombre1 = (input("Escriba su nombre porfavor: "))
 if  nombre1.isnumeric() :
        print("Opción no válida. Intenta de nuevo.")
        continue
 
 apellidoP = (input("Escriba su apellido paterno: "))
 if  apellidoP.isnumeric() :
        print("Opción no válida. Intenta de nuevo.")
        continue 

 apellidoM = (input("Escriba su apellido materno: "))
 if  apellidoM.isnumeric() :
        print("Opción no válida. Intenta de nuevo.")
        continue
 
 edad = int (input("Escriba su edad porfavor: "))
 
 peso = float (input("Escriba tu peso en kg porfavor: "))

 altura = float (input("Escriba su estatura por favor: "))



 IMC = peso / altura ** 2



 if IMC >= 0 and IMC <= 18.99:
   
   print("Hola " + str(nombre1) + " a tu edad de " + str(edad) + " años" ", te encuentras en peso bajo, te recomiendo comer sanamente") 
   
 elif IMC >= 19 and IMC <= 24.99:
  print("Hola  " + str(nombre1) + " a tu edad de " + str(edad) + " años"  ", te encuentras en peso normal, sigue alimentandote sanamente")

 elif IMC >= 25 and IMC <= 29.99:
  print("Estas en sobrepeso " + str(nombre1) + " a tu edad de " + str(edad) + ", realiza mas ejercicio y come sanamente")

 elif IMC >= 30 and IMC <= 34.99:
  print("Estas en obesidad leve " + str(nombre1) + " a tu edad de " + str(edad) + ", realiza mas ejercicio y come sanamente")

 elif IMC >= 35 and IMC <= 39.99:
  print("estas en obesidad media " + str(nombre1) + " a tu edad de " + str(edad) + " Realiza mas ejercicio y come sanamente")

 elif IMC >= 40:
  print("estas en obesidad morbida " + str(nombre1) + " a tu edad de " + str(edad) + " Realiza mas ejercicio y come sanamente")

 elif IMC >= 40:
  print("estas en obesidad morbida " + str(nombre1) + " a tu edad de " + str(edad) + " Realiza mas ejercicio y come sanamente")

if edad > 18:
    
    print("Eres mayor de edad")

 else:
    print("Eres menor de edad")

 print("Tu masa corporal es: " + str(IMC))

 print("|||Gracias por usar la calculadora de IMC. Recuerda tu salud es lo mas importante|||")
amente")



