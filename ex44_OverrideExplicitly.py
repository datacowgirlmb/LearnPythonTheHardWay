# override inheritence explicitly

class Parent(object):
	def override(self):
		print("PARENT override()")
		

class Child(Parent):
    # Child class inherits override() function, but it's overridden by the function of the same name in the Child class
	def override(self):
		print("CHILD override()")

dad = Parent()
son = Child()

dad.override()
son.override()