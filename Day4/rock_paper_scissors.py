import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

your_choice = int(input("What do you choose? Type 1 for Rock, 2 for Paper or 3 for Scissors?\n"))
game_images = [rock, paper, scissor]

print("You chose:")
print(game_images[your_choice - 1])


random_integer = random.randint(1,3)
print("Computer chose:")
print(game_images[random_integer - 1])

if random_integer == your_choice:
  print("#### Result ####")
  print("Draw")

elif (random_integer == 1 and your_choice == 2) or (random_integer == 2 and your_choice == 3) or (random_integer == 3 and your_choice == 1):
  print("##### Result ####")
  print("You win!")

else:
  print("#### Result ####")
  print("You lose!")
