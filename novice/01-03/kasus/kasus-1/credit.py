class Credit:

	def __init__(self):
		pass

	def setCredit(self, number, type, expDate):
		Credit.number = number
		Credit.type = type
		Credit.expDate = expDate

	def getCredit(self):
		print("Number card 	 = ", Credit.number)
		print("Type card	 = ", Credit.type)
		print("Exprired Date = ", Credit.expDate)		