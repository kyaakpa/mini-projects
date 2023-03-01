import random

while True:
    randomNumber = random.randint(1,10)
    
    guess = input("Enter a number from 1 to 10: ")

    if guess.isdigit():
        guess = int(guess)
        while True:
            if guess == randomNumber:
                print("You guessed it right. It was " + str(guess) + ".")
                message = input("Do you want to quit the game? ")

            else:
                print("You are incorrect. The random number was " + str(randomNumber) + ".")
                message = input("Do you want to quit the game? ")
        
            if message.lower().strip() == "yes":
                exit()
            else:
                print("Here we go again.")
        
    else: 
        print("Please input a numeric value")
    
    
     


    
        
