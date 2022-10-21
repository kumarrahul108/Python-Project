'''
    PROJECT 2 :
    
        GAME : -> Generate any Random Number and make it guess by the user until user guesses it Right.
                   Also , print in how many guesses user gussed it Right. 
                   
                   If user enters a number higher than the random number --> print : Too High
                   If user enters a number lower than the random number --> print : Too Low 
                   
                   Store guesses in a text file "highscore" 

'''


# module for generating random number
import random

ranNum = random.randint(1,100)
print(ranNum)
guess = 0


while(True): 
    
    user = int(input("\nEnter the Number  :  "))
    
    if(ranNum == user):
        print("Congrats ! You guessed the right number")
        break
    
    elif(user > ranNum):
        print("Opps ! You have entered High Value . Please keep this in mind while entering number next time !")
        
    elif(user < ranNum):
        print("Opps ! You entered Low Value . Please keep this in mind while entering number next time !")  
        
    guess += 1
    
    
print(f"\nYou have guessed it in {guess} times") 


with open("highscore.txt","r") as f:
    data = int(f.read())
    
if(data > guess):
    with open("highscore.txt","w")as f:
        f.write(str(guess))                  





