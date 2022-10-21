'''  
    PROJECT 1 :  
    
        GAME :-> Snake , Water and Gun 
        
        Rule of the Game :
        Snanke with Water --> Snake Wins
        Snake with Gun --> Gun Wins
        Water with Gun --> Water Wins 
    
'''

import random 


# function for Game 
def Game(comp,user):
    
    # when computer & user input are Same
    if(comp == user):
        print("\nMatch Tie !!")
    
    # all possibilities when computer choose Snake 
    if(comp == 1):
        if(user == 2):
            print("\nOpps ! You Loose the Match !!")
        elif(user == 3): 
            print("\nCongrats ! You Won the Match !!") 
    
    # all possibilities when computer choose Water         
    elif(comp == 2):
        if(user == 1):
            print("\nOpps ! You Loose the Match !!")
        elif(user == 3): 
            print("\nCongrats ! You Won the Match !!")  
            
    # all possibilities when computer choose Gun 
    elif(comp == 3):
        if(user == 1):
            print("\nCongrats ! You Won the Match !!")
        elif(user == 2):  
            print("\nOpps!! You Loose the Match !!")
                         


print("\nEnter \n1 for Snake \n2 for Water \n3 for Gun ")
user = int(input("\nPlease Select according to above menu : "))
comp = random.randint(1,3)

Game(user,comp)


# Displaying Computer Input 

if(comp == 1):
    print("\nComputer Choose  : Snake")
elif(comp == 2):
    print("\nComputer Choose  : Water")
elif(comp == 3):
    print("\nComputer Choose  : Gun")  
    
# Displaying User Input  
  
if(user == 1):
    print("\nYou Choose  : Snake")
elif(user == 2):
    print("\nYou Choose  : Water")
elif(user == 3):
    print("\nYou Choose  : Gun")     
      