# All classes have a function called __init__(), which is always executed when the class is being initiated.
#Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:

class BankAccount:
    def __init__(self, ac_no, bal):
        self.ac_no = ac_no
        self.bal = bal



accounts = [
    BankAccount(101, 150000),
    BankAccount(102, 150000),
    BankAccount(103, 150000)
]

ac_no = int(input("Enter Your Account Number: "))
withdrawal_amt = int(input("Enter Amount You Want to Withdraw: "))

account = None
for acc in accounts:
    if acc.ac_no == ac_no:
        account = acc
        break

if account is None:
    print("Invalid account number.")
else:
    if withdrawal_amt > account.bal:
        print("Balance is low.")
    else:
        account.bal -= withdrawal_amt
        print(f"New balance: {account.bal}")



#Sencond sample code
# account_number = '112' #'7069056944'
# withdrawal_amt = int(input("Enter your required amt :"))
# balance = 150000
# input_account = int(input("Enter your account number :"))

# if (input_account != int(account_number)):
#   print("Invalid account number.")
# elif (withdrawal_amt > balance):
#   print("Insufficient funds.")
# else:
#   balance -= withdrawal_amt
#   print(f"New balance: {balance}")


#Third sample
# # Create two bank accounts
# BankAccount1 = BankAccount(101, 150000)
# BankAccount2 = BankAccount(102, 150000)

# # Input account number and withdrawal amount
# ac_no = int(input("Enter Your Account Number: "))
# withdrawal_amt = int(input("Enter Amount You Want to Withdraw: "))

# # Check if the account number matches any defined accounts
# if ac_no == BankAccount1.ac_no:
#     account = BankAccount1
# elif ac_no == BankAccount2.ac_no:
#     account = BankAccount2
# else:
#     print("Invalid account number.")
#     exit()  # Exit the program if the account number is invalid

# # Check if the withdrawal amount is greater than the balance
# if withdrawal_amt > account.bal:
#     print("Insufficient funds.")
# else:
#     account.bal -= withdrawal_amt
#     print(f"New balance: {account.bal}")
