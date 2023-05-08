class Conjunto():
	def __init__(self):
		self.__conjunto = set()

	def AgregarNum(self):
		num = int(input("Ingrese un numero (0 para salir): "))
		while num != 0:
			self.__conjunto.add(num)
			num = int(input("Ingrese otro numero para el conjunto: "))

	def Muestra(self):
		print(self.__conjunto)

	def getConjunto(self):
		return self.__conjunto

	def __add__(self,otro):
		return self.__conjunto.union(otro.getConjunto())

	def __sub__(self,otro):
		return self.__conjunto.difference(otro.getConjunto())

	def __eq__(self,otro):
		return self.__conjunto == otro.getConjunto()
	