# While and If/Else Practice 
# Ininite Loop if not positive number 

while (True) :
    number = int (input ("Enter a postive integer: "))
    if number > 0 :
        break 
    else :
        print ("That is not positive, try again.")
        
print (str(number) + " is positive")