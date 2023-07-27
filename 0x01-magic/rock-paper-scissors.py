# Enter in input : 0 for rock, 1 for paper and 2 for scissors
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
game_option=[rock,paper,scissors]
computer_choose=random.randint(0,2)
user_choose=int(input("What is your choose? 0 for rock, 1 for paper and 2 for scissors?"))

if user_choose>=3 or user_choose<0:
    print("Your entered invalid Number")
else:
    print(f"Computer Choose \n {game_option[computer_choose]}")
    print(f"User Choose \n {game_option[user_choose]}")
    if game_option[computer_choose]== game_option[user_choose]:
        print(f"Computer Choose  \n {game_option[computer_choose]}")
        print(f"User Choose \n {game_option[user_choose]}")
        print("Game Draw !! ")
        print("And if you liked it, don't forget to give a (+1) like! Thank you!")
    elif game_option[computer_choose]==rock and game_option[user_choose]==paper:
        print("You Win ***")
        print("And if you liked it, don't forget to give a (+1) like! Thank you!")
    elif game_option[computer_choose]==rock and game_option[user_choose]==scissors:
        print("You Lose")
    elif game_option[computer_choose]==paper and game_option[user_choose]==rock:

        print("You Lose")
    elif game_option[computer_choose]==paper and game_option[user_choose]==scissors:
        print("You win")
        print("And if you liked it, don't forget to give a (+1) like! Thank you!")
    elif game_option[computer_choose]==scissors and game_option[user_choose]==rock:
        print("You win")
        print("And if you liked it, don't forget to give a (+1) like! Thank you!")
    elif game_option[computer_choose]==scissors and game_option[user_choose]==paper:
        print("You lose")
