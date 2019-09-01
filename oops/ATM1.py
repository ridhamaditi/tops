class ATM:
	"""docstring for ATM"""
	def __init__(self, pin, balance):
		self.__pin = pin
		self.balance = balance
	def display_bal(self, pin):
		if pin == self.__pin:
			return f"Current Balance: {self.balance}"
		else:
			return "Incorrect PIN"
	def deposit(self, pin, amount):
		if pin == self.__pin:
			self.balance += amount
			return f"Current Balance: {self.balance}"
		else:
			return "Incorrect PIN"
	def withdraw(self, pin, amount):
		if pin != self.__pin:
			return "Incorrect PIN"
		elif amount > self.balance:
			return "Insufficient Balance"
		else:
			self.balance -= amount
			return f"Current Balance: {self.balance}"
	def change_pin(self, old_pin, new_pin):
		if old_pin == self.__pin:
			self.__pin = new_pin
			return "PIN Changed."
		else:
			return "Incorrect PIN"
	def d_pin(self):
		return self.__pin

a = ATM(1234, 50000)
print("Display Balance through correct PIN")
print(a.display_bal(1234))
print("Display Balance through incorrect PIN")
print(a.display_bal(123))

print("\nDeposit through correct PIN")
print(a.deposit(1234, 10000))
print("Deposit through incorrect PIN")
print(a.deposit(123, 10000))

print("\nWithdraw amount through correct PIN and sufficient balance")
print(a.withdraw(1234, 10000))
print("Withdraw amount through correct PIN and insufficient balance")
print(a.withdraw(1234, 100000))
print("Withdraw amount through incorrect PIN and sufficient balance")
print(a.withdraw(123, 10000))

print("\nChanging pin with correct existing PIN")
print(a.change_pin(1234, 5678))
print("Changing pin with incorrect existing PIN")
print(a.change_pin(1234, 5678))

a.__pin = 9876
print(a.__pin)
print(a.d_pin())