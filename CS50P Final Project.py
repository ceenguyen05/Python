# Program Purpose :
# This is a bank account program
# Purpose is for you to check your account, make deposits and withdrawals

# ask the user how much they have in their account at the start for the sake of this project
# ask the user for their info for the sake of the program
# for the sake of the program, assume the user is not in debt initially
# In the main function , display menu options and then call certain functions.
# Automatically print a receipt after they are done making transactions
# after every transaction, ask the user if they wanna make more transactions
# handles user errors

def main () :
    # ask the user for their name and bank amount
    name = input ("What is your name? ")
    initial = get_initial ()

    # initializ variables
    repeat = ""
    amount = 0

    # create an instance of the BankAccount class and initialize
    bank_class = BankAccount (name , initial)

    # prompt the menu until the user does not want to make another tranaction
    while repeat != "no":
        print ("\nWhat would you like to do today? ")
        print ("1. Check Balance ")
        print ("2. Make a Deposit ")
        print ("3. Make a Withdraw ")
        choice = input("Your Selection: ")
        if choice == "1" :
            bank_class.display_info()
        elif choice == "2" :
            amount = check_deposit()
            bank_class.deposit(amount)
        elif choice == "3" :
            amount = check_withdraw()
            bank_class.withdraw(amount)
        else :
            print ("Invalid Choice Selected.")

        repeat = check_result ()

    print("\nThank you for using our services, Here is your digitial receipt")
    print("Transactions: ")
    bank_class.display_transactions()

# the class for the users bank account
# can manage all info here all at once
class BankAccount :
    # initialize the name and initial balance , create a list to handle transactions (receipt)
    def __init__ (self , name , initial) :
        self.name = name
        self.balance = initial
        self.transactions = []

    def deposit (self , amount) :
        self.balance += amount # add the amount to the balance
        self.transactions.append(f"Deposit: ${amount:.2f} , New Balance: ${self.balance:.2f}") # add transaction to list

    def withdraw (self , amount) :
        if amount > self.balance : # if trying to withdraw more than in balance , error messege
            print ("\nInsufficient Funds")
        else :
            self.balance -= amount # decrease from balance
            self.transactions.append(f"Withdraw: ${amount} , New Balance: ${self.balance:.2f}") # add transaction to list

    # dislays the users name and balance
    def display_info (self) :
        print (f"\nName: {self.name}")
        print (f"Balance: ${self.balance:.2f}")
        self.transactions.append (f"Checked Balance , Balance: {self.balance:.2f}")

    # displays the users transactions
    def display_transactions (self) :
        for count , transaction in enumerate(self.transactions , start = 1) :
            print (f"{count}. {transaction}")
        print ()

# infinite loops until a valid amount has been enetred
def get_initial () :
    while True :
        try :
            initial = float(input("What is the current balance in your account? $"))
            if initial < 0 :
                print("\nPlease enter a non-negative number, try again.")
            else :
                return initial
        except ValueError :
            print ("\nPlease enter a valid number amount, try again.")

# handles amount checking for deposits
def check_deposit () :
    while True :
        try :
            deposit = float(input("\nHow much would you like to deposit? $"))
            if deposit <= 0 :
                print ("Please Deposit an amount higher than 0, try again.")
            else :
                return deposit
        except ValueError :
            print ("Please enter a valid number, try again.")


# handles amount checking for withdrawals
def check_withdraw () :
    while True :
        try :
            withdraw = float(input("\nHow much would you like to withdraw? $"))
            if withdraw <= 0 :
                print ("Please Withdraw an amount higher than 0, try again.")
            else :
                return withdraw
        except ValueError :
            print ("Please enter a valid number, try again.")

# ask the user if they want to make more transactions
def check_result () :
    result = input("\nWould you like to make another transaction today? (Yes or No) ").strip().lower()
    if result in ("yes", "no"):
        return result
    print("Please answer Yes or No, try again.")
    return check_result()

# Only call main when ready and valid
if __name__ == "__main__":
    main()
