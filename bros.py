class bro:
	"""docstring for bro"""
	def __init__(self,name,age,gender):
		self.name=name
		self.age=age
		self.gender=gender
	def info(self):
		if self.gender=="furry":
			print("we got a furry")
		print("this "+self.gender+" is "+str(self.age)+" years old and is called "+self.name)


firstbro=bro("mike",14,"male")

firstbro.info()