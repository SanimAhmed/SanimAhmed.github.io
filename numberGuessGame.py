import random
import os
import logo
def guess():
    Guess = int(input("Make a guess : "))
    return Guess


moreGame = True
start =True
while moreGame:
    actualNum = random.randint(1,100)
    if start:
        anotherTurn= "y"
        print("\nWelcome to the Number Guessing Game!!\n")
        
    else:    
        anotherTurn = input("You want to play again? Y or N?")
        os.system('cls')
    if anotherTurn=="n":
        moreGame=False
    elif anotherTurn=="y":
        print(logo.logo)
        start = False
        diff = input("Choose your difficulty?easy or hard?")
        if diff=="easy":
            os.system('cls')
            count=10
            while count>0:
                print(f"You have {count} attempts remaining to guess the number.")
                Guess = guess()
                if Guess>actualNum:
                    print("Too High!\n Guess again!")
                    count-=1
                elif Guess<actualNum:
                    print("Too Low!\n Guess again!") 
                    count-=1
                elif Guess==actualNum:
                    print("You Guessed it correct!! You Win!!") 
                    print(logo.Winner)  
                    break    
                               
        
        if diff=="hard":
            os.system('cls')
            count=5
            while count>0:
                print(f"You have {count} attempts remaining to guess the number.")
                Guess = guess()
                if Guess>actualNum:
                    print("Too High!")
                    count-=1
                    if count>0:
                        print("Guess again!")
                elif Guess<actualNum:
                    print("Too Low!") 
                    count-=1
                    if count>0:
                        print("Guess again!")
                elif Guess==actualNum:
                    print("You Guessed it correct!! You Win!!") 
                    print(logo.Winner)  
                    break    
                                       
        if count==0 :               
                print("You Lose !!!") 
                print(f"The actual Number is : {actualNum}")        
                print(logo.loser)