
nombre1 = str (input("Escriba su nombre porfavor: "))
apellidoP = (input("Escriba su apellido paterno: "))
apellidoM = (input("Escriba su apellido materno: "))
edad = int (input("Escriba su edad porfavor: "))
peso = float (input("Escriba tu peso en kg porfavor: "))
altura = float (input("Escriba su estatura por favor: "))

IMC = peso / altura ** 2


if edad < 18:
    print("Eres menor de edad")

else:
    print("Eres menor de edad")

print("Tu masa corporal es: " + str(IMC))


if IMC >= 0 and IMC <= 18.9:
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



