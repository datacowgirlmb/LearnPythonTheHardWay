## Animal is-a object
class Animal(object):
	pass
	
## Dog is-a animal
class Dog(Animal):
	def __init__(self, name):
		## Dog has-a __init_ that takes self & name parameters
		self.name = name
		
## Cat is-a Animal, which is-a object
class Cat(Animal):
	def __init__(self, name):
		## Cat has-a name
		self.name = name

## Person is-a object
class Person(object):
	## Person has-a __init__ that takes self & name parameters
	def __init__(self, name):
		## Person has-a name
		self.name = name
		
		## Person has-a pet of some kind
		self.pet = None
		
## Employee is-a Person
class Employee(Person):
	## Employee has-a __init__ that takes self, name, & salary parameters
	def __init__(self, name, salary):
		## Call the Employee class with parameter name
		super(Employee, self).__init__(name)
		
		## Employee has-a salary
		self.salary = salary
		
## Fish is-a object
class Fish(object):
	pass
	
## Salmon is-a fish, which is-a object
class Salmon(Fish):
	pass
	
## Halibut is-a fish, which is-a object
class Halibut(Fish):
	pass
	
## rover is-a Dog, which is-a Animal, which is-a object
rover = Dog("Rover")

## Satan is-a Cat, which is-a Animal, which is-a object
satan = Cat("Satan")

## mary is-a Person, which is-a object
mary = Person("Mary")

## mary has-a pet (satan), which is a Cat, which is-a Animal, which is-a object
mary.pet = satan

## frank is-a Employee (with name "Frank" & salary 120000), which is-a Person
frank = Employee("Frank", 120000)

## frank has-a pet, which is Dog, which is-a Animal, which is-a object
frank.pet = rover

## flipper is a Fish, which is-a object
flipper = Fish()

# crouse is-a Salmon, which is-a Fish, which is-a object
crouse = Salmon()

## harry is a Halibut, which is-a Fish, which is-a object
harry = Halibut()