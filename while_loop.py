# demonstration of a while loop that loops 1-100 and displays certain things 
# if they are divisable by 3 , 5 , and both of them 

FIZZ = "Fizz"
BUZZ = "Buzz"
FIZZ_BUZZ = "FizzBuzz"

numbers = 1 
while numbers != 101 :
    if numbers % 3 == 0 and numbers % 5 == 0 :
        print (FIZZ_BUZZ)
    elif numbers % 3 == 0 :
        print (FIZZ)
    elif numbers % 5 == 0 :
        print (BUZZ)
    else :
        print (numbers)
    numbers += 1
