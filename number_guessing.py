import random
def difficulty_level():
  if difficulty == "hard":
    print("You chose hard.")
    attempts = 5
  elif difficulty == "easy":
    print("You chose easy.")
    attempts = 5
  print(f"You have {attempts} attempts remaining to guess the number.")
  return  attempts
def secret_num_creator():
  return random.randint(1, 100)

print("Welcome to the number guessing name!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'hard' or 'easy':\n'").lower()
secret_number = secret_num_creator()
guesses = []
attempts = 0
attempts = difficulty_level()
while True:
        guess = int(input("Make a guess:\n"))
        guesses.append(guess)
        attempts -= 1
        if guess < secret_number:
            print("Too low.")
        elif guess >secret_number:
            print("Too high.")
        elif guess == secret_number:
            print("You got it!")
            break 
        print(f"Numbers you have already used: {guesses}")
        print(f"You have {attempts} attempts remaining to guess the number.")
        if attempts == 0:
            print(f"You lost! The number was {secret_number}.")
            break

