# menu driven calculator program with python 
# uses functions 

# main function 
# asks all the questions 
def main () :
    print ("Choose your application ")
    print ("Menu: ")
    print ("A. Addition")
    print ("B. Subtraction")
    print ("C. Multiplication")
    print ("D. Division")
    print ("E. Squared")
    # gets the character from the user and if they entered in a lowercase letter , uses .upper() to make upper
    selection = input("Your selection: ").upper()
    
    # if , elif , and else statement to check which selection was chosen
    if selection == 'E' :
        num1 = int(input("\nEnter a number: "))
        print (f"{num1} squared is {square (num1)}") # calls square function
    # checks if the user choice is between A and E
    elif 'A' <= selection <= 'D' :
        # this is a way to get a user input twice , using map and split 
        num1 , num2 = map(float,input("\nEnter two numbers seperated by a space: ").split())
        if selection == 'A' :
            print (f"{num1} plus {num2} is {addition(num1 , num2)}") # calls addition function
        elif selection == 'B' :
            print (f"{num1} minus {num2} is {subtraction(num1 , num2)}") # calls subtraction function
        elif selection == 'C' :
            print (f"{num1} times {num2} is {multiplication(num1 , num2)}") # calls multiplication function
        elif selection == 'D' :
            print (f"{num1} divided by {num2} is {division(num1 , num2)}") # calls division function
    else :
            print ("\nInvalid menu selection") # if they did not enter A B C D or E 
        
    print ("\nEnd of Program")
    
# function for addition
def addition (num1 , num2) :
    return num1 + num2 

# function for subtraction 
def subtraction (num1 , num2) :
    return num1 - num2 
    
# fuction for multiplication
def multiplication (num1 , num2) :
    return num1 * num2
    
# function for division 
def division (num1 , num2) :
    return num1 / num2 
        
# function for squaring 
def square (num1) :
    return pow (num1 , 2)

# call main function at the end 
main ()
