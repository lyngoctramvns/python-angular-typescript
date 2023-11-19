import sys
import random

user_input = input('Enter either \n 1. Rock or \n 2. Paper or \n 3. Scissors\n\n')
computer_choice = random.choice(["Rock","Paper","Scissors"])
x = "Rock"
y = "Paper"
z = "Scissors"


# Alternative: if user_input != x and user_input != y and user_input != z:
if user_input not in (x, y, z):
	sys.exit("Enter either Rock, Paper or Scissors. Remember the correct capitalization!")
elif user_input == computer_choice:
	print("You choose " + user_input + ".")
	print("Computer choose " + computer_choice + ".")
	print('We have a tie!')
else:
	print("You choose " + user_input + ".")
	print("Computer choose " + computer_choice + ".")
	if user_input == x and computer_choice == y:
		print("Computer wins!")
	elif user_input == x and computer_choice == z:
		print("You wins!")
	elif user_input == y and computer_choice == x:
		print("You wins!")
	elif user_input == y and computer_choice == z:
		print("Computer wins!")
	elif user_input == z and computer_choice == x:
		print("Computer wins!")
	else:
		print("You win!")