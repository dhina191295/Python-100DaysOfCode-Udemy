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

# Write your code below this line 👇

user = None
computer = None
result = None

input1 = input("What type do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")

if input1 == "0":
    user = "rock"
    print(rock)
elif input1 == "1":
    user = "paper"
    print(paper)
elif input1 == "2":
    user = "scissors"
    print(scissors)

random1 = random.randint(0, 2)
# print(random1)
print("Computer chose")
if random1 == 0:
    computer = "rock"
    print(rock)
elif random1 == 1:
    computer = "paper"
    print(paper)
elif random1 == 2:
    computer = "scissors"
    print(scissors)

if user == computer:
    print("DRAW")
elif user == "rock" and computer == "scissors":
    print("You won")
elif user == "scissors" and computer == "paper":
    print("You won")
elif user == "paper" and computer == "rock":
    print("You won")
else:
    print("You lose")
