import random


def guess_number(x):
    ans = random.randint(1,x)
    guessed = 0
    
    while guessed != ans:
        guessed = int(input("guess a number between 1 and 10"))
        if guessed < ans:
            print("dedicated answer is higher, try again") 

        elif guessed > ans:
            print("dedicated answer is lower, try again")
        
        
    print("well done, you have guessed the number correctly")

        
    




def computer_guess(x):
    low = 1
    high = x
    count = 0
    decision = ""
    
    while decision != "C":
        
         if low != high:
            guess =  random.randint(low, high)
         
         else: 
            #in the case that both low and high become the same number
            guess = high or low
            
         decision = input(f"throughout 1 to 100, i guess that {guess} is your number. H) if number is a higher bound. L) if number is a lower bound. C) if i have guessed your number correctly.")
         count += 1 
        
        
        
         if decision == "H":
            low = guess + 1 
            




         elif decision == "L":
            high = guess - 1
            


    print(f"it had taken me {count} guesses to find your number.")
    





x = int(input("hello, would you like to 1) guess the computers number 2) challenge the computer to guess your number "))


while x != 1 and x != 2:
    print("invalid syntax, try again")
    x = int(input("hello, would you like to 1) guess the computers number 2) challenge the computer to guess your number "))
   
if x == 1:
    guess_number(10)

elif x == 2:
    computer_guess(100)




    