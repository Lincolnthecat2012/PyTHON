import random 
random_number = random.randint(1, 100) 
guessedstr = input('Please guess any number between 1 and 100 ') 
guesses = 0 
guessed = int(guessedstr) 

def guess_again(random_number, guesses): 

    guessedstr = input('Please guess any number between 1 and 100 ') 
    guessed = int(guessedstr) 
    guesses += 1
    if guessed == random_number: 
        print ("Well Done! You Got It Right! " ) 
        print (f"You took, {guesses} guesses") 
        
    if guessed != random_number: 
        if guessed >= random_number: 
            print("Nice Try But Guess Lower") 
        if guessed <= random_number: 
            print("Nice Try But Guess Higher") 
        guess_again(random_number, guesses) 

guess_again(random_number,guesses)