# demonstration of a for loop 

number_names = int (input ("How many people are in your group? ")) # get number of students 

names_list = [] # create an empty lisr 

# for loop to ask the user to enter names of the group members 
# adds the name to a list 
for _ in range(number_names) :
    name = input ("Enter their name: ")
    names_list.append(name)
    
# display the names in the group 
print ("\nTeamates in Your Group: ")
# displays all the names in the names_list list 
for names in names_list :
    print (names)