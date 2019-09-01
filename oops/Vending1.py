class Vending_machine(object):
	"""docstring for Vending_machine"""
	def __init__(self, product, price):
		self.product = product
		self.price = price
		self.stock = 0
		self.balance = 0
	def restock(self, quantity):
		self.stock += quantity
		return "Stock updated."
	def deposit(self, amount):
		self.balance += amount
		return f"You inserted {amount} and your balance is {self.balance}"
	def purchase(self, quantity):
		if quantity > self.stock:
			return "Insufficient quantity"
		else:
			total_price = quantity * self.price
			if total_price > self.balance:
				return "Not enough balance"
			else:
				self.balance -= total_price
				if self.balance != 0:
					return f"Thank you for your purchase\nDon't forget to collect {self.balance} amount."
				else:
					return "Thank you for your purchase"

vm = Vending_machine("Coke", 10)
print(vm.restock(15))
print(vm.deposit(25))
print(vm.purchase(20))
print(vm.purchase(3))
print(vm.purchase(2))