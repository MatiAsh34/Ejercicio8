from ClaseConjunto import *

if __name__ == '__main__':

	opcion = None
	while opcion != 5:
		print("1- Crear conjuntos")
		print("2- Sumar dos conjuntos")
		print("3- Restar dos conjuntos")
		print("4- Verificar si dos conjuntos son iguales")
		print("5- Salir")
	
		opcion = int(input("Ingrese codigo: "))
		if opcion == 1:
			print("Elmentos del conjunto 1")
			Conjunto1 = Conjunto()
			Conjunto1.AgregarNum()
			print("Elmentos del conjunto 2")
			Conjunto2 = Conjunto()
			Conjunto2.AgregarNum()

		if opcion == 2:
			Conjunto3 = Conjunto1 + Conjunto2 
			print(Conjunto3)

		if opcion == 3:
			Conjunto3 = Conjunto1 - Conjunto2 
			print(Conjunto3)

		if opcion == 4:
			if Conjunto1 == Conjunto2:
				print("Son iguales")
			else:
				print("No son iguales")

		if opcion == 5:
			print ("Saliendo....")
