# import random

# topRange = input("Type the upper limit of the range: ")

# if topRange.isdigit():
#     topRange = int(topRange)
    
#     if topRange <= 0:
#         print("Type a number larger than zero")
#         quit()
# else:
#     print("Error, please type in a valid number.")
#     exit()

# r = random.randrange(0, topRange)

# guesses = 0
# while True:
#     guesses  += 1
#     userGuess = input("make a guess: ")
#     if  userGuess.isdigit():
#         userGuess = int(userGuess)
#     else: 
#         print("Invalid Input! Please enter a number.")
#         continue
        
#     if r == userGuess:
#         print("Congratulations, you guessed correctly! The computer's number was",r,".")
#         break
#     elif userGuess < r:
#             print("Your guess is too low.")
#     else:
#         print("Your guess is too high.")
                
# print("You get it in ",guesses,"tries.")
        
import random

def get_user_input():
    while True:
        user_input = input("Make a guess: ")
        if user_input.isdigit():
            return int(user_input)
        else:
            print("Invalid input! Please enter a number.")

def play_guessing_game(top_range):
    secret_number = random.randrange(1, top_range + 1)
    guesses = 0
    while True:
        guesses += 1
        user_guess = get_user_input()
        if user_guess == secret_number:
            print(f"Congratulations, you guessed correctly! The secret number was {secret_number}.")
            break
        elif user_guess < secret_number:
            print("Your guess is too low.")
        else:
            print("Your guess is too high.")
    return guesses

def main():
    try:
        top_range = int(input("Type the upper limit of the range: "))
        if top_range <= 0:
            print("Type a number larger than zero")
            return
        num_guesses = play_guessing_game(top_range)
        print("You got it in", num_guesses, "tries.")
    except ValueError:
        print("Error: Please type in a valid number.")

if __name__ == "__main__":
    main()
