# Number Guessing Game
# The program generates a random number between 1 and 100.
# The player keeps guessing until the correct number is found.

import random

# Function to display the game title
def display_title():
  print("Welcome to the Number Guessing Game!")



# Function to display the end message
def end_message():
  print("\nThanks for playing!")



# Function to get a valid guess from the user
def guess_number():
 while True:
    try:
      guess=int(input("\nYour guess:"))
      return guess
    except ValueError:
      print("\nInvalid input. Please enter a number between 1 and 100.")
      

# Function containing the main game logic
def play_game():
  num=random.randint(1,100)
  count=1
  print("\nI'm thinking of a number between 1 and 100.")
  guess=guess_number()

  # Loop until the correct number is guessed
  while guess!=num:
    if guess<num:
      print("Too low. Guess again.\n")
    else:
      print("Too high. Guess again.\n")
    guess=guess_number()
    count+=1
  print(f"\nCorrect! You guessed the number in {count} tries.")
  

# Main function to control the game flow
def main():
  display_title()
  response="y"
  while response.lower()=="y":
    play_game()
    response=input("\nDo you want to play again (y/n):")
  end_message()


# Standard Python practice to run main function
if __name__=="__main__":
  main()
