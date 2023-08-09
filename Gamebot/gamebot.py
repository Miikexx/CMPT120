# Choose Your Own Chatbot 
# Mike Kim
# January 29th, 2021

# make a game (survival)

import random

# variables 
possible_starting_point = ["forest","jungle"]
animals = ["bear", "tiger", "lion", "cheetah", "cobra"]


# variables using random function:
animal_selection = random.choice(animals)
spawn_location = random.choice(possible_starting_point)
animal_spawn_location = random.choice(possible_starting_point)
# greet user

print("Hello! This is a survival game! With the right decisions\
 and a little bit of luck, you should be able to beat this game :)")

# explain the game a bit more
print("You will be randomly spawned into a location. \
Then, you will encounter an animal.")
print("-"*10)
print("These are the animals that you will encounter:")

# for loop listing all the animals
for animal in animals:
  print(animal)
print("-"*10)
print("From there, your decision dictates whether if you are going to survive or not!")
print("-"*10)

for i in range(3):
  print("*"*20)
  print("Hello, you will be spawned in a " + spawn_location + "!")
  print("-"*10)
  print("The " + animal_selection + " has spawned in a "+ animal_spawn_location + "." )
  print("-"*10)

  # nested if
  if spawn_location == animal_spawn_location:
    decision = input("What will you do?(run or stay)").lower().strip(" ?!.,")
    print("-"*10)
    if decision == "run":
      print("You have survived!")
    else:
      print("You've died. Make sure to run away next time!")
  else:
    print("-"*10)
    print("There will be no interaction for now. You win!")


# feedback of the game (use upper lower and if un nested)
print("*"*20)
feedback = input("Thanks for playing this game. How would you rate our game?(your options are: good, meh, or bad)").lower().strip(" .?!,")
if feedback == "good":
  print("Awesome!")
elif feedback == "meh":
  print("We will try to improve!")
else:
  print("I'm sorry to hear that. We will try our best to make this game fun!")