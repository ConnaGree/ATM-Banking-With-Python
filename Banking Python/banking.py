
class Bank:
	
	def __init__(self, initial_amount=0.00):
		self.balance = initial_amount
		
	def log_transaction(self, transaction_string):
		with open("transactions.txt", "a") as file:
			file.write(f'{transaction_string} \t\t {self.balance}\n')
		
	def withdrawal(self, amount):
		try:
			amount = float(amount)
		except ValueError:
			amount = 0
		if amount: 
			self.balance = self.balance - amount
			self.log_transaction(f'Withdrew {amount}')
	
	def deposite(self, amount):
		try: 
			amount = float(amount)
		except ValueError:
			amount = 0
		if amount: 
			self.balance = self.balance + amount
			self.log_transaction(f'Deposited {amount}')
	

account = Bank(50.50)
account.deposite(10)
account.withdrawal(20)

		
while True:
	try:
		action = input("What kind of action to do you want to take?")
	
	except KeyboardInterrupt:
		print("Leaving the ATM\n")
		break
	if action in ["withdrawal", "deposite"]:
		if action == "withdrawal":
			amount = input("How much do you want to take out?")
			account.withdrawal(amount)
		
		else: 
			amount = input("How much do you want to put in?")
			account.deposite(amount)
		
		print(f"Your balance is, {account.balance}")
