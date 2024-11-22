# testing out python and simple functions (# is used for comments)
# python uses snake_case 
# classes are CamelCased 
# constants are UPPER_CASE 
# ; not nessessary 

# to write output to the user , use print ()
print ("Hello World\n") 

#assignig variables with values , automatically given data type 
int1 = 10 
float1 = 10.5

# str() converts whatever variable to a string 
# int() , float() , etc does the same 
print (str(int1) + " is an integer") 
print (str(float1) + " is a float") 

# using strings 
string1 = "\nCasey you are learning Python." 
print (string1 + '\n') ;

# get input from the user 
# display input from user to user 
name = input("What is your name? ") 
age = int(input("What is your age? ")) 
major = input("What is your major? ") 
print ("\nYour Personal Info: ") ;
print ("Name: " + name) 
print ("Age:" , age) 
print ("Major: " + major) 

# if statement in python 
# indentations instead of {} like in C++ and Java 
# if and else block ends at first line that is not indented 
# semicolon needed after conditions 
age1 = int(input("\nWhat is your age? ")) 
if age1 >= 18 :
    print ("You are an Adult. \n") 
else :
    print ("You are a minor. \n") 

# test while loop
# no () , uses while statement then semicolon 
# incrementation and decrementation is done manually , ++ and -- does not exist
number = 3 
count = 0 
while count < number :
    print (count) 
    count += 1 ;

# try a for loop 
# use end = ' ' to skip the automatic newline when using print 
# [] creates a list 
print ("\nlets count to 5: ") ;
number_list = {0 , 1 , 2 , 3 , 4 , 5}
for number in number_list :
    print (number, end = ' ') ;
    
# use a for loop to create a list with user input 
# [] makes a list 
# for _ is a throwaway character when the variable next to for is not needed 
input_size = int(input("\n\nHow many numbers is in your list? ")) 
number_list1 = [] 
number_count = 1
for _ in range(input_size) :
    # use f and {} around a variable to include it in a string statement 
    number_list_input = int(input(f"Enter in number {number_count}: ")) 
    number_list1.append (number_list_input) 
    number_count += 1 
# display the list 
print ("\nYour number list is:" , number_list1 , end = ' ') 



    