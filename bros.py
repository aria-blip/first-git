class bro:
	"""docstring for bro"""
	def __init__(self,name,age):
		self.name=name
		self.age=age
	def info(self):
		print("this dude is "+str(self.age)+" years old and is called "+self.name)


firstbro=bro("mike",14)

firstbro.info()