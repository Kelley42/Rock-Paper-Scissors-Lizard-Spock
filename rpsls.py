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
	userchoice = input("\nRock, paper, scissors, lizard, or Spock? ").strip(" ").lower()
	print_userchoice(userchoice)

	seq = ["rock", "paper", "scissors", "lizard", "spock"]
	computerchoice = random.choice(seq)
	print_computerchoice(computerchoice)

	win = "You win!"
	lose = "You lose."
	draw = "It's a draw."
	
	row1 = [draw, lose, win, win, lose]
	row2 = [win, draw, lose, lose, win]
	row3 = [lose, win, draw, win, lose]
	row4 = [lose, win, lose, draw, win]
	row5 = [win, lose, win, lose, draw]
	
	grid = [row1, row2, row3, row4, row5]

	y = int(seq.index(computerchoice))
	x = int(seq.index(userchoice))
	print(grid[x][y])

	playagain()


# Start game
print("\nRock Paper Scissors Lizard Spock Game!")

game()
