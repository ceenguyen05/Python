# Program Purpose :
# Inventory management program that uses loops, exceptions and dictionaries to update 
# items in an inventory

# function get_menu makes sure a valid input was selected from the user
def get_menu () :
    menu_choice = 0 # declare a int variable and this will get returned later 
    choices = [ 1 , 2 , 3 , 4 , 5 ] # list of the number choices
    while True : # infinate loop until the user enters a choice 1-5
        try : # trys and gets a number 1-5 , if an int but not 1-5 , display error message 
            print("Inventory Menu")
            print("1. Add Item")
            print("2. Remove Item")
            print("3. Update Quantity")
            print("4. View Inventory")
            print("5. Exit Menu")
            menu_choice = int(input("Your menu choice: "))
            
            if menu_choice in choices :
                return menu_choice # if 1-5 return to the function and break the infinite loop
            else :
                print ("\nInvalid input, please enter a choice from the menu, try again. \n")
                
        except ValueError : # catches input that isnt an int 
            print ("\nInvalid input, please enter a choice from the menu, try again.\n")

def main () :
    menu_choice = get_menu() 
    item = ""
    quantity = 0
    
    # dictionary for the inventory
    Inventory = {}
    
    # infinite loop 
    while True :
        # break the infinite loop when the user enters 5 for exit 
        if menu_choice == 5 :
            print ("\nEnd of program.")
            break 
        else :
            print ()
            # ask the user for the item and quantity and add it to the inventory dictionary
            if menu_choice == 1 :
                item = input("What is the item you would like to add? ")
                try :
                    quantity = int(input("How much would you like to add? "))
                    print ()
                    if quantity < 0 :
                        print ("Cannot have a negative quantity amount. \n")
                except ValueError :
                    print("Invalid quantity input entered. \n")
                if item in Inventory :
                    Inventory [item] += quantity
                else :
                    Inventory [item] = quantity 
                
            # ask the user what item they would like to remove 
            elif menu_choice == 2 :
                item = input("What item would you like to remove? ")
                print ()
                try :
                    del Inventory[item]
                except KeyError :
                    print ("Item doesn't exist. \n")
            
            # ask the user what would they like to update and ask them for the amount    
            elif menu_choice == 3 :
                item = input("What is the item you would like to update? ")
                if item in Inventory :
                    try :
                        quantity = int(input("What is the quantity you would like to add / remove? "))
                        print()
                        Inventory [item] += quantity 
                        if Inventory [item] < 0 :
                            Inventory [item] = 0
                    except ValueError :
                        print ()
                        print ("Invalid quantity amount inputted. \n")
                else :
                    print ("\nItem doesn't exist. \n")
                    
            # Display the current inventory 
            elif menu_choice == 4 :
                if Inventory :
                    print ("Current Inventory")
                    for item0 , quantity0 in Inventory.items() :
                        print (f"Item: {item0} , Amount: {quantity0}")
                    print()
                else :
                    print ("Inventory is currently empty. \n")
                
            menu_choice = get_menu() # prompt the menu to the user again 

main ()
