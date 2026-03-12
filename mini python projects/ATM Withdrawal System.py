# atm withdrawal checker that asks a user to enter for withdrawal amount and checkIf withdraw > balance → Insufficient fundsElse → Transaction successful
balance = 1000

print("Welcome to the ATM")
print("Your balance is:", balance)

withdraw = float(input("Enter amount to withdraw: "))

if withdraw > balance:
    print("Insufficient funds")
elif withdraw <= 0:
    print("Invalid amount")
else:
    balance = balance - withdraw
    print("Transaction successful")
    print("Remaining balance:", balance)