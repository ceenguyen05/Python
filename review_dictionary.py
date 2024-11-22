# Review of Dictionaries

# Declaration of a Dictionary 
Surnames = {
    "Casey" : "Nguyen" ,
    "Erin" : "Cho"
}

userString = input ("Enter your name: ") 
# Displays the string from the dictionary , returns not found if not found in dictionary 
print ("Your last name is: " + Surnames.get(userString , "Not Found")) 