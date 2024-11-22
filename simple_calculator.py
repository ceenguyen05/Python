# program purpose 
# ask the user what they want to do 
# get two numbers 
# display the numbers and result 
# all using functions

# main function 
# displays the menu and displays the results to the user 
def main () :
    print ("Select from the menu below")
    print ("Menu: ")
    print ("A. Addition")
    print ("B. Subtraction")
    print ("C. Multiplication")
    print ("D. Division")
    selection = get_selection ()
    number1 , number2 = get_numbers (selection)
    if (selection == 'A') :
        print (f"{number1} + {number2} = {get_addition(number1 , number2)}")
    elif (selection == 'B') :
        print (f"{number1} - {number2} = {get_subtraction(number1 , number2)}")
    elif (selection == 'C') :
        print (f"{number1} * {number2} = {get_multiplication(number1 , number2)}")
    else :
        print (f"{number1} / {number2} = {get_division(number1 , number2)}")
        
# this function gets the menu choice from the user 
# will not exit out of question until a valid menu choice is selected 
def get_selection () :
    menu_choices = {'A' , 'B' , 'C' , 'D'} # defing a bracket of valid choices 
    while True : # keeps running until something returns 
        uc = input("Selected Choice: \n").upper() # turns all characters into upper 
        if (len(uc) == 1 and uc in menu_choices) : # checks if user entered one character and in menu choice 
            return uc  # returns the selection , exiting the loop
        else :
            print ("Select a valid menu choice\n") # keeps asking user for a valid menu choice 

# this function asks the user for two numbers 
# checks for division by zero as well
def get_numbers (s) :
    number1 = float(input("\nEnter a number: "))
    while True : # loops if division by 0 occurs 
        number2 = float(input("Enter a number: "))
        if (s == 'D' and number2 == 0) :
            print ("Cannot divide by 0, enter another number.")
        else :
            return number1 , number2

# these functions return the result of the operators 
def get_addition (n1 , n2) :
    return n1 + n2 
    
def get_subtraction (n1 , n2) :
    return n1 - n2 
    
def get_multiplication (n1 , n2) :
    return n1 * n2 
    
def get_division (n1 , n2) :
    return n1 / n2

# calls main that executes everything 
main ()
