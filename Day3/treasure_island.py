print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
crossroad = input("You're at a crossroad, where do you want to go? \nType 'left' or 'right': \n")

if crossroad == "left":
  print("#########################")
  print("You've come to a lake. There is an island in the middle of the lake.")
  swim_or_wait = input("Type 'wait' to wait for a boat. Type 'swim' to swim across.\n")
  if swim_or_wait == "wait":
    print("#########################")
    print("You arrive at the island unharmed. There is a house with 3 doors.")
    door_choice = input("One red, one yellow and one blue. Which colour do you choose?\n")
    if door_choice == 'red':
      print("!!!!!!!!!!!!!!!!!!!!!!!!!")
      print("It's a room full of fire. Game over.")
    elif door_choice == 'yellow':
      print("#########################")
      print("You found the treasure! You win!")
    elif door_choice == 'blue':
      print("!!!!!!!!!!!!!!!!!!!!!!!!!")
      print("You enter a room of beasts. Game over.")

  else:
    print("!!!!!!!!!!!!!!!!!!!!!!!")
    print("You get attacked by an agry trout. Game over.")
else:
  print("!!!!!!!!!!!!!!!!!!!!!")
  print("You fell into a hole. Game Over.")
