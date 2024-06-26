from random import randint

accounts = {}

def createAccount():

    randomId = randint(1, 99999)
    while randomId not in accounts:
        balance = input("Enter balance > ")
        accounts[int(randomId)] = int(balance)

def checkBalance(Id):
    if Id in accounts:
        print(f"The balance is {accounts[Id]}")
    else:
        print("Id unidentified")

def withdraw(id,amount):
    if id in accounts:
        rem = accounts[id] - amount
        accounts[id] = rem
        if rem < 0:
            print(f"You have utang na. Your balance now is {rem}")
        else:
            print(f"The remaining balance is {rem}")

def deposit(id,amount):
    if id in accounts:
        rem = accounts[id] + amount
        accounts[id] = rem
        print(f"Your balance now is {rem}")
            
def deleteAccount(id):
    if id in accounts:
        del accounts[id]
        print(f"{id} this account is deleted"
        )
    else:
        print("Unrecognized Id")

while True:
    
    print(accounts)
    print("""
What do want to do
    Functions        keywords
"Create Account" =  Create
"Delete Account" =  Delete
"Check Balance"  =  Check       
"Withdraw"       =  Withdraw
"Deposit"        =  Deposit
"Exit"           =  Exit
          
""")
    user = input("Enter keyword > ")
    if user.capitalize() == "Create":
        createAccount()

    elif user.capitalize() == "Delete":
        id = int(input("Enter the ID you want to delete >"))
        deleteAccount(id)

    elif user.capitalize() == "Check":
        id = int(input("Enter the ID you want to check the balance >"))
        checkBalance(id)

    elif user.capitalize() == "Withdraw":
        id = int(input("Which ID do you want to withdraw money from? "))
        amount = int(input("Enter amount> "))
        withdraw(id,amount) 

    elif user.capitalize() == "Deposit":
        id = int(input("Which ID do you want to deposit money from? "))
        amount = int(input("Enter amount> "))
        deposit(id,amount)
        
    elif user.capitalize() == "Deposit":
        exit
    else:
        print("Enter the right keyword")