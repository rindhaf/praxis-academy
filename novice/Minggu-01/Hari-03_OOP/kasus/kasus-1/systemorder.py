class System:

	def __init__(self):
		pass

	def setCredit(self, orderID, status):
		System.orderID = orderID
		System.status = status

	def getCredit(self):
		print("Order ID = ", System.orderID)
		print("Status order = ", System.status) 