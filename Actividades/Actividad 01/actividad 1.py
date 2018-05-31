import random
from abc import ABCMeta, abstractmethod


# El restoran guarda su lista de chefs y clientes
class Restaurant:
	def __init__(self, chefs,clients):
		self.chefs = chefs
		self.clients = clients

# La simulacion funciona por tres dias
# Tres platos cada chef por cliente
	def start(self):

		for i in range(3):
			print("Día "+ str(i+1) + ":")
			plates = []
			for chef in self.chefs:
				for j in range(3):
					plates.append(chef.cook())
			for client in self.clients:
				for plate in plates:
					client.eat_plate(plate)

class Plate:

	def __init__(self, food, drink):
		self.food = food
		self.drink = drink

# Es una clase abstracta
class Food(metaclass=ABCMeta):

	def __init__(self, ingredients):
		self.ingredients = []
		self.base_quality = random.randint(50,200)
		self.quality = 0

	#@abstractmethod
	#def check_time(self):
	#	pass

	@abstractmethod
	def check_ingredients(self):
		pass

	@abstractmethod
	def set_quality(self):
		pass

class Salad(Food):

	def __init__(self, lista_ingredients):
		super().__init__(lista_ingredients)
		self.ingredients.append("Lechuga")
		i1 = random.randint(0, len(lista_ingredients)-1)
		i2 = random.randint(0, len(lista_ingredients)-1)
		#while (i1 == i2):
		#	i2 = Random.randint(len()ingredients)
		self.ingredients.append(lista_ingredients[i1])
		self.ingredients.append(lista_ingredients[i2])

		self.set_quality()

	def set_quality(self):
		self.quality = self.base_quality + self.check_ingredients()

	def check_ingredients(self):
		added_quality = 0
		for ing in self.ingredients:
			cambio = 0
			if ing == "crutones":
				cambio += 20
			elif ing == "manzana":
				cambio -= 20
			added_quality += cambio
		return added_quality


class Pizza(Food):

	def __init__(self, lista_ingredients):
		super().__init__(lista_ingredients)
		self.ingredients.append("Queso")
		self.ingredients.append("Salsa de tomate")
		i1 = random.randint(0, len(lista_ingredients)-1)
		i2 = random.randint(0, len(lista_ingredients)-1)
		i3 = random.randint(0, len(lista_ingredients)-1)
		#while (i1 == i2):
		#	i2 = Random.randint(len()ingredients)
		self.ingredients.append(lista_ingredients[i1])
		self.ingredients.append(lista_ingredients[i2])
		self.ingredients.append(lista_ingredients[i3])
		self.set_quality()

	def set_quality(self):		
		self.quality = self.base_quality + self.check_ingredients()

	def check_ingredients(self):
		added_quality = 0
		for ing in self.ingredients:
			cambio = 0
			if ing == "pepperoni":
				cambio += 50
			elif ing == "pina":
				cambio -= 50
			added_quality += cambio
		return added_quality



class Drink(metaclass=ABCMeta):
	
	def __init__(self):
		self.base_quality = random.randint(50,150)
		self. quality = 0


class Jugo(Drink):

	def __init__(self):
		super().__init__()
		self.quality = self.base_quality + 30


class Soda(Drink):

	def __init__(self):
		super().__init__()
		self.quality = self.base_quality - 30


class Person(metaclass=ABCMeta):

	def __init__(self, name):
		self.name = name


class Chef(Person):

	def __init__(self, name):
		super().__init__(name)

	def cook(self):
		food_index = random.randint(0,1)
		drink_index = random.randint(0,1)

		# El random de ingredientes esta dentro de food
		if food_index == 0:
			food = Pizza(["pepperoni", "pina", "cebolla", "tomate", "jamon", "pollo"])
		else:
			food = Salad(["crutones", "espinaca", "manzana", "zanahoria"])
		if drink_index == 0:
			drink = Jugo()
		else:
			drink = Soda()

		plate = Plate(food,drink)

		return plate


class Client(Person):

	def __init__(self, name, personality):
		super().__init__(name)
		self.personality = personality

	def eat_plate(self, plate):
		average_quality = (plate.food.quality + plate.drink.quality)/2
		self.personality.react(average_quality)


class Personality(metaclass=ABCMeta):

	@abstractmethod
	def react(self):
		pass

	@abstractmethod
	def im_happy(self):
		pass

	@abstractmethod
	def im_mad(self):
		pass	

class Cool(Personality):
	def react(self, quality):
		if quality >= 100:
			self.im_happy()
		else:
			self.im_mad()
	def im_happy(self):
		print("Yumi! Que rico")

	def im_mad(self):
		print("Preguntare si puedo cambiarlo")

class Hater(Personality):

	def react(self, quality):
		if quality >= 100:
			self.im_happy()
		else:
			self.im_mad()

	def im_happy(self):
		print("No esta malo, pero igual prefiero Pizza x2")

	def im_mad(self):
		print("Nunca mas vendre a Daddy Juan's!")



"""

s = Pizza(["a","b","c","d"])
print(s.ingredients)
print(s.quality)
a = Soda()
print(a.quality)

"""

chef1 = Chef("A")
chef2 = Chef("B")
chef3 = Chef("C")
pers1 = Hater()
pers2 = Cool()
p1 = Client("1", pers1)
p2 = Client("2", pers2)

r = Restaurant([chef1,chef2,chef3],[p1,p2])
r.start()