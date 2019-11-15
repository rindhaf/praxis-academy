class Order:
    def __init__(self):
        print("Ini class Order")
    
    def setOrder(self, orderID, dateOrder, dateDeparture, departure, arrival, amountPassenger):
        Order.orderID = orderID
        Order.dateOrder = dateOrder
        Order.dateDeparture = dateDeparture
        Order.departure = departure
        Order.arrival = arrival
        Order.amountPassenger = amountPassenger
    
    def getOrder(self):
        print("Order ID         = ", Order.orderID)
        print("Date Order       = ", Order.dateOrder)
        print("Date Depature    = ", Order.dateDeparture)
        print("Departure place  = ", Order.departure)
        print("Arrival place    = ", Order.arrival)
        print("Amount Passenger = ", Order.amountPassenger)        