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

#Write your code below this line 👇
choices = [rock, paper, scissors]
while True:
    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
    if user_choice >= 0 and user_choice < 3:
        break

random_choice = random.randint(0, 2)
print("Your choice is:")
print(choices[user_choice])
print("computer choice is:")
print(choices[random_choice])

if user_choice == 0 and random_choice == 2:
    print("YOU WIN")
elif user_choice == 2 and random_choice == 0:
    print("YOU LOSE")
elif user_choice < random_choice:
    print("YOU LOSE")
elif random_choice < user_choice:
    print("YOU WIN")
else:
    print("IT'S A DRAW")