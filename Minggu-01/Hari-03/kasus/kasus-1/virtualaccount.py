class VirtualAccount:

	def __init__(self):
		pass

	def setVA(self, number):
		VirtualAccount.number = number
		
	def getVA(self):
		print("Number 	 = ", VirtualAccount.number)