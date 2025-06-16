## a number guessing game 

import random

print("Welcome to the guessing number game!")
print("The system will generate a random number between 1 to 100 and you will have to guess it.") 
print("The fewer the attempts, higher the score.")

round= 0
best_score= None

while True:
    num= random.randint(1,100)
    attempts= 0
    round+=1

    while True:
        
        try: 

            guess= int(input("Enter a number: "))
            
            if guess>num:
                attempts+=1
                print("Too high! Try again")

            elif guess<num:
                attempts+=1
                print("Too low! Try again")

            else:
                attempts+=1
                print("CORRECT! You guessed it in ", attempts, "attempts")
                if best_score is None or attempts<best_score:
                    best_score=attempts
                break

        except ValueError:
            print("Please enter a valid number")
    
    
    restart= input("Do you want to play again? (yes/no): ").lower()
    if restart != "yes":
        break

print("##Game stats:")
print("Your best score is:", best_score)
print("Thanks for playing!")



