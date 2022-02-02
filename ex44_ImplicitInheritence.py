# implicit inheritence

class Parent(object):
	def implicit(self):
		print("PARENT implicit()")
		

# Child class inherits all features from the Parent class
class Child(Parent):
	pass
	
	
dad = Parent()
son = Child()

dad.implicit()
son.implicit()