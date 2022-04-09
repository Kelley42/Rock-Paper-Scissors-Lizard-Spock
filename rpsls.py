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

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

lizard = '''
       __        
      /..\      
     (    ) \|/ 
 _\___>  <__//`  
 >,---.   ,-'   
      |  . \

'''

spock = '''
      _.-.   .-.
     ( \ \   / )
      \ \ \ / / )
  .-.  \ \ V / /
   \ \ | '   ` |
    \ \|       |
     \         /
'''
# Defs
def print_userchoice(userchoice):
	global rock, paper, scissors, lizard, spock
	if userchoice == "rock":
		print(rock)
	elif userchoice == "paper":
		print(paper)
	elif userchoice == "scissors":
		print(scissors)
	elif userchoice == "lizard":
		print(lizard)
	elif userchoice == "spock":
		print(spock)
	else:
		print("\nIncorrect choice - try again!")
		game()


def print_computerchoice(computerchoice):
	if computerchoice == "rock":
		print(f"Computer chooses: rock{rock}")
	elif computerchoice == "paper":
		print(f"Computer chooses: paper{paper}")
	elif computerchoice == "scissors":
		print(f"Computer chooses: scissors{scissors}")
	elif computerchoice == "lizard":
		print(f"Computer chooses: lizard{lizard}")
	elif computerchoice == "spock":
		print(f"Computer chooses: Spock{spock}")


def playagain():
	question = input("\nPlay again? ").lower()

	questionyes = ["yes", "y"]
	questionno = ["no", "n"]
	
	if any(match in question for match in questionyes):
		game()
	elif any(match in question for match in questionno):
		exit()
	else:
		print("\nIncorrect response - try again!")
		playagain()


def game():		
	userchoice = input("\nRock, paper, scissors, lizard, or Spock? ").lower()
	print_userchoice(userchoice)

	seq = ["rock", "paper", "scissors", "lizard", "spock"]
	computerchoice = random.choice(seq)
	print_computerchoice(computerchoice)

	if computerchoice == "rock":
		if userchoice == "paper" or userchoice == "spock":
			print("You win!")
		elif userchoice == "scissors" or userchoice == "lizard":
			print("You lost.")
		else:
			print("It's a draw.")
	elif computerchoice == "paper":
		if userchoice == "scissors" or userchoice == "lizard":
			print("You win!")
		elif userchoice == "rock" or userchoice == "spock":
			print("You lost.")
		else:
			print("It's a draw!")
	elif computerchoice == "scissors":
		if userchoice == "rock" or userchoice == "spock":
			print("You win!")
		elif userchoice == "paper" or userchoice == "lizard":
			print("You lose.")
		else:
			print("It's a draw.")
	elif computerchoice == "lizard":
		if userchoice == "scissors" or userchoice == "rock":
			print("You win!")
		elif userchoice == "paper" or userchoice == "spock":
			print("You lose.")
		else:
			print("It's a draw.")
	elif computerchoice == "spock":
		if userchoice == "paper" or userchoice == "lizard":
			print("You win!")
		elif userchoice == "rock" or userchoice == "scissors":
			print("You lose.")
		else:
			print("It's a draw.")
	playagain()


# Start game
print("Rock Paper Scissors Game!")

game()
