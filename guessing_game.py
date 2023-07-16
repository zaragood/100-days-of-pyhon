from guess_art import logo
import random
print(logo)

print("Welcome to the number guessing game!\n")
print("I am thinking of a number between 1 and 100! can you guess the number?")

#generate a random number
random_number = random.randint(1, 101)
print(random_number)

#number of attempts to give the user depending on the level they choose
invalide = True
while invalide:
    level = input("Choose difficulty. Type 'easy' or hard: ").lower()

    if level == "easy":
        attempt = 5
        print(f"You have {attempt} atttempts.")
    elif level == "hard":
        attempt = 3
        print(f"You have {attempt} attempts.")
    else:
        print("invalid response")
        invalide = True
    invalide = False
   
#prompting the user to keep playing as long as they till have attemps left and has not guessed the right number 
game_over = False

while not game_over:
    guess = int(input("Make a guess: "))
    
    #checking if random_number is  greater than the user's guess
    if random_number > guess:
        #for every wrong attempt we want to keep reducing their attempt by 1
        attempt -= 1
        print("Too low\nGuess again.")
        print(f"You have {attempt} remaining to guess the number")
        if attempt == 0:
            print("You Lost! Game Over")
            game_over = True
    elif random_number < guess:
        attempt -= 1
        print("Too high\nGuess again.")
        print(f"You have {attempt} remaining to guess the number")
        if attempt == 0:
            print("You Lost! Game Over")
            game_over = True
    else:
        print(f"You got it! The answer was {random_number}.")
        game_over = True
        
        
        
        
#second program that does thesame thing. just uncomment it and use it

# from random import randint
# from art import logo

# EASY_LEVEL_TURNS = 10
# HARD_LEVEL_TURNS = 5

# #Function to check user's guess against actual answer.
# def check_answer(guess, answer, turns):
#   """checks answer against guess. Returns the number of turns remaining."""
#   if guess > answer:
#     print("Too high.")
#     return turns - 1
#   elif guess < answer:
#     print("Too low.")
#     return turns - 1
#   else:
#     print(f"You got it! The answer was {answer}.")

# #Make function to set difficulty.
# def set_difficulty():
#   level = input("Choose a difficulty. Type 'easy' or 'hard': ")
#   if level == "easy":
#     return EASY_LEVEL_TURNS
#   else:
#     return HARD_LEVEL_TURNS

# def game():
#   print(logo)
#   #Choosing a random number between 1 and 100.
#   print("Welcome to the Number Guessing Game!")
#   print("I'm thinking of a number between 1 and 100.")
#   answer = randint(1, 100)
#   print(f"Pssst, the correct answer is {answer}") 

#   turns = set_difficulty()
#   #Repeat the guessing functionality if they get it wrong.
#   guess = 0
#   while guess != answer:
#     print(f"You have {turns} attempts remaining to guess the number.")

#     #Let the user guess a number.
#     guess = int(input("Make a guess: "))

#     #Track the number of turns and reduce by 1 if they get it wrong.
#     turns = check_answer(guess, answer, turns)
#     if turns == 0:
#       print("You've run out of guesses, you lose.")
#       return
#     elif guess != answer:
#       print("Guess again.")


# game()

